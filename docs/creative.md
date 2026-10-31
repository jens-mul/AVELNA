# AVELNA Creative Production System
**Canonical operations manual · revision 1.0 · 31 October 2026**

> **Current status:** a real private Higgsfield `AVELNA Creative Studio` project and reference Elements exist. One paid five-second camera test was completed. We **have not** produced an approved full commercial, verified the exact factory SKU, established the mat's water-performance claims, or deployed Hermes' paid executor. **No element's `completed` status by itself means the founders approved the image.**
>
> For public release always pass `PRODUCT VERIFIED + IMAGE RIGHTS + CLAIMS + HUMAN FINAL REVIEW`. This document describes *how we work*; it is not a spending authorization.

This document is the single entry point for the visual production workflow. It supersedes dated deployment/library-status statements in `docs/higgsfield.md`, `docs/hermes.md`, old issues and unapproved concept prompts. Keep source history, but don't blindly execute historical proposals.

## Core principle: Three creative entities, three independent locks

| Entity | Higgsfield category | What must stay consistent | What is actually approved |
| --- | --- | --- | --- |
| **Location / Bathroom** | `environment` | Room plan, shower opening, glass, grout scale, vanity, light, camera coordinates | Original AVELNA Dutch bathroom **environment concept**. Newer cropped/generated views are **candidates**, not signed off independently. |
| **Bath Stone / Product** | `prop` | Top silhouette, true asymmetric left-origin grooves, corners, surface; later true measured depth, base | Supplier reference and crops are only **internal calibration**. Exact factory design, rights, physical testing and full 3D not verified. |
| **StepWoman / Character** | `character` | Same adult AI character, face/hair/skin tone, wrap towel, bare feet, scale and foot anatomy | Four individually generated references uploaded and completed technically. **No definitive character-consistency signoff yet**. Old `StepWoman_01` is retired. |

**The final commercial can be visually aspirational; the product photo and performance claims must be truthful.** Do not confuse compositing/reference fidelity with proof of factory identity.

## Roles — non-negotiable

| Work | ChatGPT + owners | Higgsfield | Hermes |
| --- | --- | --- | --- |
| Concept, art direction, new prompts, image generation | **Own**; founders decide exact version | Hosts/executes explicitly chosen tasks | Does **not** brainstorm, rewrite prompts or invent reference images |
| Individual character, location and product reference selection | Founders approve each role/version | Private media uploads + `Elements` index | Reads exactly the approved manifest |
| Shotplan, camera, wet-foot realism | Authors / conducts creative QA | Video render when authorized | CLI execution of approved shot packet only |
| Paid-generation approval | Founders authorize exact request / cap | Quotes and invoices | Cannot infer approval from repository text |
| Final edit, cropping, audio, exports | Set visual rules, approve final cut | Media rendering/tools | Deterministic assembly, QA, report |
| Webshop / orders / stock | Owners | — | Integrates once permission and real API exist |

Current owner decision: **products sold individually**. Each SKU has its own product page, images, price, assets, and ad program. No mandatory bundles. The first hero is the Bath Stone; Faucet Mat is separate.

## Actual Higgsfield state (verified this session)

- Private media project `AVELNA Creative Studio`: exists.
- Project folders: `00_source_reference`, `10_candidates`, `20_approved_masters`, `30_creative_outputs`, `40_archived_versions`.
- **14 Elements observed, all technical status `completed`**: 4 Bathroom (including original), 5 Stone (including original concept), 5 StepWoman (including old retired one). See safe names/status in `config/creative-element-registry.example.json`.
- The primary bathroom upload is in `20_approved_masters` for **environment composition approval only**.
- New Bathroom, Stone and StepWoman views are in `10_candidates`. Supplier source top view is also in `00_source_reference`.
- Old StepWoman's *source* is now attached to `40_archived_versions`; its **Element remains in Elements**. The active MCP exposes no standalone delete-element action. Do not falsely claim it was deleted.
- Completed video test `The Approach V1` is in `30_creative_outputs`. Cinema Studio Video v2, 5.04s, 856×1072 actual pixels, approximate 5-credit charge observed at submission (account showed 5 fewer afterward). The attempted 3:4 request was rejected at runtime; 9:16 submission yielded a roughly 4:5 file. It is a **camera/ambience proof**, not an approved hero ad.
- **Latest observed account balance: 55 credits**. This is a snapshot, not attributable to our work or a forecast, and no extra generation was started during this documentation task.

