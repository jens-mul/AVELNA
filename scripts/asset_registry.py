"""Resolve approved AVELNA aliases to Higgsfield Element placeholders without networking."""
from __future__ import annotations

import re
import uuid
from typing import Any

ALIAS = re.compile(r"(?<![A-Za-z0-9_])@AVELNA_[A-Za-z0-9_]{2,48}\b")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
DISALLOWED_PLACEHOLDER = re.compile(r"<<<[^<>]*>>>")
VALID_STATES = {"owner_approved", "verified_upload", "element_completed", "production_enabled"}


class AssetBlocked(ValueError):
    """Unsafe or unverified asset; never spend credits on this candidate."""


def resolve_aliases(
    prompt: str,
    registry: dict[str, dict[str, Any]],
    *,
    model_id: str,
    observed_supported_models: set[str],
) -> str:
    """Create exact MCP <<<UUID>>> references from protected, verified metadata.

    Caller must supply supported model IDs from live tool discovery, not a guessed list.
    Registry is considered trusted only if stored with independent ACLs.
    """
    if not isinstance(prompt, str) or not prompt or len(prompt) > 10000:
        raise AssetBlocked("invalid_prompt")
    if DISALLOWED_PLACEHOLDER.search(prompt):
        raise AssetBlocked("unresolved_reference_placeholder")
    if not isinstance(model_id, str) or model_id not in observed_supported_models:
        raise AssetBlocked("unsupported_model")
    aliases = set(ALIAS.findall(prompt))
    if not aliases:
        return prompt
    if not isinstance(registry, dict):
        raise AssetBlocked("registry_missing")
    replacements = {}
    for alias in aliases:
        meta = registry.get(alias)
        if not isinstance(meta, dict):
            raise AssetBlocked("unknown_alias")
        if meta.get("alias") != alias or meta.get("status") != "production_enabled":
            raise AssetBlocked("asset_not_production_enabled")
        if meta.get("rights_status") != "cleared" or meta.get("product_verified") is not True:
            raise AssetBlocked("rights_or_product_unverified")
        if meta.get("approved_for_paid_ads") is not True:
            raise AssetBlocked("not_approved_for_ads")
        if not isinstance(meta.get("approved_by"), str) or not meta["approved_by"]:
            raise AssetBlocked("missing_owner_approval")
        if not isinstance(meta.get("approved_at"), str) or not meta["approved_at"]:
            raise AssetBlocked("missing_approval_timestamp")
        if not isinstance(meta.get("source_hash_sha256"), str) or not SHA256.fullmatch(meta["source_hash_sha256"]):
            raise AssetBlocked("invalid_asset_hash")
        if meta.get("element_status") != "completed":
            raise AssetBlocked("element_not_completed")
        if model_id not in meta.get("usable_models", []):
            raise AssetBlocked("asset_model_mismatch")
        try:
            element_id = str(uuid.UUID(meta["reference_element_id"]))
        except (TypeError, ValueError, AttributeError, KeyError):
            raise AssetBlocked("invalid_element_uuid") from None
        replacements[alias] = f"<<<{element_id}>>>"
    return ALIAS.sub(lambda match: replacements[match.group(0)], prompt)


def safe_alias_manifest(record: dict[str, Any]) -> dict[str, Any]:
    """Public audit view omits provider/workspace/upload UUIDs and approval identity."""
    return {
        "alias": record.get("alias"),
        "status": record.get("status"),
        "product_verified": record.get("product_verified") is True,
        "rights_cleared": record.get("rights_status") == "cleared",
        "reference_ready": record.get("element_status") == "completed",
    }
