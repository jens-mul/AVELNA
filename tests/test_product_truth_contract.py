import json
from pathlib import Path
import unittest


class ProductTruthContractTests(unittest.TestCase):
    def test_missing_physical_facts_are_null(self):
        p = Path(__file__).resolve().parents[1] / "config" / "product-truth-vdstm007.json"
        m = json.loads(p.read_text(encoding="utf8"))
        facts = m["product_facts"]
        self.assertEqual((facts["long_side_mm"], facts["short_side_mm"]), (600,390))
        self.assertIsNone(facts["thickness_mm"])
        self.assertIsNone(facts["net_weight_grams"])
        self.assertIsNone(facts["backing_type"])

    def test_source_rights_and_exact_identity_not_approved(self):
        p = Path(__file__).resolve().parents[1] / "config" / "product-truth-vdstm007.json"
        m = json.loads(p.read_text(encoding="utf8"))
        self.assertFalse(m["state"]["image_rights_cleared"])
        self.assertFalse(m["state"]["exact_sku_identity_verified"])
        self.assertFalse(m["state"]["commercial_master_approved"])
        self.assertFalse(m["source"]["published_in_public_repo"])

    def test_source_hash_is_present_and_well_formed(self):
        m = json.loads((Path(__file__).resolve().parents[1] / "config" / "product-truth-vdstm007.json").read_text(encoding="utf8"))
        self.assertEqual(len(m["source"]["sha256"]),64)
        int(m["source"]["sha256"],16)


if __name__ == "__main__":
    unittest.main()
