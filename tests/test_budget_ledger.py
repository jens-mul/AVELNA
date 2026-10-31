import sqlite3
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from scripts.budget_ledger import BudgetBlocked, DryRunLedger


class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.db = Path(self.tmp.name) / "test.sqlite"
        self.ledger = DryRunLedger(self.db)

    def test_db_context_closes_connection_on_every_exit(self):
        for fail in (False, True):
            with self.subTest(fail=fail):
                db = None
                try:
                    try:
                        with self.ledger._db() as db:
                            db.execute("BEGIN IMMEDIATE")
                            db.execute(
                                "INSERT INTO reservations VALUES (?, 'ai', 1, 'pending', 0)",
                                (f"context-{fail}",),
                            )
                            if fail:
                                raise RuntimeError("abort transaction")
                    except RuntimeError as error:
                        self.assertEqual(str(error), "abort transaction")
                    assert db is not None
                    with self.assertRaisesRegex(sqlite3.ProgrammingError, "closed"):
                        db.execute("SELECT 1")
                    with self.ledger._db() as check:
                        count = check.execute(
                            "SELECT COUNT(*) FROM reservations WHERE idempotency_key=?",
                            (f"context-{fail}",),
                        ).fetchone()[0]
                    self.assertEqual(count, 0 if fail else 1)
                finally:
                    if db is not None:
                        db.close()

    def test_reservation_and_settlement(self):
        self.ledger.reserve_simulated("task1", "ai", 1000)
        self.assertEqual(self.ledger.snapshot()["committed_including_pending"]["ai"], 1000)
        self.ledger.settle_simulated("task1", 800)
        self.assertEqual(self.ledger.snapshot()["committed_including_pending"]["ai"], 800)
        self.assertFalse(self.ledger.snapshot()["authorizes_spending"])

    def test_idempotency_prevents_double_spend(self):
        first = self.ledger.reserve_simulated("same", "media", 1000)
        second = self.ledger.reserve_simulated("same", "media", 1000)
        self.assertEqual(first, second)
        self.assertEqual(self.ledger.snapshot()["committed_including_pending"]["media"], 1000)

    def test_idempotency_key_conflict(self):
        self.ledger.reserve_simulated("same", "ai", 500)
        with self.assertRaises(BudgetBlocked):
            self.ledger.reserve_simulated("same", "ai", 600)

    def test_limit(self):
        self.ledger.reserve_simulated("cap", "ai", 2000)
        with self.assertRaises(BudgetBlocked):
            self.ledger.reserve_simulated("extra", "ai", 1)

    def test_no_oversettlement(self):
        self.ledger.reserve_simulated("task", "ai", 500)
        with self.assertRaises(BudgetBlocked):
            self.ledger.settle_simulated("task", 501)

    def test_timeout_does_not_release_budget(self):
        self.ledger.reserve_simulated("pending", "media", 6000)
        with self.assertRaises(BudgetBlocked):
            self.ledger.release_no_charge_simulated("pending", confirmed_no_charge=False)
        self.assertEqual(self.ledger.snapshot()["pending"]["media"], 6000)
        self.ledger.release_no_charge_simulated("pending", confirmed_no_charge=True)
        self.assertEqual(self.ledger.snapshot()["pending"]["media"], 0)

    def test_concurrent_attempts_not_overdrawn(self):
        def task(i):
            try:
                self.ledger.reserve_simulated("job-" + str(i), "ai", 1200)
                return True
            except BudgetBlocked:
                return False
        with ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(task, range(4)))
        self.assertEqual(sum(results), 1)
        self.assertEqual(self.ledger.snapshot()["committed_including_pending"]["ai"], 1200)

    def test_invalid_budget(self):
        with self.assertRaises(BudgetBlocked):
            DryRunLedger(self.db, {"product": 9000, "ai": 2000, "media": 6001, "reserve": 2999})


if __name__ == "__main__":
    unittest.main()
