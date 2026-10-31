"""Project architecture invariants; no account or network access."""
import ast
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ArchitectureTests(unittest.TestCase):
    def test_shared_skills_are_referenced_not_vendored(self):
        routing = json.loads((ROOT/'config/skill-routing.json').read_text())
        self.assertEqual(routing['scope'], 'project_only')
        self.assertEqual(routing['missing_dependency_action'],
                         'BLOCKED_do_not_copy_install_or_reimplement_shared_skill')
        self.assertEqual(set(routing['project_skills']), {
            'avelna-creative', 'avelna-growth', 'avelna-research', 'avelna-orchestrator'})
        for name, entry in routing['project_skills'].items():
            with self.subTest(name=name):
                text = (ROOT/entry['path']).read_text()
                self.assertIn('name: '+name, text)
                self.assertIn('project', text.lower())
                for shared in entry['shared_skills']:
                    self.assertIn(shared, text)
        self.assertEqual(list((ROOT/'skills').glob('higgsfield-*')), [])

    def test_active_handoff_code_has_no_remote_client_or_mcp_placeholder(self):
        for name in ['asset_registry.py', 'asset_handoff.py']:
            source = (ROOT/'scripts'/name).read_text()
            tree = ast.parse(source)
            imports = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imports.update(n.name.split('.')[0] for n in node.names)
                elif isinstance(node, ast.ImportFrom):
                    imports.add((node.module or '').split('.')[0])
            self.assertFalse(imports & {'socket', 'subprocess', 'urllib', 'requests', 'httpx', 'mcp'})
            self.assertNotIn('<<<{', source)
            self.assertNotIn('reference_element_id', source)

    def test_central_contract_and_unapproved_example(self):
        contract = json.loads((ROOT/'config/asset-contract.json').read_text())
        example = json.loads((ROOT/'config/asset-manifest.example.json').read_text())
        self.assertEqual(contract['schema_version'], example['schema_version'])
        self.assertEqual(contract['higgsfield_transport'], 'cli')
        for key in ['mcp_fallback', 'direct_api_fallback', 'browser_generation_fallback']:
            self.assertIs(contract[key], False)
        self.assertIsNone(example['product_sku'])
        self.assertNotEqual(example['assets'][0]['status'], 'owner_approved')
        self.assertFalse(example['assets'][0]['rights_status'] == 'cleared')

    def test_readme_links_are_existing_project_documents(self):
        for path in [ROOT/'README.md', ROOT/'docs/creative.md', ROOT/'docs/higgsfield.md']:
            self.assertTrue(path.is_file(), str(path))
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                target = target.split('#')[0]
                if target and '://' not in target and not target.startswith('mailto:'):
                    self.assertTrue((path.parent/target).exists(), str(path.parent/target))


if __name__ == '__main__':
    unittest.main()
