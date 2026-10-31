"""Prepare an AVELNA handoff locally; no provider client, shell or networking."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import struct
import tempfile
import zlib

from scripts.asset_registry import AssetBlocked, checked_file, resolve_assets

ROOT = Path(__file__).resolve().parents[1]


def read_object(path):
    """Bound JSON input and avoid echoing sensitive values in exceptions."""
    try:
        with Path(path).open('rb') as source:
            raw = source.read(1_000_001)
        if len(raw) > 1_000_000:
            raise AssetBlocked('json_too_large')
        value = json.loads(raw)
        if not isinstance(value, dict):
            raise AssetBlocked('json_object_required')
        return value
    except (OSError, ValueError, UnicodeError):
        raise AssetBlocked('json_unavailable_or_invalid') from None


def shared_dependencies(repo_root, skill_root):
    """Check project-local routers and existing shared skill files without copying."""
    routing = read_object(repo_root/'config/skill-routing.json')
    if routing.get('scope') != 'project_only':
        raise AssetBlocked('project_only_routing_required')
    required = set()
    for entry in routing['project_skills'].values():
        project_path = (repo_root/entry['path']).resolve(strict=True)
        if not project_path.is_relative_to(repo_root/'skills'):
            raise AssetBlocked('project_skill_outside_repo')
        required.update(entry['shared_skills'])
    base = Path(skill_root)
    for name in sorted(required):
        if not isinstance(name, str) or not re.fullmatch(r'higgsfield-[a-z0-9-]+', name):
            raise AssetBlocked('invalid_shared_skill_name')
        candidates = [base/name/'SKILL.md', *base.glob('*/'+name+'/SKILL.md')]
        if not any(p.is_file() for p in candidates):
            raise AssetBlocked('shared_skill_missing')
    return sorted(required)


def prepare_handoff(manifest, repo_root, asset_root, *, skill_root):
    """Return local media bindings and prompt bytes, never an executable command.

    This validates local declarations, not an independent operator signature,
    product safety, model compatibility, account auth or live provider upload.
    """
    root = Path(repo_root).resolve(strict=True)
    if (not isinstance(manifest, dict) or manifest.get('schema_version') != 2 or
            manifest.get('transport', 'cli') != 'cli'):
        raise AssetBlocked('cli_manifest_v2_required')
    contract = read_object(root/'config/asset-contract.json')
    if (contract.get('schema_version') != 2 or contract.get('higgsfield_transport') != 'cli' or
            any(contract.get(key) is not False for key in
                ['mcp_fallback', 'direct_api_fallback', 'browser_generation_fallback'])):
        raise AssetBlocked('cli_only_contract_required')
    purpose = manifest.get('purpose')
    sku = manifest.get('product_sku')
    if not isinstance(sku, str) or not sku.strip():
        raise AssetBlocked('exact_sku_required')
    if purpose == 'production_preparation' and sku.startswith('SYNTHETIC_'):
        raise AssetBlocked('synthetic_product_not_production')
    prompt = manifest.get('prompt')
    if not isinstance(prompt, dict):
        raise AssetBlocked('prompt_contract_required')
    rel = prompt.get('path')
    if not isinstance(rel, str) or Path(rel).parent != Path('prompts') or Path(rel).suffix != '.md':
        raise AssetBlocked('canonical_prompt_required')
    prompt_path, raw = checked_file(root, rel, prompt.get('sha256'), limit=100_000)
    if not prompt_path.is_relative_to(root/'prompts'):
        raise AssetBlocked('canonical_prompt_required')
    try:
        text = raw.decode('utf-8')
    except UnicodeError:
        raise AssetBlocked('utf8_prompt_required') from None
    if '<<<' in text or re.search(r'@AVELNA_|\{[A-Za-z_][A-Za-z0-9_]*\}', text):
        raise AssetBlocked('unresolved_prompt_binding')
    dependencies = shared_dependencies(root, skill_root)
    bindings = resolve_assets(manifest.get('assets'), asset_root, contract, purpose=purpose)
    return {
        'schema_version': 2, 'transport': 'cli', 'purpose': purpose,
        'product_sku': sku,
        'manifest_sha256': hashlib.sha256(json.dumps(manifest, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest(),
        'local_handoff_verified': True,
        'prompt': {'path': rel, 'sha256': prompt['sha256'], 'text': text},
        'bindings': bindings, 'shared_skill_files_present': dependencies,
        'authorizes_spending': False, 'ready_to_execute': False,
        'remote_handoff_verified': False,
        'blockers': ['live_cli_model_schema', 'account_workspace', 'exact_quote',
                     'independent_grant', 'remote_upload_and_job_readback'],
        'note': 'Rehash immediately before authorized execution. Generic CLI flags do not prove model compatibility. Private packet; do not commit real source paths or approval data.',
    }


def demo_packet(repo_root, skill_root):
    """Real temporary PNG + real canonical prompt; synthetic declarations only."""
    def chunk(tag, payload):
        return struct.pack('!I', len(payload)) + tag + payload + struct.pack('!I', zlib.crc32(tag + payload))

    png = (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('!2I5B', 1, 1, 8, 2, 0, 0, 0)) +
           chunk(b'IDAT', zlib.compress(b'\x00\x80\x80\x80')) + chunk(b'IEND', b''))
    root = Path(repo_root)
    prompt_path = 'prompts/editorial-master.md'
    with tempfile.TemporaryDirectory(prefix='avelna-synthetic-handoff-') as folder:
        asset = Path(folder)/'synthetic-not-a-product.png'
        asset.write_bytes(png)
        manifest = {
            'schema_version': 2, 'purpose': 'synthetic_dry_run',
            'product_sku': 'SYNTHETIC_NOT_A_REAL_SKU',
            'prompt': {'path': prompt_path, 'sha256': hashlib.sha256((root/prompt_path).read_bytes()).hexdigest()},
            'assets': [{'alias': '@AVELNA_Synthetic_01', 'path': asset.name,
                        'source_hash_sha256': hashlib.sha256(png).hexdigest(),
                        'role': 'product_reference', 'status': 'owner_approved',
                        'rights_status': 'cleared', 'product_verified': True,
                        'approved_by': 'synthetic-test-fixture-not-an-owner-approval',
                        'approved_at': '2026-10-31T12:00:00Z', 'synthetic': True}],
        }
        packet = prepare_handoff(manifest, root, Path(folder), skill_root=skill_root)
        # Public demo summary deliberately omits temporary absolute paths and full prompt.
        return {
            'synthetic': True, 'transport': 'cli', 'local_handoff_verified': True,
            'prompt_path': packet['prompt']['path'], 'prompt_sha256': packet['prompt']['sha256'],
            'asset_sha256': packet['bindings'][0]['source_hash_sha256'],
            'binding_role': packet['bindings'][0]['role'], 'cli_flag': packet['bindings'][0]['cli_flag'],
            'shared_skill_files_present': packet['shared_skill_files_present'],
            'provider_calls': 0, 'credits_spent': 0, 'authorizes_spending': False,
            'ready_to_execute': False, 'remote_handoff_verified': False,
            'temporary_sources_removed_after_demo': True, 'blockers': packet['blockers'],
        }


def private_output(path, repo_root):
    """Never overwrite repository source or publish a private runtime packet."""
    target, root = Path(path).resolve(), Path(repo_root).resolve()
    if target.is_relative_to(root):
        relative = target.relative_to(root)
        if not relative.parts or relative.parts[0] not in {'private', 'runtime', 'state', 'outputs'}:
            raise AssetBlocked('output_must_be_private')
    return target


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--demo', action='store_true')
    group.add_argument('--manifest', type=Path)
    parser.add_argument('--asset-root', type=Path)
    parser.add_argument('--skill-root', type=Path, default=Path(os.environ.get('HERMES_HOME', Path.home()/'.hermes'))/'skills')
    parser.add_argument('--output', type=Path)
    options = parser.parse_args(argv)
    try:
        target = private_output(options.output, ROOT) if options.output else None
        if options.demo:
            report = demo_packet(ROOT, options.skill_root)
        else:
            if options.asset_root is None:
                raise AssetBlocked('asset_root_required')
            report = prepare_handoff(read_object(options.manifest), ROOT, options.asset_root, skill_root=options.skill_root)
        result = json.dumps(report, indent=2, ensure_ascii=False)
        if target:
            target.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
            # New private files are created owner-only; never truncate an existing file.
            with open(target, 'x', encoding='utf-8', opener=lambda p, flags: os.open(p, flags, 0o600)) as stream:
                stream.write(result + '\n')
        if target:
            print(json.dumps({'packet_written': True, 'local_handoff_verified': True,
                              'authorizes_spending': False}))
        else:
            print(result)
        return 0
    except AssetBlocked as exc:
        print(json.dumps({'local_handoff_verified': False, 'authorizes_spending': False, 'error': str(exc)}))
        return 2
    except (OSError, KeyError, TypeError, ValueError):
        print(json.dumps({'local_handoff_verified': False, 'authorizes_spending': False, 'error': 'handoff_input_or_io_error'}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