Private media/workspace/project/Element UUIDs belong in an access-controlled runtime registry, **not** publicly in git. Re-resolve actual IDs via live tool lookup before executing; never reconstruct from name guesses. No customer data or Vaultwarden tokens in repository.

## Reading order — when to open what

1. [`01-reference-production.md`](creative-system/01-reference-production.md) — how we made separate front/back/upper/lower images, how to generate *one at a time*, and when a candidate is accepted.
2. [`02-higgsfield-elements.md`](creative-system/02-higgsfield-elements.md) — exact project/library/upload/Element handling, names, deprecation and readback.
3. [`03-shot-continuity.md`](creative-system/03-shot-continuity.md) — a single bathroom, a single mat, the same woman; shot handoff and water/foot physics.
4. [`04-production-execution-qa.md`](creative-system/04-production-execution-qa.md) — shot packet, readiness, credit gates, results, per-frame QA and final approval.
5. [`05-experiment-journal.md`](creative-system/05-experiment-journal.md) — what we actually tried, failed, learned and corrected.
6. [`06-hermes-cli-handoff.md`](creative-system/06-hermes-cli-handoff.md) — turn the founders' signed-off prompts/assets into narrow Hermes CLI execution without a second creative director.
7. [`07-onboarding-checklist.md`](creative-system/07-onboarding-checklist.md) — exact sequence for the next operator session.
8. [`research/creative-sources.md`](../research/creative-sources.md) — authoritative provider docs and date/claim caveats.

Public machine-readable **examples**, with **no private IDs**: `config/creative-element-registry.example.json` and `config/creative-shot-brief.example.json`. Exact image prompts for difficult scenes live in `prompts/shot-02-step-out-v1.md` and `prompts/shot-03-foot-contact-v1.md`. Both are draft creative instructions, not validated performance claims.

## Stage gates and what 'locked' means

| Stage | Required proof | Who can sign | Result |
| --- | --- | --- | --- |
| S0 Supplier candidate | Exact product link and observed features | Research only | `supplier_candidate` |
| S1 Source identity | Verifiable photo/source hash and permissions | Owner | `source_identity_reviewed` |
| S2 Visual master | Specific image file/hash + likeness/architecture/product geometry QA | Owner | `creative_master_approved` (role-specific) |
| S3 Higgsfield presence | Confirmed media ID, correct folder, completed Element and live role | Tool readback | `asset_registered`; **not commercial approval** |
| S4 Shot packet | Frozen prompt hash, references, model, framing, budget quote, shot goal | Owner | `shot_approved` |
| S5 Production | One accepted external job, read-back status/video file, cost evidence | Provider | `render_completed` |
| S6 Visual/physical QA | Frame-by-frame continuity, anatomy, wetness, claimed performance | Founders; real test for claims | `final_media_approved` or `rejected` |
| S7 Publication | Real SKU, rights, product compliance, stock, offer and explicit ad scope | Business owners | `commercial_release_allowed` |

In particular, founders can approve a **bathroom reference** without approving the imaginary mat inside it; can approve a **StepWoman look** without approving a water-imprint claim; and can approve an internal **proof-of-concept** without authorizing public ad spend.

## Ten-minute run summary

- Begin from the three existing reference categories; do not ask a model to reinvent them.
- Generate individual portrait/room/stone images, one standalone output per request; reject collages.
- Confirm upload, map alias and actual ID, and inspect `completed`; keep `candidate` and `approved` separate.
- Freeze one shot brief (not a full unbounded movie): exact start/end frame and movement, the same asset versions, no scene changes beyond those listed.
- Quote provider credit cost; only run on a separate approved monetary grant. On rejected/unknown submission don't retry blindly.
- Inspect actual result at start/middle/end; record drift. Repeat only after one specific correction and a fresh grant.
- Reject AI-only water-drying footage as evidence of real product behavior until the supplier SKU and physical test substantiate that claim.

**This is a production handbook, not evidence that the whole production is automated or 1:1 physically accurate.**
