"""AVELNA dry-run readiness and unit economics. No provider calls or grants."""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from decimal import Decimal, ROUND_HALF_UP
from typing import Any

CAPS = {"product": 9000, "ai": 2000, "media": 6000, "reserve": 3000}
CHECKS = (
    "product_locked", "image_rights_verified", "safety_reviewed",
    "brand_name_reviewed", "offer_verified", "checkout_verified",
    "consent_verified", "tracking_tested", "capabilities_verified",
    "execution_isolated",
)
COST_KEYS = (
    "landed_cents", "outbound_and_pack_cents", "payment_cents",
    "expected_returns_cents", "variable_labour_cents",
)


def cents(value: Any, name: str) -> int:
    if type(value) is not int or value < 0:
        raise ValueError(f"{name}: non-negative integer cents required")
    return value


def parse_aware_time(value: Any) -> datetime:
    if not isinstance(value, str):
        raise ValueError("timestamp: timezone-aware ISO string required")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if dt.tzinfo is None or dt.utcoffset() is None:
            raise ValueError("missing timezone")
        return dt.astimezone(timezone.utc)
    except (ValueError, OverflowError, TypeError):
        raise ValueError("timestamp: valid timezone-aware ISO value required") from None


def contribution(offer: dict[str, Any]) -> dict[str, int]:
    """Scenario only; assumes VAT recoverability, never infers Dutch KOR selection."""
    if not isinstance(offer, dict) or offer.get("currency") != "EUR":
        raise ValueError("EUR offer object required")
    vat = cents(offer.get("vat_basis_points"), "vat_basis_points")
    if vat > 10000:
        raise ValueError("unsupported VAT rate")
    gross = cents(offer.get("price_incl_cents"), "price_incl_cents")
    gross += cents(offer.get("shipping_charged_incl_cents"), "shipping_charged_incl_cents")
    revenue = Decimal(gross) / (Decimal(1) + Decimal(vat) / Decimal(10000))
    rounded_revenue = int(revenue.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    variable = sum(cents(offer.get(key), key) for key in COST_KEYS)
    before_ads = rounded_revenue - variable
    target = cents(offer.get("target_contribution_cents"), "target_contribution_cents")
    return {
        "revenue_ex_vat_cents": rounded_revenue,
        "contribution_before_ads_cents": before_ads,
        "break_even_media_cac_cents": before_ads,
        "target_media_cac_cents": before_ads - target,
    }


def review_readiness(
    policy: dict[str, Any],
    state: dict[str, Any],
    now: datetime | None = None,
) -> dict[str, Any]:
    """Review packet only. NEVER returns spend approval."""
    now = now or datetime.now(timezone.utc)
    if not isinstance(now, datetime) or now.tzinfo is None or now.utcoffset() is None:
        raise ValueError("now: timezone-aware datetime required")
    errs: list[str] = []
    try:
        if not isinstance(policy, dict) or not isinstance(state, dict):
            raise ValueError("policy and state objects required")
        if policy.get("currency") != "EUR":
            errs.append("wrong_currency")
        if policy.get("execution") != "prepare_only" or policy.get("paid_execution_enabled") is not False:
            errs.append("starter_is_prepare_only")
        if policy.get("require_operator_grant") is not True:
            errs.append("missing_operator_gate")
        total = cents(policy.get("total_cap_cents"), "total_cap_cents")
        caps = policy.get("bucket_caps_cents")
        spent = state.get("committed_including_pending_cents")
        if not isinstance(caps, dict) or set(caps) != set(CAPS):
            raise ValueError("invalid budget buckets")
        if not isinstance(spent, dict) or set(spent) != set(CAPS):
            raise ValueError("invalid committed buckets")
        if total != sum(cents(caps[k], k) for k in CAPS):
            errs.append("budget_sum_mismatch")
        if total > 20000:
            errs.append("overall_cap_exceeded")
        for k, upper in CAPS.items():
            amount = cents(caps[k], k)
            committed = cents(spent[k], "committed_" + k)
            if amount > upper:
                errs.append("bucket_cap_exceeded_" + k)
            if committed > amount:
                errs.append("bucket_overspent_" + k)
        checks = state.get("checks")
        if not isinstance(checks, dict):
            raise ValueError("checks object required")
        for k in CHECKS:
            if checks.get(k) is not True:
                errs.append("not_verified_" + k)
        if type(state.get("saleable_stock")) is not int or state["saleable_stock"] < 1:
            errs.append("no_saleable_stock")
        if state.get("unreconciled_mutations") != []:
            errs.append("unreconciled_mutation")
        age = now.astimezone(timezone.utc) - parse_aware_time(state.get("snapshot_at"))
        if age > timedelta(minutes=15) or age < -timedelta(seconds=60):
            errs.append("stale_or_future_snapshot")
    except (ValueError, TypeError, KeyError) as exc:
        errs.append(str(exc))
    return {
        "ready_for_operator_review": not errs,
        "authorizes_spending": False,
        "errors": errs,
    }


if __name__ == "__main__":
    print(json.dumps({
        "status": "offline_library",
        "authorizes_spending": False,
        "note": "Run tests and build independent executor before paid mode.",
    }, indent=2))
