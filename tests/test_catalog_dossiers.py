"""Offline integrity tests for the product dossiers; not product certification."""
import json
import unittest
from datetime import date
from pathlib import Path

CATALOG = Path(__file__).resolve().parents[1] / "catalog"


def dictionaries(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from dictionaries(child)
    elif isinstance(value, list):
        for child in value:
            yield from dictionaries(child)


class CatalogDossierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.collection = json.loads((CATALOG / "collection-01.json").read_text(encoding="utf-8"))
        cls.sources = json.loads((CATALOG / "sources.json").read_text(encoding="utf-8"))["sources"]
        cls.products = [json.loads((CATALOG / p).read_text(encoding="utf-8")) for p in cls.collection["product_files"]]

    def test_json_documents(self):
        paths = list(CATALOG.rglob("*.json"))
        self.assertGreaterEqual(len(paths), 5)
        for path in paths:
            with self.subTest(path=path):
                document = json.loads(path.read_text(encoding="utf-8"))
                self.assertIsInstance(document, dict)
                self.assertEqual(document["schema_version"], "1.0.0")

    def test_products_and_research_links(self):
        self.assertEqual({p["product_id"] for p in self.products}, {"bath-stone", "shower-holder", "luca-sink-set"})
        paths = self.collection["product_files"] + self.collection["research_files"]
        paths += [p["research_file"] for p in self.products]
        paths += ["README.md", "BUILD-HANDOFF.md", "NEXT-STEPS.md"]
        for relative in paths:
            resolved = (CATALOG / relative).resolve()
            resolved.relative_to(CATALOG.resolve())
            self.assertTrue(resolved.is_file(), relative)

    def test_source_references(self):
        ids = [s["id"] for s in self.sources]
        self.assertEqual(len(ids), len(set(ids)))
        for document in [self.collection] + self.products:
            for item in dictionaries(document):
                if "source_ids" in item:
                    self.assertIsInstance(item["source_ids"], list)
                    self.assertLessEqual(set(item["source_ids"]), set(ids))
        for source in self.sources:
            self.assertTrue(source["limitations"])
            self.assertTrue(source["retrieval_status"])
            if source["observed_on"] is not None:
                date.fromisoformat(source["observed_on"])
            if source["url"] is not None:
                self.assertTrue(source["url"].startswith("https://"))

    def test_fact_status_and_dates(self):
        allowed = {"supplier_reported", "repository_record", "conflicted", "unknown"}
        for product in self.products:
            for name, fact in product["facts"].items():
                with self.subTest(product=product["product_id"], field=name):
                    self.assertEqual(set(fact), {"value", "status", "source_ids", "observed_on"})
                    self.assertIn(fact["status"], allowed)
                    if fact["status"] == "unknown":
                        self.assertIsNone(fact["value"])
                        self.assertIsNone(fact["observed_on"])
                    else:
                        self.assertIsNotNone(fact["value"])
                        self.assertTrue(fact["source_ids"])
                        date.fromisoformat(fact["observed_on"])

    def test_minor_units(self):
        for product in self.products:
            self.assertIn(product["commercial_observations"]["currency"], {"USD", "EUR"})
            for item in dictionaries(product):
                for key, value in item.items():
                    if "_minor" in key and value is not None:
                        values = value.values() if isinstance(value, dict) else [value]
                        for amount in values:
                            self.assertIs(type(amount), int, (key, amount))
                            self.assertGreaterEqual(amount, 0)

    def test_draft_publication_guards(self):
        for product in self.products:
            state = product["publication"]
            if not state["ready"]:
                self.assertFalse(state["checkout_enabled"])
            if state["checkout_enabled"]:
                for field in ["approved_by", "approved_on", "approved_retail_price_eur_minor_including_vat", "saleable_stock"]:
                    self.assertIsNotNone(state[field])
                self.assertTrue(product["media"]["rights_verified"])
                self.assertTrue(product["media"]["exact_product_match_verified"])
            for assumption in product["planning_assumptions"]:
                self.assertFalse(assumption["allowed_in_public_copy"])
            self.assertTrue(product["content_draft"]["do_not_publish_without_evidence"])

    def test_complete_set_planning_assumption(self):
        luca = next(p for p in self.products if p["product_id"] == "luca-sink-set")
        assumption = next(a for a in luca["planning_assumptions"] if a["id"] == "LUCA-ONE-PIECE-ONE-SET")
        self.assertEqual(assumption["value"], {"published_pieces": 1, "complete_sets": 1})
        self.assertIn("USER-20261108", assumption["source_ids"])

    def test_listing_and_blocker_ids(self):
        for product in self.products:
            identity = product["identity"]
            self.assertIn(identity["listing_id"], identity["product_url"])
            ids = [item["id"] for item in product["open_items"]]
            self.assertTrue(ids)
            self.assertEqual(len(ids), len(set(ids)))
            for item in product["open_items"]:
                for field in ["required", "method", "blocks"]:
                    self.assertTrue(item[field])

    def test_zoso_selection_does_not_inherit_yongye_identity(self):
        bath = next(p for p in self.products if p["product_id"] == "bath-stone")
        self.assertEqual(bath["identity"]["listing_id"], "1601426633204")
        self.assertEqual(bath["facts"]["supplier_name"]["value"], "Yiwu Zoso Craft Co., Ltd.")
        self.assertNotEqual(bath["facts"]["supplier_model"]["value"], "VDSTM-007")
        self.assertEqual(bath["superseded_listing"]["listing_id"], "1601587124238")
        self.assertEqual(bath["facts"]["published_moq"]["value"], 2)
        self.assertIn("USER-ZOSO-LOCK", bath["selection"]["source_ids"])
        self.assertFalse(bath["selection"]["purchase_authorized"])
        self.assertFalse(bath["media"]["exact_product_match_verified"])
        self.assertIsNone(bath["identity"]["exact_variant_id"])

    def test_zoso_shipping_is_quantity_scoped_and_subtotal_is_not_landed_cost(self):
        bath = next(p for p in self.products if p["product_id"] == "bath-stone")
        commercial = bath["commercial_observations"]
        shipping = commercial["shipping_observation"]
        self.assertEqual(shipping["destination_country"], "NL")
        self.assertEqual(shipping["currency"], "EUR")
        self.assertEqual(shipping["quantity"], 2)
        self.assertEqual(shipping["total_minor"], 2692)
        self.assertEqual(shipping["per_unit_minor"], 1346)
        self.assertEqual(shipping["per_unit_minor"] * shipping["quantity"], shipping["total_minor"])
        self.assertEqual(commercial["netherlands_shipping_price_minor"], shipping["total_minor"])
        self.assertEqual(shipping["displayed_struck_through_total_minor"] - shipping["displayed_discount_minor"], shipping["total_minor"])
        self.assertIsNone(shipping["five_unit_shipping_total_minor"])
        self.assertFalse(shipping["inherited_for_other_quantities"])
        self.assertFalse(shipping["final_checkout_verified"])
        assumptions = {a["id"]: a["value"] for a in bath["planning_assumptions"]}
        self.assertEqual(assumptions["BATH-SAMPLE-QTY"], 2)
        subtotal = assumptions["BATH-TWO-UNIT-SUBTOTAL"]
        self.assertEqual(subtotal["items_total_minor"], subtotal["quantity"] * subtotal["unit_item_price_minor"])
        self.assertEqual(subtotal["shipping_total_minor"], shipping["total_minor"])
        self.assertEqual(subtotal["subtotal_minor"], subtotal["items_total_minor"] + subtotal["shipping_total_minor"])
        self.assertEqual(subtotal["subtotal_per_unit_minor"] * subtotal["quantity"], subtotal["subtotal_minor"])
        self.assertIsNone(commercial["landed_cost_eur_minor_ex_recoverable_vat"])
        self.assertIsNone(commercial["cash_cost_eur_minor_including_taxes"])


if __name__ == "__main__":
    unittest.main()
