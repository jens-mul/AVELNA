import copy
import hashlib
from pathlib import Path
import tempfile
import unittest

from scripts import asset_registry


class AssetRegistryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root/'source.png'
        self.source.write_bytes(b'synthetic-file-hash-fixture-not-a-product-photo')
        self.record = {
            'alias': '@AVELNA_Test_01', 'path': 'source.png',
            'source_hash_sha256': hashlib.sha256(self.source.read_bytes()).hexdigest(),
            'role': 'product_reference', 'status': 'owner_approved',
            'rights_status': 'cleared', 'product_verified': True,
            'approved_by': 'synthetic-test-only', 'approved_at': '2026-10-31T12:00:00Z',
            'synthetic': True,
        }
        self.contract = {'roles': {'product_reference': '--image-references'},
                         'max_asset_bytes': 1024, 'allowed_extensions': ['.png']}

    def resolve(self, records=None, *, purpose='synthetic_dry_run'):
        return asset_registry.resolve_assets([self.record] if records is None else records,
                                             self.root, self.contract, purpose=purpose)

    def test_approved_local_asset_becomes_role_bound_cli_reference(self):
        out = self.resolve()
        self.assertEqual(out[0]['cli_flag'], '--image-references')
        self.assertEqual(out[0]['path'], str(self.source.resolve()))
        self.assertEqual(out[0]['source_hash_sha256'], self.record['source_hash_sha256'])
        self.assertNotIn('<<<', str(out))

    def test_invalid_approval_rights_role_or_hash_is_blocked(self):
        variants = {
            'alias': '@UNKNOWN', 'status': 'candidate', 'rights_status': 'unverified',
            'product_verified': 'true', 'approved_by': '', 'approved_at': 'not-a-date',
            'source_hash_sha256': 'a'*64, 'role': 'invented', 'synthetic': False,
        }
        for key, value in variants.items():
            with self.subTest(field=key):
                record = copy.deepcopy(self.record)
                record[key] = value
                with self.assertRaises(asset_registry.AssetBlocked):
                    self.resolve([record])

    def test_changed_bytes_invalidate_approval(self):
        self.source.write_bytes(b'different-content')
        with self.assertRaises(asset_registry.AssetBlocked):
            self.resolve()

    def test_missing_file_is_blocked(self):
        self.source.unlink()
        with self.assertRaises(asset_registry.AssetBlocked):
            self.resolve()

    def test_paths_cannot_escape_asset_root_even_via_symlink(self):
        with tempfile.TemporaryDirectory() as other:
            external = Path(other)/'outside.png'
            external.write_bytes(self.source.read_bytes())
            link = self.root/'link.png'
            link.symlink_to(external)
            for value in [str(external), '../outside.png', 'link.png', 'https://example.test/a.png']:
                with self.subTest(path=value):
                    record = dict(self.record, path=value)
                    with self.assertRaises(asset_registry.AssetBlocked):
                        self.resolve([record])

    def test_empty_and_duplicate_assets_are_blocked(self):
        for records in [[], [self.record, self.record]]:
            with self.subTest(records=len(records)):
                with self.assertRaises(asset_registry.AssetBlocked):
                    self.resolve(records)

    def test_synthetic_asset_is_not_production_input(self):
        with self.assertRaises(asset_registry.AssetBlocked):
            self.resolve(purpose='production_preparation')

    def test_file_size_and_extension_are_bounded(self):
        for change in [{'max_asset_bytes': 1}, {'allowed_extensions': ['.jpg']}]:
            with self.subTest(change=change):
                old = self.contract.copy()
                self.contract.update(change)
                try:
                    with self.assertRaises(asset_registry.AssetBlocked):
                        self.resolve()
                finally:
                    self.contract = old


if __name__ == '__main__':
    unittest.main()
