"""OFFLINE reservation simulator (SQLite) for AVELNA. NO payment capability.

A production executor needs independent operator-grant verification, OS/process
isolation, provider authorization/quotes and actual billing reconciliation.
Do not grant this library direct provider credentials.
"""
from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Any

DEFAULT_CAPS = {"product": 9000, "ai": 2000, "media": 6000, "reserve": 3000}


class BudgetBlocked(ValueError):
    pass


def nonnegative_int(value: Any) -> int:
    if type(value) is not int or value < 0:
        raise BudgetBlocked("nonnegative_integer_required")
    return value


class DryRunLedger:
    """Atomic reservation and idempotency simulation in integer cents."""

    def __init__(self, path: str | Path, caps: dict[str, int] | None = None):
        self.path = str(path)
        self.caps = dict(DEFAULT_CAPS if caps is None else caps)
        if set(self.caps) != set(DEFAULT_CAPS):
            raise BudgetBlocked("unknown_budget_buckets")
        if any(nonnegative_int(self.caps[k]) > DEFAULT_CAPS[k] for k in DEFAULT_CAPS):
            raise BudgetBlocked("budget_bucket_exceeds_launch_plan")
        if sum(self.caps.values()) > 20000:
            raise BudgetBlocked("total_cap_exceeded")
        with self._db() as db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS reservations ("
                "idempotency_key TEXT PRIMARY KEY, bucket TEXT NOT NULL,"
                "reserved_cents INTEGER NOT NULL, status TEXT NOT NULL,"
                "actual_cents INTEGER NOT NULL DEFAULT 0)"
            )

    @contextmanager
    def _db(self):
        db = sqlite3.connect(self.path, timeout=15, isolation_level=None)
        try:
            with db:
                db.execute("PRAGMA busy_timeout = 15000")
                yield db
        finally:
            db.close()

    def reserve_simulated(self, key: str, bucket: str, max_cents: int) -> dict[str, Any]:
        """For testing only: reserve max cost; does not authorize external spending."""
        if not isinstance(key, str) or not 1 <= len(key) <= 128:
            raise BudgetBlocked("invalid_idempotency_key")
        if bucket not in self.caps:
            raise BudgetBlocked("unknown_budget_bucket")
        amount = nonnegative_int(max_cents)
        if amount == 0:
            raise BudgetBlocked("positive_reservation_required")
        with self._db() as db:
            db.execute("BEGIN IMMEDIATE")
            existing = db.execute(
                "SELECT bucket, reserved_cents, actual_cents, status "
                "FROM reservations WHERE idempotency_key=?", (key,)
            ).fetchone()
            if existing is not None:
                if existing[0] != bucket or existing[1] != amount:
                    raise BudgetBlocked("idempotency_key_conflict")
                return {"key": key, "status": existing[3], "reserved_cents": existing[1],
                        "actual_cents": existing[2], "authorizes_spending": False}
            used = db.execute(
                "SELECT COALESCE(SUM(CASE WHEN status='pending' THEN reserved_cents "
                "WHEN status='settled' THEN actual_cents ELSE 0 END),0) "
                "FROM reservations WHERE bucket=?", (bucket,)
            ).fetchone()[0]
            if used + amount > self.caps[bucket]:
                raise BudgetBlocked("budget_reservation_exceeds_bucket")
            db.execute(
                "INSERT INTO reservations(idempotency_key,bucket,reserved_cents,status)"
                " VALUES(?,?,?,'pending')", (key, bucket, amount)
            )
            db.commit()
        return {"key": key, "status": "pending", "reserved_cents": amount,
                "actual_cents": 0, "authorizes_spending": False}

    def settle_simulated(self, key: str, actual_cents: int) -> dict[str, Any]:
        """Only simulations; real settlement must verify external provider receipt."""
        actual = nonnegative_int(actual_cents)
        with self._db() as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute(
                "SELECT reserved_cents, status, actual_cents FROM reservations "
                "WHERE idempotency_key=?", (key,)
            ).fetchone()
            if row is None:
                raise BudgetBlocked("missing_reservation")
            reserved, status, old_actual = row
            if status == "settled" and actual == old_actual:
                return {"key": key, "status": "settled", "actual_cents": actual}
            if status != "pending":
                raise BudgetBlocked("not_pending")
            if actual > reserved:
                raise BudgetBlocked("actual_cost_above_reserved")
            db.execute(
                "UPDATE reservations SET status='settled',actual_cents=? "
                "WHERE idempotency_key=?", (actual, key)
            )
            db.commit()
        return {"key": key, "status": "settled", "actual_cents": actual}

    def release_no_charge_simulated(self, key: str, *, confirmed_no_charge: bool) -> None:
        """Never free a pending budget because an HTTP request merely timed out."""
        if confirmed_no_charge is not True:
            raise BudgetBlocked("no_charge_evidence_required")
        with self._db() as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute(
                "SELECT status FROM reservations WHERE idempotency_key=?", (key,)
            ).fetchone()
            if row is None or row[0] != "pending":
                raise BudgetBlocked("not_pending")
            db.execute(
                "UPDATE reservations SET status='no_charge' WHERE idempotency_key=?", (key,)
            )
            db.commit()

    def snapshot(self) -> dict[str, Any]:
        with self._db() as db:
            rows = db.execute(
                "SELECT bucket,status,reserved_cents,actual_cents FROM reservations"
            ).fetchall()
        used = {k: 0 for k in self.caps}
        pending = {k: 0 for k in self.caps}
        for bucket, status, reserved, actual in rows:
            if status == "pending":
                used[bucket] += reserved
                pending[bucket] += reserved
            elif status == "settled":
                used[bucket] += actual
        return {"caps": self.caps, "committed_including_pending": used,
                "pending": pending, "authorizes_spending": False}
