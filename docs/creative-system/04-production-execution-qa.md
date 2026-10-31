# 04 — Shot execution, credit gating, visual QA and delivery

## Starting point

Higgsfield reference Elements and folders already exist. The attached media is **not** a commercial product lock. No work starts just because this documentation is in git.

A production task should be scoped to **ONE** of:
- independent still generation/edit for one specific named reference view;
- one named shot render;
- deterministic cut/crop/graphic/audio export from approved assets;
- read-only research/review.

A request to "build the whole ad automatically" is decomposed into a set of approved, cost-estimated jobs. **No unlimited recursive attempt loop.**

## Required creative shot packet

The machine-readable example is `config/creative-shot-brief.example.json`.

| Section | Required input |
| --- | --- |
| Identity | `campaign_id`, `sku_code`, `shot_id`, `brief_version`, scene purpose |
| Evidence | true supplier/source rights and factory identity state |
| Environment | `@AVELNA_Bathroom_01` plus optional candidate angle, owner approval scope |
| Product | `@AVELNA_Stone_Top_01` etc.; source-truth status, footage classification |
| Character | explicit approved StepWoman front/back/upper/lower refs; **old element excluded** |
| Camera | start and end frame, lens/camera axis, move direction/distance, duration |
| Action | what changes, which foot, spatial path, time and water contact |
| Fixed world | room geometry, dry floor, mat placement, grooves, subject identity |
| Output | aspect, resolution, frame rate, codec, audio on/off, safe area |
| Provenance | exact prompt and SHA; requested model/settings and provider price quote |
| Spending | valid operator grant with provider/account, max credits and expiry (in protected executor only) |
| Delivery | expected folder, filename, QA rubric, human signoff, publication status |

**Anti-Hermes surprise rule:** if any canonical prompt, reference, exact price cap or required image is missing, return a structured `BLOCKED` response. Hermes may not fabricate the missing creative specification.

## Model and provider selection (snapshot, not guarantee)

For the first five-second camera-only trial, the model comparison on the then-linked account reported:
- Cinema Studio Video v2: 5 credits, supports a stable single-shot setup.
- Seedance 2.0 Mini: 5 credits for an equivalent budget-oriented 5s draft.
- Grok 1.5 Lite: 5 credits for the comparable draft.
- Kling v3 standard: 7.5 credits.
- Some advanced 3.5/4.0/2.5 modes were 25–35 credits (unaffordable at that earlier 10-credit balance).

**The actual accepted render:** `cinematic_studio_video_v2`, `std`, sound `off`, speed ramp `linear`, `multi_shots:false`, `cfg_scale:0.5`. Five-second camera-only result **completed**; quote 5 credits; real output 856×1072, 5.042 seconds. Requested 3:4 was rejected even though model description listed it. Reran cost quote for 9:16 before the only successful submission; returned clip cropped differently. Do not claim "true 9:16 output" solely from requested parameter.

Model support, prices and quotas change. Every new paid job must use actual latest provider preflight, not these historical figures. Available credits were 55 in most recent readback, but **not a grant**.

## Cost discipline and submission idempotency

1. Read provider balance/credits; independently check account subscription and model roles.
2. Identify exact confirmed uploaded assets/Elements. Validate supported model; some ignore Elements entirely.
3. Build complete params in memory (model, prompt, start/end refs, aspect, duration, mode, sound, destination folder).
4. Call a read-only price/preflight path when provided (some quote calls can import URLs; prefer already uploaded media IDs to avoid duplicate uploads).
5. Check price fits the **separately approved maximum** and scope of the launch plan. This repo cannot authorize €200 spend.
6. Only then submit one generation job. Record returned job ID, submission time and receipt.
7. On a transport timeout or uncertain result, **do not submit another job**. Look up the prior job or reconcile billing before retry.
8. Poll to terminal status. On `failed`, record cost/possible refund and **stop**; never automatically increment count or switch to a more expensive model.
9. Read the real result and provider balance after; reconcile expected vs actual debits.
10. QA each frame and store exact result version; do not automatically promote to approved master.

No paid Higgsfield call was made by creating or organizing the reference Elements. A new video test requires its own authorization.

## Shot quality checklist — 100-point human + deterministic review

| Category | Weight | Pass tests | Hard reject |
| --- | ---: | --- | --- |
| **World continuity** | 20 | same layout, tile grout scale, vanity, shower and light | vanity/grout/glass morph or room relocation |
| **Product geometry** | 25 | consistent footprint, corners, groove path and source orientation | invented repeated waves, stretched/relocated mat, random underside |
| **Character continuity** | 15 | same adult AI woman/hair/towel proportions, plausible motion | face identity change, extra/missing limb, wrong toes |
| **Physical water/contact** | 20 | water only from plausible source, dry surrounding floor, anatomically plausible footprint | flooded floor, stains before contact, impossible droplets |
| **Editorial quality** | 10 | controlled exposure, gentle camera, no compression/flicker | camera whip, severe flicker, cartoon splash |
| **Export integrity** | 10 | correct duration/codec, safe framing, no unwanted text | black frames, unusable crop, copyrighted music |

