import unittest
from copy import deepcopy
from datetime import datetime, timezone

from scripts.preflight import CAPS, CHECKS, contribution, review_readiness

NOW = datetime(2026, 10, 31, 12, 0, tzinfo=timezone.utc)


def packet():
    policy = {
        "currency": "EUR", "execution": "prepare_only",
        "paid_execution_enabled": False, "require_operator_grant": True,
        "total_cap_cents": 20000, "bucket_caps_cents": dict(CAPS),
    }
    state = {
        "committed_including_pending_cents": {k: 0 for k in CAPS},
        "checks": {k: True for k in CHECKS},
        "saleable_stock": 3,
        "snapshot_at": "2026-10-31T11:59:00+00:00",
        "unreconciled_mutations": [],
    }
    return policy, state


class PreflightTests(unittest.TestCase):
    def test_contribution(self):
        offer = {
            "currency": "EUR", "vat_basis_points": 2100,
            "price_incl_cents": 4995, "shipping_charged_incl_cents": 0,
            "landed_cents": 1200, "outbound_and_pack_cents": 800,
            "payment_cents": 50, "expected_returns_cents": 200,
            "variable_labour_cents": 0, "target_contribution_cents": 500,
        }
        calc = contribution(offer)
        self.assertEqual(calc["revenue_ex_vat_cents"], 4128)
        self.assertEqual(calc["contribution_before_ads_cents"], 1878)
        self.assertEqual(calc["target_media_cac_cents"], 1378)
        offer["landed_cents"] = -1
        with self.assertRaises(ValueError):
            contribution(offer)

    def test_readiness_never_authorizes_spending(self):
        result = review_readiness(*packet(), now=NOW)
        self.assertTrue(result["ready_for_operator_review"])
        self.assertFalse(result["authorizes_spending"])

    def test_stock_zero(self):
        p, s = packet()
        s["saleable_stock"] = 0
        self.assertFalse(review_readiness(p, s, NOW)["ready_for_operator_review"])

    def test_unverified_boolean_string(self):
        p, s = packet()
        s["checks"]["product_locked"] = "true"
        self.assertFalse(review_readiness(p, s, NOW)["ready_for_operator_review"])

    def test_pending_costs_count(self):
        p, s = packet()
        s["committed_including_pending_cents"]["ai"] = 2001
        self.assertFalse(review_readiness(p, s, NOW)["ready_for_operator_review"])

    def test_no_reallocation(self):
        p, s = packet()
        p["bucket_caps_cents"]["media"] += 100
        p["bucket_caps_cents"]["reserve"] -= 100
        self.assertFalse(review_readiness(p, s, NOW)["ready_for_operator_review"])

    def test_stale_or_naive_time(self):
        p, s = packet()
        for value in ("2026-10-30T11:59:00Z", "2026-10-31T12:00:00"):
            s["snapshot_at"] = value
            self.assertFalse(review_readiness(p, s, NOW)["ready_for_operator_review"])

    def test_invalid_timestamp_not_reflected(self):
        p, s = packet()
        s["snapshot_at"] = "FAKE_SECRET_CONTENT"
        result = review_readiness(p, s, NOW)
        self.assertFalse(result["ready_for_operator_review"])
        self.assertNotIn("FAKE_SECRET_CONTENT", str(result))

    def test_unknown_mutation(self):
        p, s = packet()
        s["unreconciled_mutations"] = ["unknown-task"]
        self.assertFalse(review_readiness(p, s, NOW)["ready_for_operator_review"])

    def test_unknown_paid_flag(self):
        p, s = packet()
        p["paid_execution_enabled"] = True
        self.assertFalse(review_readiness(p, s, NOW)["ready_for_operator_review"])
        p, s = packet()
        p["require_operator_grant"] = False
        self.assertFalse(review_readiness(p, s, NOW)["ready_for_operator_review"])


if __name__ == "__main__":
    unittest.main()
