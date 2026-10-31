import unittest
from copy import deepcopy

from scripts.asset_registry import AssetBlocked, resolve_aliases, safe_alias_manifest

MODEL = "nano_banana_2"
UUID = "123e4567-e89b-42d3-a456-426614174000"


def registry():
    return {"@AVELNA_BathStone_01": {
        "alias": "@AVELNA_BathStone_01",
        "status": "production_enabled", "rights_status": "cleared",
        "product_verified": True, "approved_for_paid_ads": True,
        "approved_by": "operator-confirmed", "approved_at": "2026-10-31T12:00:00Z",
        "source_hash_sha256": "a" * 64, "element_status": "completed",
        "reference_element_id": UUID, "usable_models": [MODEL],
    }}


class AssetRegistryTests(unittest.TestCase):
    def test_replace_only_known_approved_alias(self):
        out = resolve_aliases("Use @AVELNA_BathStone_01 exactly.",
                              registry(), model_id=MODEL,
                              observed_supported_models={MODEL})
        self.assertEqual(out, "Use <<<" + UUID + ">>> exactly.")

    def test_no_element_when_model_unsupported(self):
        with self.assertRaises(AssetBlocked):
            resolve_aliases("@AVELNA_BathStone_01", registry(),
                            model_id="unknown", observed_supported_models={MODEL})

    def test_unapproved_asset_is_blocked(self):
        r = registry()
        r["@AVELNA_BathStone_01"]["approved_for_paid_ads"] = False
        with self.assertRaises(AssetBlocked):
            resolve_aliases("@AVELNA_BathStone_01", r,
                            model_id=MODEL, observed_supported_models={MODEL})

    def test_invalid_uuid_or_hash_blocked(self):
        r = registry()
        r["@AVELNA_BathStone_01"]["reference_element_id"] = "fake"
        with self.assertRaises(AssetBlocked):
            resolve_aliases("@AVELNA_BathStone_01", r,
                            model_id=MODEL, observed_supported_models={MODEL})
        r = registry()
        r["@AVELNA_BathStone_01"]["source_hash_sha256"] = None
        with self.assertRaises(AssetBlocked):
            resolve_aliases("@AVELNA_BathStone_01", r,
                            model_id=MODEL, observed_supported_models={MODEL})

    def test_untrusted_placeholder_is_blocked(self):
        with self.assertRaises(AssetBlocked):
            resolve_aliases("<<<unknown>>>", registry(),
                            model_id=MODEL, observed_supported_models={MODEL})

    def test_unknown_alias_is_blocked(self):
        with self.assertRaises(AssetBlocked):
            resolve_aliases("@AVELNA_NotInLibrary", registry(),
                            model_id=MODEL, observed_supported_models={MODEL})

    def test_public_view_excludes_ids_and_identity(self):
        safe = safe_alias_manifest(next(iter(registry().values())))
        self.assertNotIn("reference_element_id", safe)
        self.assertNotIn("approved_by", safe)
        self.assertTrue(safe["rights_cleared"])


if __name__ == "__main__":
    unittest.main()
