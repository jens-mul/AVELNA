"""Check AVELNA public creative references and shot packet invariants. Offline only."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class CreativePlaybookTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads((ROOT / "config/creative-element-registry.example.json").read_text(encoding="utf8"))
        cls.packet = json.loads((ROOT / "config/creative-shot-brief.example.json").read_text(encoding="utf8"))

    def test_fourteen_unique_elements_and_sanitized_ids(self):
        entries = self.registry["elements"]
        self.assertEqual(len(entries), 14)
        self.assertEqual(self.registry["current_total_elements"], len(entries))
        names = [entry["alias"] for entry in entries]
        self.assertEqual(len(names), len(set(names)))
        self.assertTrue(all(name.startswith("@AVELNA_") for name in names))
        self.assertFalse(self.registry["account_identifiers_included"])
        for entry in entries:
            self.assertIsNone(entry["reference_element_id"])
            self.assertIsNone(entry["source_media_id"])
            self.assertFalse(entry["commercially_approved"])
            self.assertFalse(entry["exact_physical_product_verified"])

    def test_old_character_is_explicitly_deprecated(self):
        entries = {entry["alias"]: entry for entry in self.registry["elements"]}
        old = entries["@AVELNA_StepWoman_01"]
        self.assertTrue(old["deprecated"])
        self.assertEqual(old["creative_status"], "deprecated_but_exists")
        self.assertEqual(old["provider_status_at_last_read"], "completed")
        for key in ("Front", "Back", "Upper", "Lower"):
            item = entries["@AVELNA_StepWoman_" + key + "_01"]
            self.assertEqual(item["creative_status"], "candidate")
            self.assertFalse(item["deprecated"])

    def test_unverified_product_not_approved(self):
        for entry in self.registry["elements"]:
            if entry["category"] == "prop":
                self.assertNotEqual(entry["creative_status"], "product_verified")
                self.assertIn(entry["usage_scope"], ("internal_only", "internal_calibration_only"))
        self.assertTrue(self.packet["concept_only"])
        self.assertFalse(self.packet["sku_locked"])
        self.assertFalse(self.packet["commercial_release_allowed"])

    def test_shot_packet_has_no_paid_grant(self):
        self.assertFalse(self.packet["grant"]["authorized"])
        self.assertIsNone(self.packet["provider"]["cost_quote_credits"])
        self.assertFalse(self.packet["prompt"]["owner_approved"])
        self.assertEqual(self.packet["camera"]["floor_outside_shower"], "dry")

    def test_prompts_docs_exist(self):
        paths = [
          "docs/creative.md",
          "docs/creative-system/01-reference-production.md",
          "docs/creative-system/02-higgsfield-elements.md",
          "docs/creative-system/03-shot-continuity.md",
          "docs/creative-system/04-production-execution-qa.md",
          "docs/creative-system/05-experiment-journal.md",
          "docs/creative-system/06-hermes-cli-handoff.md",
          "docs/creative-system/07-onboarding-checklist.md",
          "prompts/shot-02-step-out-v1.md",
          "prompts/shot-03-foot-contact-v1.md",
          "prompts/shot-04-reveal-v1.md",
        ]
        for item in paths:
            with self.subTest(file=item):
                self.assertTrue((ROOT / item).is_file())

    def test_canonical_manual_and_no_secret_account_data(self):
        md = (ROOT / "docs/creative.md").read_text(encoding="utf8").lower()
        self.assertIn("not a spending authorization", md)
        self.assertIn("technical status", md)
        raw = json.dumps(self.registry)
        self.assertNotIn("cloudfront.net", raw)
        self.assertNotIn("workspace_id", raw)
        self.assertNotIn("project_id", raw)

if __name__ == "__main__":
    unittest.main()