**Hard reject overrides score.** A 95/100 clip that depicts a non-existent product or made-up water effect as real is **not** suitable for live product advertising. A frame-by-frame review should include timestamps, failures and annotated stills (private where source rights are uncertain).

### Minimum frame audit

For a 5s clip: 0.0s, 1.0s, 2.0s, 3.0s, 4.0s, last frame; for human/water shots also contact/lift boundaries. Compare each frame to the approved world state:
- Mat crop alignment and grout crossing; corner deformation.
- Water coverage map on mat and dry tile mask outside.
- Contact frame foot/toe count and shadow.
- Skin wetness continuity and hair/towel identity.
- Room color grading and highlight clipping.
- Camera jerk and object flicker.

Archive a small contact-sheet **for QA only**; do not mistakenly replace the individual production stills with a multi-panel montage.

## Distinct output classifications

| Value | Meaning | Permitted use |
| --- | --- | --- |
| `creative_candidate` | AI-generated reference, may drift | internal iteration |
| `environment_approved` | founder-approved architecture and styling | mood/scene base, not product proof |
| `product_candidate` | source-truth photo or model, identity/rights not verified | internal calibration |
| `reference_element_completed` | technical Higgsfield status only | may be used in internal concept generation with permission |
| `shot_approved` | exact shot creative and params accepted | one authorized production job, **not** publication |
| `render_completed` | provider job done, unreviewed | manual QA only |
| `final_media_approved` | quality + product/rights/claims passed | staged use as permitted |
| `commercial_release_allowed` | business legal/offer/tracking/stock/ad approvals completed | published product material/advertising |
| `deprecated_but_exists` | historical Element still in provider | never select, may need manual cleanup |

Keep the classification attached to each asset, not a global truth flag inherited by everything in one folder.

## Final video assembly (once multiple approved clips exist)

- Choose clean, matched shots; no arbitrary high-energy transitions. Cut on foot motion or eye-line, use short 3–6 second fragments.
- Apply a single room color grade with white towel/ivory product control swatches. Correct creative AI exposure, don't shift the true product color.
- Deliver desktop video as a layout designed for horizontal crop (the current vertical source does NOT become a real wide shot by resizing), mobile variant separately.
- Export H.264/yuv420p MP4 at actual output dimensions, mute autoplay, include a poster frame, optional subtitles/captions if copy requires it.
- Verify audio/music licenses and ability to run in paid ads. Branding, words and pricing are separate deterministic overlays rather than model-generated glyphs.
- Keep one canonical final timeline file or edit decision list referencing exact job IDs (privately). Renders of a final clip alone are not editable source footage.
- Performance claim about drying time/absorption must be backed by SKU-specific evidence and shown as an honest demonstration, not faked.

## Web performance and conversion handoff

For each *individually sold* product:
- separate product page and media gallery;
- first frame readable without play, foreground mat and spatial context;
- autoplay muted, plays inline, WebM/MP4 variants if genuinely supported, clear loading poster;
- reduced-motion alternative and accessible textual product information;
- CDN deliverable, optimized file size and measured page performance;
- actual truthful dimensions/texture images, not an attractive imaginary mat;
- no prefilled false reviews or guarantee badges.

Conversion success can only be evaluated after paid orders, real ad spend and costs. "This video is premium" is an art-direction judgement, not a measured CAC.

## Incident response / rollback

| Incident | Immediate action | Recovery |
| --- | --- | --- |
| Wrong Element or old StepWoman | Stop the render; don't automatically retry | Resolve current alias + source hashes, regenerate only after new approval |
| 3:4 rejected by provider | No charge if no job accepted; read response | Update actual supported ratio and re-quote; never assume catalog truth |
| Job submission times out | Outcome unknown | Provider job-history/status readback; don't double spend |
| Model alters grooves or face | Reject output | New single controlled input; stronger reference / source composite / physically captured model |
| Mat becomes wet without contact | Reject as physics/claim defect | Re-stage foot contact, physically constrain wet mask |
| Footstep has missing toes | Reject | Generate new single frame, not a collage |
| Rights or SKU uncertainty | Block publication | Check supplier contract / own sample and visual proof |
| Credit balance differs from expected | Stop further generation | Reconcile provider usage, do not guess/refill cap |
| Wrong clip posted | Pause only owned ad / rollback CDN asset | Restore last approved version, report link/IDs and change log |

## Required receipt from Hermes for any later run

The agent returns:
1. source package identifier + exact prompt hash + reference names;
2. actual tool and model IDs (from discovered CLI), runtime/version;
3. confirmed provider cost quote, explicit grant scope and actual debit;
4. accepted job IDs/status/readback, exact video dimensions and duration;
5. frame QA verdict with reasons, not only "looks good";
6. output preview/storage path and whether it is a concept, approved edit or commercially cleared;
7. next creative blocker that requires the founders.

A successful provider job is **not** equivalent to a profitable ad, a verified product, or a successful physical material test.
