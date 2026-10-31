# AVELNA / Bath Stone 01 — Product Truth Master v0.1

**STATUS:** Internal visual calibration, **not** commercial product lock or seller photo license.  
**Date:** 2026-10-31 · **Owner:** AVELNA founders · **Creative producer:** ChatGPT with founder approval.

## The core rule

**The physical product is the source of truth, not the generative output.** We previously rendered three isolated wavy mats in `assets/concepts/`, but their curves run across the entire object while the user-provided supplier image has an asymmetric set of arcs starting in the **upper-left and descending to the lower-left**. These old concepts are **superseded for product-identity work**. Do not place them in ads, a shop listing, a Reference Element or product dimension diagram.

Supplier listing associated with reference: [Longyan Yongye VDSTM-007](https://www.alibaba.com/product-detail/Fast-Drying-Hard-Bath-Mat-Super_1601587124238.html). The user supplied a visual reference attributed to this listing. This link and image are visually compatible, but **exact factory linkage and commercial reuse rights are still not verified**.

### Facts from product page vs unknowns

| Attribute | Current evidence | State |
| --- | --- | --- |
| Supplier | Longyan Yongye trade co., LTD | Alibaba listing |
| Listing model | VDSTM-007 | Alibaba listing |
| Shape | Rounded rectangle, white grooved upper surface | Product photo (visual) |
| Declared footprint | 600 × 390 mm | Supplier listing |
| Original color | White, exact color calibration unknown | Supplier listing |
| Wave arrangement | Unequal spacing, upper-left sweeping wave; right side mostly smooth | User-provided supplier-image reference |
| Thickness | **unknown** for the confirmed VDSTM-007 item | Do not copy 9 mm from a different item |
| Net weight | **unknown**; Alibaba 8 kg is **gross package weight** | Do not portray as mat weight |
| Anti-slip underside | **unknown** | No generated black base texture accepted |
| Material composition, safety, performance | **unverified** | Requires exact-SKU documents and physical assessment |
| Quantity 1 | Price tier exists but page also states MOQ 100 | Checkout not confirmed |

Do **not** put a `9 mm` height arrow, black rubber backing, guaranteed slip-proof claim or fake certification on a gallery image.

## What has been created in this conversation (private internal kit)

The user-supplied source image is **800 × 800 px**. A contour-based extraction identified the actual product perimeter at approximately `x=25–773, y=173–646`. The extracted product pixels are unchanged in RGB; only the outside background is masked. Current local outputs are available in the ChatGPT artifact bundle, **not** committed to the public repository because commercial publication rights on the supplier image have not been confirmed.

Local kit, each separately SHA-256 verifiable:
- `00_internal-source-photograph.png` — untouched source reference for QA.
- `01_exact-source-pixel-cutout.png` — exact product pixels with a transparent mask.
- `02_locked-top-reference-transparent.png` — resampled source-pixel cutout, no generative redraw.
- `03_editorial-top-reference.png` — AVELNA layout using the exact masked source.
- `04_verified-dimensions-reference.png` — premium technical sheet, supplier-declared 600 × 390 mm, thickness **unknown**.
- `05_surface-groove-truth-board.png` — original crop evidence of the groove paths, corners and texture.
- `manifest.json` — hashes, status, dimensions and unknown fields.

The asset master is **source-locked 2D**, not a photo-calibrated 3D model. Grooves were not regenerated. This does **not** license redistributing supplier photographs to a public website.

## One canonical pipeline

1. **PRODUCT_LOCK:** Verify supplier/model against actual listing, checkout, sample and rights. If model/design changes, create a fresh version; never overwrite the old SKU or hash.
2. **SOURCE_CAPTURE:** Save original in private storage, sha256, source URL, timestamp, photography license, dimensions and known colour profile. Obtain real top, underside, profile, 3/4 left/right and groove macros when sample arrives.
3. **PIXEL MASTER:** Crop and background-mask only the verified top view. Preserve its original pixels and contour. Record crop coordinates and alpha generation parameters.
4. **TECHNICAL GALLERY:** Generate dimension callouts **deterministically**, not as AI-generated text. Add 600 mm and 390 mm based on this listing. Side height remains blank until actually measured. Do not draw an unverified underside.
5. **NEW ANGLES:** Until source-backed 3D capture is complete, any AI 3/4/low-angle is `concept_only`. After a physical sample, create a calibrated 3D mesh or controlled multi-view reconstruction from real photographs; retain approved source geometry and reject modifications.
6. **LIFESTYLE:** AI may generate a **bathroom background**, not the product itself. Composite the exact product layer with realistic scale/perspective and explicit shadow. If projection requires a surface that cannot be derived from existing images, it must be marked illustrative pending validation.
7. **OWNER REVIEW:** Founder approves a specific output hash. Never infer approval from a previous colourway, prompt or image.
8. **HERMES HANDOFF:** Hermes executes only pre-approved image, prompt and asset IDs via installed Higgsfield CLI skills. No autonomous prompt/image invention, no unapproved model re-render. A new failed geometry is a rejection and asks ChatGPT/founder for a correction.

## Reproducible technical render

Use [`creative-tools/render_truth.py`](../creative-tools/render_truth.py) with the **private original**. It checks the input file hash before rendering, segments a plain-background photo, preserves the exact source pixels in the mask, and creates an AVELNA dimensions sheet with fixed fonts and deterministic annotations.

Dependencies: [`creative-tools/requirements.txt`](../creative-tools/requirements.txt), Python 3.11+, OpenCV headless, NumPy, Pillow. This command uses real user-owned source locally, not GitHub. It does not generate images or spend Higgsfield credits:

~~~bash
python3 -m pip install -r creative-tools/requirements.txt
python3 creative-tools/render_truth.py \
  --source /PRIVATE/PATH/avelna_product_truth_v01/00_internal-source-photograph.png \
  --manifest config/product-truth-vdstm007.json \
  --out /PRIVATE/PATH/avelna-vdstm007-output
~~~

The expected source hash is for the normalized `00_internal-source-photograph.png` **included in the private ZIP**. The same visible image exported again as another PNG may have a different file hash; do not bypass this validation silently. The expected source hash in the manifest protects against switching to another Alibaba image. A hash mismatch blocks output. `creative-tools` is a separate optional toolkit and intentionally **not** part of the standard-library-only deployment service. A separate `visual-provenance` CI job validates masking and gallery rendering against synthetic data. The owner should treat the first run on the target host as untested until a matching real source is available.

## Future professional six-image gallery

| Slot | Asset | Allowed before physical sample? |
| --- | --- | --- |
| 01 | Clean source-locked top packshot / cropped product | Internal review, after rights confirmation commercial |
| 02 | 600 × 390 mm architectural dimension sheet | Internal review, commercial after rights approval |
| 03 | Real wave/corner/texture micro-details | Internal review, commercial after rights approval |
| 04 | 3/4 studio photo | **No accurate new angle from one top photo** |
| 05 | Measured side depth and true anti-slip backing | **No — measure and photograph sample** |
| 06 | AVELNA Dutch bathroom lifestyle shot with locked product | Draft after legitimate reference; public only after geometry/rights review |

## Video reference provided by founder

[How to Use Higgsfield AI Better than 99% of People](https://www.youtube.com/watch?v=dJSJMt4ESEU) — public video title/metadata verified. Full narration/transcript **was not accessible in this session**, so do not claim its detailed method was watched or audited. The metadata references Elements, Angles 2.0 and consistency features, but that is not proof these functions guarantee an exact physical product. Validate actual multi-angle capabilities in the user's CLI install and compare to real sample.

## Commercial go/no-go

A visual is `internal_truth_reference` until `supplier_sku_verified && sample_reviewed && image_rights_cleared && product_geometry_signed_off`. AI-only generated art cannot satisfy those conditions. Source pixels remain private until commercial reuse approval.
