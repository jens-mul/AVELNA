# 02 — Higgsfield Asset Library & Reference Elements SOP

**Scope:** private provider state and workflow; not an interface contract for every future model release. Discovered tools on 2026-10-31 and actual readbacks are authoritative. Refer to [Higgsfield Help Center](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent) and official current tool schema before automating.

## The mental model: three different objects

- **Media file:** uploaded image with a Higgsfield media UUID and a file URL. Upload does not grant usage rights or imply approved creative quality.
- **Project placement:** an entry that points to that media file in a particular project/folder. Attach does not create an Element.
- **Reference Element:** a reusable `character`, `environment` or `prop` with **its own ID**, name and status. A completed Element is a usable technical reference, **not** proof that the depicted product is right or the founder has approved that image.

**A standalone image from ChatGPT is not automatically a native Element.** The entire workflow requires confirmed media, an Element creation and a readback.

## Our real private structure

Project: **`AVELNA Creative Studio`** (created and read back).

| Folder | Meaning | Current policy |
| --- | --- | --- |
| `00_source_reference` | Original supplier/calibration photo, relevant factual references | Private; material rights may still be unverified |
| `10_candidates` | Candidate rooms, model views, photostudies and generated concepts | No live publication or performance claims |
| `20_approved_masters` | Exact founder-approved environment/product/character versions | Approval must specify **which property** is approved |
| `30_creative_outputs` | Generated videos/stills/exports by shot and revision | Job status ≠ founder approval |
| `40_archived_versions` | Retired input photos and old creative references | Folder archiving does NOT delete an Element |

Folders are actual created folders. We put the four individual StepWoman images into Candidates after verifying that their Elements were present; the old character's source was attached to the archive folder. The old Element remains visible (no standalone delete action in the current connected MCP).

## Existing Element naming convention — real, observed

A full current list (without private UUIDs) is in `config/creative-element-registry.example.json`. Do not recreate any of these names unless the specific source image or original Element is intentionally versioned.

**Environment**
- `@AVELNA_Bathroom_01` — founder-approved *environment mood/composition*; includes an unverified conceptual mat.
- `@AVELNA_Bathroom_Mid_01` — video still from camera proof; candidate.
- `@AVELNA_Bathroom_Close_01` — closer camera-proof still; candidate.
- `@AVELNA_Bathroom_Shower_01` — original-image crop; candidate.

**Product / prop**
- `@AVELNA_StoneConcept_01` — older source-based concept, **not** verified physical product.
- `@AVELNA_Stone_Top_01` — user-supplied supplier top-view photo; private internal calibration, rights unknown.
- `@AVELNA_Stone_Oblique_01` — 2D perspective of source pixels, **not** a measured 3D camera view.
- `@AVELNA_Stone_Grooves_01` — true source crop, source rights unknown.
- `@AVELNA_Stone_Corner_01` — true source crop, source rights unknown.

**Character**
- `@AVELNA_StepWoman_Front_01` — standalone front studio full-length view, candidate.
- `@AVELNA_StepWoman_Back_01` — standalone rear studio full-length view, candidate.
- `@AVELNA_StepWoman_Upper_01` — upper-body / face, candidate.
- `@AVELNA_StepWoman_Lower_01` — legs and bare feet, candidate.
- `@AVELNA_StepWoman_01` — **DEPRECATED**, obsolete montage-derived reference. Source was archived in project folder; Element itself still exists. Never choose it for new production.

**Observed:** 14 named Elements, each returned provider status `completed`. This is not a commercial approval matrix. None of the Stone entities is approved as an exact factory product.

## Upload protocol — what worked, and what must be rechecked

### A. User/chat attachment pathway

For an eligible file reference available to a ChatGPT conversation, the connected uploader accepted `media_upload_and_confirm({ file: <attachment_file_id>, type: "image" })` and returned `media_id` + URL + status. In this session the four standalone StepWoman images were uploaded individually and later read back.

**Do not generalize:** the tool's declared contract says user-provided ChatGPT attachments; image-gen output references in a given conversation may or may not be accepted. Never pass a local filesystem path to this tool or assume a blob exists because it has a URL in chat.

### B. Higgsfield sandbox creation/transformation

For standalone files created in the Higgsfield cloud sandbox (cropped room frames, source-pixel Stone crops), use the actual documented pipeline:

1. Call `media_upload` for exact filename/MIME and correct workspace; get presigned URL + media UUID.
2. In **the same sandbox producing command**, render the image and PUT actual file bytes via provider's presigned URL. Confirm HTTP 200; handle errors without leaking signed URL in GitHub/logs.
3. Call `media_confirm` with that media ID and `type:"image"`.
4. Attach the confirmed media as `type:"media_input"` to the right project folder using `attach_project_asset`.
5. Call `list_project_assets` for that specific project/folder and match **source UUID + placement**; do not claim success merely from an accepted upload POST.
6. Only after a confirmed source create `create_reference_element` in the intended category. Then read `show_reference_elements` and check source ID, name, category and status `completed`.
7. Save IDs, source SHA, source rights, consent, timestamp, image pixel size and approval *in a private runtime manifest*; GitHub receives only aliases and sanitized state.

