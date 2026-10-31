"""Local asset integrity checks. No provider networking or generation syntax."""
from datetime import datetime
import hashlib
from pathlib import Path
import re

ALIAS = re.compile(r'@AVELNA_[A-Za-z0-9_]{2,48}\Z')
SHA256 = re.compile(r'[0-9a-f]{64}\Z')


class AssetBlocked(ValueError):
    """Fail closed without echoing private input into public diagnostics."""


def checked_file(root, relative, expected_hash, *, limit):
    """Resolve a bounded file below an explicit root and verify its actual bytes."""
    if (not isinstance(relative, str) or not relative or
            Path(relative).is_absolute() or '..' in Path(relative).parts or '://' in relative):
        raise AssetBlocked('invalid_relative_path')
    if not isinstance(expected_hash, str) or not SHA256.fullmatch(expected_hash):
        raise AssetBlocked('invalid_content_hash')
    try:
        base = Path(root).resolve(strict=True)
        path = (base/relative).resolve(strict=True)
        if not path.is_relative_to(base) or not path.is_file():
            raise AssetBlocked('file_outside_root_or_not_regular')
        with path.open('rb') as source:
            data = source.read(limit + 1)
        if not data or len(data) > limit:
            raise AssetBlocked('file_empty_or_too_large')
        if hashlib.sha256(data).hexdigest() != expected_hash:
            raise AssetBlocked('content_hash_changed')
        return path, data
    except (OSError, RuntimeError):
        raise AssetBlocked('source_unavailable') from None


def resolve_assets(records, asset_root, contract, *, purpose):
    """Validate metadata and return CLI media bindings; does not authorize spending.

    Caller-owned declarations are not independently verified grants or proof of
    real product safety. Rehash immediately before any separately authorized use.
    """
    if purpose not in {'synthetic_dry_run', 'production_preparation'}:
        raise AssetBlocked('unknown_handoff_purpose')
    if not isinstance(records, list) or not 1 <= len(records) <= 16:
        raise AssetBlocked('nonempty_bounded_assets_required')
    if not isinstance(contract, dict) or not isinstance(contract.get('roles'), dict):
        raise AssetBlocked('asset_contract_required')
    limit = contract.get('max_asset_bytes')
    if type(limit) is not int or not 1 <= limit <= 100_000_000:
        raise AssetBlocked('invalid_asset_size_limit')
    output, aliases = [], set()
    for record in records:
        if not isinstance(record, dict):
            raise AssetBlocked('asset_object_required')
        alias = record.get('alias')
        if not isinstance(alias, str) or not ALIAS.fullmatch(alias) or alias in aliases:
            raise AssetBlocked('unknown_or_duplicate_alias')
        aliases.add(alias)
        if record.get('status') != 'owner_approved' or record.get('rights_status') != 'cleared':
            raise AssetBlocked('approval_or_rights_missing')
        if record.get('product_verified') is not True:
            raise AssetBlocked('product_unverified')
        if not isinstance(record.get('approved_by'), str) or not record['approved_by'].strip():
            raise AssetBlocked('approval_identity_missing')
        try:
            timestamp = datetime.fromisoformat(record['approved_at'].replace('Z', '+00:00'))
            if timestamp.tzinfo is None or timestamp.utcoffset() is None:
                raise ValueError()
        except (KeyError, AttributeError, TypeError, ValueError):
            raise AssetBlocked('aware_approval_time_required') from None
        if type(record.get('synthetic')) is not bool or record['synthetic'] != (purpose == 'synthetic_dry_run'):
            raise AssetBlocked('synthetic_production_boundary')
        role = record.get('role')
        if not isinstance(role, str) or role not in contract['roles']:
            raise AssetBlocked('unsupported_reference_role')
        flag = contract['roles'][role]
        if flag not in {'--image-references', '--start-image', '--end-image'}:
            raise AssetBlocked('unsupported_cli_media_flag')
        path, _ = checked_file(asset_root, record.get('path'), record.get('source_hash_sha256'), limit=limit)
        if path.suffix.lower() not in contract.get('allowed_extensions', []):
            raise AssetBlocked('unsupported_file_extension')
        output.append({'alias': alias, 'path': str(path), 'role': role, 'cli_flag': flag,
                       'source_hash_sha256': record['source_hash_sha256']})
    return output
