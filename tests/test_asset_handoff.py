import contextlib
import copy
import hashlib
import importlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts.asset_registry import AssetBlocked

ROOT = Path(__file__).resolve().parents[1]


class HandoffTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.assets = Path(self.temp.name)/'assets'
        self.assets.mkdir()
        self.skills = Path(self.temp.name)/'dependency-test-stubs'
        routing = json.loads((ROOT/'config/skill-routing.json').read_text())
        for entry in routing['project_skills'].values():
            for name in entry['shared_skills']:
                folder = self.skills/'creative'/name
                folder.mkdir(parents=True, exist_ok=True)
                (folder/'SKILL.md').write_text('---\nname: '+name+'\ndescription: synthetic dependency-test stub\n---\nNo execution.\n')
        source = self.assets/'synthetic.png'
        source.write_bytes(b'synthetic-test-reference')
        prompt = ROOT/'prompts/editorial-master.md'
        self.manifest = {'schema_version': 2, 'purpose': 'synthetic_dry_run',
                         'product_sku': 'SYNTHETIC_NOT_A_REAL_SKU',
                         'prompt': {'path': 'prompts/editorial-master.md',
                                    'sha256': hashlib.sha256(prompt.read_bytes()).hexdigest()},
                         'assets': [{'alias': '@AVELNA_Test_01', 'path': source.name,
                                     'source_hash_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                                     'role': 'product_reference', 'status': 'owner_approved',
                                     'rights_status': 'cleared', 'product_verified': True,
                                     'approved_by': 'synthetic-test-only', 'approved_at': '2026-10-31T12:00:00Z',
                                     'synthetic': True}]}

    def module(self):
        return importlib.import_module('scripts.asset_handoff')

    def packet(self):
        return self.module().prepare_handoff(self.manifest, ROOT, self.assets, skill_root=self.skills)

    def test_packet_pins_canonical_prompt_and_exact_asset_without_execution(self):
        packet = self.packet()
        self.assertEqual(packet['prompt']['text'], (ROOT/'prompts/editorial-master.md').read_text())
        self.assertEqual(packet['prompt']['sha256'], self.manifest['prompt']['sha256'])
        self.assertEqual(packet['bindings'][0]['cli_flag'], '--image-references')
        self.assertEqual(packet['bindings'][0]['source_hash_sha256'], self.manifest['assets'][0]['source_hash_sha256'])
        self.assertFalse(packet['authorizes_spending'])
        self.assertFalse(packet['remote_handoff_verified'])
        self.assertFalse(packet['ready_to_execute'])
        self.assertEqual(packet['transport'], 'cli')
        self.assertNotIn('<<<', str(packet))

    def test_changed_prompt_hash_is_blocked(self):
        self.manifest['prompt']['sha256'] = 'a'*64
        with self.assertRaises(AssetBlocked):
            self.packet()

    def test_noncanonical_prompt_is_blocked_even_with_matching_hash(self):
        self.manifest['prompt'] = {'path': 'README.md', 'sha256': hashlib.sha256((ROOT/'README.md').read_bytes()).hexdigest()}
        with self.assertRaises(AssetBlocked):
            self.packet()

    def test_missing_shared_skill_blocks_without_reimplementation(self):
        for path in self.skills.rglob('SKILL.md'):
            with self.subTest(skill=path.parent.name):
                original = path.read_text()
                path.unlink()
                try:
                    with self.assertRaises(AssetBlocked):
                        self.packet()
                finally:
                    path.write_text(original)

    def test_old_manifest_or_non_cli_override_is_rejected(self):
        for mutation in [{'schema_version': 1}, {'transport': 'mcp'}]:
            with self.subTest(mutation=mutation):
                old = copy.deepcopy(self.manifest)
                self.manifest.update(mutation)
                try:
                    with self.assertRaises(AssetBlocked):
                        self.packet()
                finally:
                    self.manifest = old

    def test_production_packet_carries_sku_and_manifest_fingerprint(self):
        self.manifest['purpose'] = 'production_preparation'
        self.manifest['product_sku'] = 'TEST_DECLARATION_NOT_A_VERIFIED_PRODUCT'
        self.manifest['assets'][0]['synthetic'] = False
        packet = self.packet()
        self.assertEqual(packet.get('product_sku'), self.manifest['product_sku'])
        fingerprint = hashlib.sha256(json.dumps(self.manifest, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()
        self.assertEqual(packet['manifest_sha256'], fingerprint)
        self.assertFalse(packet['authorizes_spending'])
        self.assertFalse(packet['ready_to_execute'])

    def test_production_preparation_requires_exact_sku(self):
        self.manifest['purpose'] = 'production_preparation'
        self.manifest['assets'][0]['synthetic'] = False
        for sku in [None, '', 'SYNTHETIC_NOT_A_REAL_SKU']:
            with self.subTest(sku=sku):
                self.manifest['product_sku'] = sku
                with self.assertRaises(AssetBlocked):
                    self.packet()

    def test_handoff_never_calls_shell_or_network(self):
        with patch('subprocess.run') as shell, patch('socket.socket') as network:
            self.packet()
            shell.assert_not_called()
            network.assert_not_called()

    def test_demo_command_uses_real_files_but_never_executes_higgsfield(self):
        module = self.module()
        self.assertTrue(callable(getattr(module, 'main', None)), 'Need executable local dry-run proof')
        with patch('subprocess.run') as shell, patch('socket.socket') as network:
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                result = module.main(['--demo', '--skill-root', str(self.skills)])
            shell.assert_not_called()
            network.assert_not_called()
        self.assertEqual(result, 0)
        report = json.loads(output.getvalue())
        self.assertTrue(report['local_handoff_verified'])
        self.assertTrue(report['synthetic'])
        self.assertEqual(report['provider_calls'], 0)
        self.assertEqual(report['credits_spent'], 0)
        self.assertFalse(report['remote_handoff_verified'])

    def test_private_output_does_not_echo_packet_to_stdout(self):
        manifest_path = Path(self.temp.name)/'manifest.json'
        manifest_path.write_text(json.dumps(self.manifest))
        destination = Path(self.temp.name)/'private-packet.json'
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = self.module().main(['--manifest', str(manifest_path), '--asset-root', str(self.assets),
                                         '--skill-root', str(self.skills), '--output', str(destination)])
        self.assertEqual(result, 0)
        status = json.loads(output.getvalue())
        self.assertEqual(set(status), {'packet_written', 'local_handoff_verified', 'authorizes_spending'})
        self.assertTrue(status['packet_written'])
        self.assertNotIn(str(self.assets), output.getvalue())
        self.assertIn('bindings', json.loads(destination.read_text()))

    def test_private_output_is_owner_only_and_never_overwritten(self):
        destination = Path(self.temp.name)/'private-report.json'
        with contextlib.redirect_stdout(io.StringIO()):
            result = self.module().main(['--demo', '--skill-root', str(self.skills), '--output', str(destination)])
        self.assertEqual(result, 0)
        self.assertEqual(destination.stat().st_mode & 0o777, 0o600)
        before = destination.read_bytes()
        with contextlib.redirect_stdout(io.StringIO()):
            again = self.module().main(['--demo', '--skill-root', str(self.skills), '--output', str(destination)])
        self.assertNotEqual(again, 0)
        self.assertEqual(destination.read_bytes(), before)

    def test_private_packet_cannot_overwrite_public_repo_file(self):
        module = self.module()
        self.assertTrue(callable(getattr(module, 'main', None)))
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = module.main(['--demo', '--skill-root', str(self.skills), '--output', str(ROOT/'README.md')])
        self.assertNotEqual(result, 0)
        self.assertEqual(json.loads(output.getvalue())['error'], 'output_must_be_private')


if __name__ == '__main__':
    unittest.main()