These steps were exercised for Bathroom and Stone derived stills with real returned asset and placement IDs. **No paid generation was involved in the upload process.**

### C. Existing media / previous generation

Reuse the exact existing confirmed media or completed job ID. Don't reupload to create multiple nearly identical versions. If a particular video frame was extracted from a previous generation, include source job and timestamp and identify it as a **generated-derived** frame.

## How an Element is used

### Inside ChatGPT/MCP

The connected Higgsfield tool contract requires `<<<ELEMENT_UUID>>>` **inside the prompt**, *not* the literal `@name`. The server then injects the reference images and rewrites to the named tag. The Element ID does **not** go into ordinary `medias[]`. Fetch real UUID from live `show_reference_elements`; never guess or copy the wrong one.

Explicitly supported models in the tool description **at the time of discovery**:
- Image: Nano Banana Pro / 2, GPT Image 2, Seedream 4.5 / 5 lite, Cinema Studio Image 2.5.
- Video: Cinema Studio Video 2 and 3.0, Seedance 2.0, Kling 3.0 (Kling also requires a genuine `start_image`; an Element alone is not a valid start frame).

Models change. Re-read live accepted roles and media constraints before a job. A visible `@name` in text without a valid Element binding does **not** establish reference fidelity.

### Inside Hermes/CLI (the chosen route)

Higgsfield officially supports Hermes using the **CLI + upstream Higgsfield skills**. CLI syntax/capabilities must be discovered from the installed version and those personal skills. **Do not translate MCP `<<<UUID>>>` syntax blindly into CLI flags or invent commands.** The verified private manifest should map names → current IDs and role classes; Hermes resolves identities through the installed CLI or stops when that capability cannot be established. See `06-hermes-cli-handoff.md`.

### Anti-duplication / names / versioning

- Identity is the **source image SHA + role + version**, not the short filename.
- New visual identity → `_02` or explicit named revision, never overwrite an existing master and silently update its source.
- A crop of a source is a *derived angle*, not a newly photographed architectural view.
- A new Character view created in a separate run is a *candidate match* until visually compared with the canonical front.
- Alias prefix `@AVELNA_` distinguishes brand-owned concepts from supplier item codes.
- Avoid vague aliases `@Product`/`@Bathroom` and positional search like “last item”.

## Retiring and deleting

- The **old** `@AVELNA_StepWoman_01` is deprecated, and the source asset is placed under `40_archived_versions` for retrieval.
- The connected Higgsfield tool catalog surfaced **no** action to delete a standalone Reference Element. `remove_project_asset` deletes only a project placement; it does **not** erase an underlying element/upload. `delete_project` would be catastrophically broad and must never be used as a workaround.
- If the Higgsfield website exposes Element deletion, the operator may remove just that one obsolete element manually and then read `show_reference_elements` to verify absence. Until confirmed: status = `deprecated_but_exists`.
- Do not claim a source/photo has been physically purged from provider backups.

## Private manifest recommendation

Higgsfield IDs and account scope are treated as private runtime metadata. An operator/agent can construct an actual JSON registry from verified provider results with keys:

~~~json
{
  "schema_version": 1,
  "last_verified_at": "2026-10-31T17:25:00Z",
  "workspace_id": "<PRIVATE_REAL_UUID>",
  "project_id": "<PRIVATE_REAL_UUID>",
  "elements": [
    {
      "alias": "@AVELNA_Bathroom_01",
      "element_id": "<PRIVATE_REAL_UUID>",
      "media_id": "<PRIVATE_REAL_UUID>",
      "category": "environment",
      "provider_status": "completed",
      "creative_scope": "environment_style_only",
      "owner_approved": true,
      "rights_status": "AI_concept"
    }
  ]
}
~~~

Use actual provider IDs only in the private copy; placeholder IDs in public docs are **not executable**. A private registry should be uploaded to a restricted provider folder or secure local runtime, never committed to the public repository. No access tokens or presigned URL strings should be included even privately unless necessary.

## Folder/status audit after every session

For each item:
- Is the source actually present? (media ID / SHA)
- Does one project placement exist in the correct folder?
- Does the Element exist with correct role and source, status completed?
- Is it **concept**, **owner-approved creative**, **product-verified** or **commercially cleared**?
- Is it the currently selected version, or deprecated?
- Is it in the correct intended shot and model context?
- Was any paid generation started? Exact job ID and pre/post credit balance?

**Technical library success never substitutes for visual, legal, physical or commercial approval.**
