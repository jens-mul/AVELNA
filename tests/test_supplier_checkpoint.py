"""Offline checks for the redacted supplier checkpoint; no external calls."""
import json
import unittest
from pathlib import Path

CATALOG = Path(__file__).resolve().parents[1] / "catalog"


def records(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from records(child)
    elif isinstance(value, list):
        for child in value:
            yield from records(child)


class SupplierCheckpointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.checkpoint = json.loads((CATALOG / "checkpoint.json").read_text(encoding="utf-8"))
        cls.luca = json.loads((CATALOG / "products/luca-sink-set.json").read_text(encoding="utf-8"))
        cls.shower = json.loads((CATALOG / "products/shower-holder.json").read_text(encoding="utf-8"))

    def test_sources_and_links(self):
        sources = json.loads((CATALOG / "sources.json").read_text(encoding="utf-8"))["sources"]
        source_ids = {source["id"] for source in sources}
        for record in records(self.checkpoint):
            if "source_ids" in record:
                self.assertTrue(set(record["source_ids"]).issubset(source_ids))
        for relative in [self.checkpoint["readme"]] + [item["product_file"] for item in self.checkpoint["sample_basket"]["items"]]:
            path = (CATALOG / relative).resolve()
            path.relative_to(CATALOG.resolve())
            self.assertTrue(path.is_file())
        for product in (self.luca, self.shower):
            self.assertEqual(product["status_checkpoint_file"], "checkpoint.json")

    def test_ai_response_is_not_a_quote_or_approval(self):
        contact = self.checkpoint["luca_contact"]
        self.assertEqual(contact["listing_id"], self.luca["identity"]["listing_id"])
        self.assertFalse(contact["human_response_received"])
        self.assertFalse(contact["manager_confirmation_received"])
        for claim in contact["response_claims"]:
            self.assertEqual(claim["status"], "ai_claim_unverified")
            self.assertFalse(claim["human_confirmed"])
            self.assertFalse(claim["publishable"])
        for name in ("sample_quote", "five_set_quote"):
            self.assertEqual(contact[name]["status"], "not_received")
            self.assertIsNone(contact[name]["confirmed_delivered_total_minor"])
        self.assertFalse(self.luca["publication"]["ready"])
        self.assertFalse(self.luca["selection"]["purchase_authorized"])
        self.assertEqual(self.luca["content_draft"]["approved_claims"], [])
        self.assertIsNone(self.luca["facts"]["exact_box_contents"]["value"])

    def test_requested_components_and_sample_quantities(self):
        request = self.checkpoint["luca_contact"]["request"]
        self.assertEqual(sum(item["quantity"] for item in request["requested_components"]), 5)
        self.assertEqual(request["sample_complete_sets"], 1)
        self.assertEqual(request["separate_follow_up_quote_complete_sets"], 5)
        quantities = {item["product_id"]: item["quantity"] for item in self.checkpoint["sample_basket"]["items"]}
        self.assertEqual(quantities, {"bath-stone": 2, "luca-sink-set": 1, "shower-holder": 1})

    def test_partial_costs_never_become_a_delivered_total(self):
        basket = self.checkpoint["sample_basket"]
        items = {item["product_id"]: item for item in basket["items"]}
        bath, luca, shower = (items[name] for name in ("bath-stone", "luca-sink-set", "shower-holder"))
        self.assertEqual(bath["provisional_subtotal_minor"], bath["quantity"] * bath["unit_product_minor"] + bath["shipping_total_minor"])
        expected = bath["provisional_subtotal_minor"] + luca["unit_product_minor"] + shower["planning_product_allowance_minor"] + shower["shipping_total_minor"]
        self.assertEqual(basket["provisional_base_eur_minor"], expected)
        self.assertEqual(expected, 5434)
        self.assertIsNone(luca["shipping_total_minor"])
        self.assertIsNone(shower["unit_product_minor"])
        self.assertIsNone(basket["confirmed_delivered_total_eur_minor"])
        self.assertFalse(basket["all_in_quote_complete"])
        shipping = self.shower["commercial_observations"]["shipping_observation"]
        self.assertEqual(shipping["quantity"], 1)
        self.assertEqual(shipping["total_minor"], 0)
        self.assertFalse(shipping["inherited_for_other_quantities"])
        self.assertFalse(shipping["final_checkout_verified"])

    def test_no_new_permissions_or_private_payload(self):
        privacy = self.checkpoint["privacy"]
        self.assertTrue(privacy["public_summary_only"])
        for field in ("raw_chat_stored", "screenshot_stored", "buyer_name_stored", "destination_postcode_stored"):
            self.assertFalse(privacy[field])
        self.assertFalse(self.checkpoint["sample_basket"]["purchase_authorized"])
        self.assertFalse(self.checkpoint["budget_status"]["new_budget_approved"])
        self.assertFalse(self.checkpoint["budget_status"]["bucket_reallocation_approved"])
        self.assertFalse(self.checkpoint["after_response"]["assistant_supplier_contact_authorized"])
        self.assertFalse(self.checkpoint["after_response"]["automatic_follow_up_or_monitoring_created"])
        for record in records(self.checkpoint):
            for key, value in record.items():
                if key.endswith("_minor") and value is not None:
                    self.assertIs(type(value), int, key)
                    self.assertGreaterEqual(value, 0, key)


if __name__ == "__main__":
    unittest.main()
