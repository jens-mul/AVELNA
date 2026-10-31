# 01 — Individual reference image production (ChatGPT + founders)

## Objective

Create **independent high-resolution images** of one reusable item/entity. Never create a tile/contact sheet and later cut it into 128-pixel pseudo-masters when the end goal is a sharp standalone asset. We learned that repeated model requests for multi-angle references often produced a collage even when we asked for a single shot. *If it returns a montage, that is a failed deliverable.*

**Reference identity is not a fixed prompt:** a saved image and its immutable hash are the identity. Text is only guidance to animate, light and frame that exact asset.

## Before generation: creative brief + reference manifest

Every target should include the following fields **before** a call to any generator:

| Field | Example | Constraint |
| --- | --- | --- |
| Entity | `StepWoman` / `Bathroom` / `Stone` | exactly one primary subject |
| Requested output | `StepWoman Front 01` | one file = one frame/angle, **no contact sheet** |
| Input refs | original approved image file(s), SHA and role | no guessed, stale or unrelated image |
| Fixed geometry | face/hair/body/towel; room layout; mat wave geometry | preserve identity, not only mood |
| Variable | camera angle / focal distance / pose only | changes enumerated, no arbitrary redesign |
| Camera | full-length 45–70mm studio; 35–50mm room; 85–100mm detail | approximate aesthetics, not proof of actual camera |
| Light/background | simple continuous studio background; neutral softboxes | no excessive amber glow, no dramatic fashion glare |
| Deliverable | 1 standalone image, no labels/borders/text | inspect entire image, no cropped limbs |
| Approval | exact SHA, founder's yes | no auto-approval from AI |
| Rights and claims | AI concept vs licensed product source | commercial use explicitly gated |

### Our current StepWoman V1 identity anchor

The founder supplied/approved the *direction* for a fictional adult AI woman in a white textured towel. Source variants were originally mosaics, and their cropped portraits suffered from poor sharpness. We subsequently produced **four individually generated studio photographs**: front full-body, back full-body, upper body and lower body. All are presently registered as Elements; registration does not mean identity has been optically verified across them.

**Appearance constraints:** fictional adult woman; medium-length damp dark-brown hair with warm brown highlights; mid-warm neutral skin tone; ordinary natural makeup; soft realistic skin texture, not plastic retouching; white wrap towel with consistent fold and front knot; wet lower legs with small localized beads; bare feet with five plausible toes; calm non-performative expression. Do not invent a testimonial or claim a real person's endorsement.

#### Required four-shot production order (one separate image-generation call per row)

| Image | Crop and camera | Fixed aspects | Acceptance |
| --- | --- | --- | --- |
| **Front** | Vertical 3:4 or 4:5, full body including **both heels and toes**, chest-height 45–70mm look | face, hairline, towel fold, proportions, skin hue | sharp face, two complete hands, two complete feet, level floor |
| **Back** | Vertical full body, camera height matched to Front | same wet-hair length, same towel hem/coverage, body scale | no impossible body twist, consistent hair and shoulder proportions |
| **Upper** | Head, shoulders, towel top edge; medium portrait 70–100mm look | facial landmarks, wet strands, skin and towel texture | no airbrushed face, no different hairstyle/eye color |
| **Lower** | From towel hem/upper thigh down to toes, neutral angle | same leg proportions/skin hue, textile edge, natural droplets | toes/heels correct, no fused legs, sensible balance |

#### Default standalone studio prompt template

Use the already approved front/source photo as a **real attached image reference**, rather than relying only on this text:

~~~text
Create ONE standalone photorealistic studio photograph of the same fictional
adult character as the attached identity reference. Deliver precisely one
uncollaged image; NO grid, no storyboard, no panels, no multi-view sheet,
no labels, numbers, borders, split-screen or duplicated model.

View requested: [FRONT FULL-BODY | BACK FULL-BODY | UPPER CLOSE-UP | LOWER CLOSE-UP].
Use soft diffuse studio lighting, neutral warm-grey seamless paper backdrop,
gentle floor contact shadow and realistic neutral color balance. Match the
reference person's consistent wet dark-brown hair, face identity when visible,
white terry towel, realistic adult body proportions, damp skin detail and
bare feet. Make only the necessary camera/pose changes for the requested view.
No fashion gloss filter, wet floor, extra characters or accessories.
Focus on the physical texture of skin and towel, precise fingers/toes and
correct natural perspective. Leave full relevant anatomy inside frame.
~~~

**Output rule:** even a beautiful image is rejected if it contains more than one view, differs in face/limbs/towel or crops a critical foot. Regenerate *that view only*. Do not extract a blurred tiny slice of a contact sheet and call it a new hero master.

### Identity continuity QA — compare images side-by-side

Use front and back/close-up as reference images in actual model calls whenever possible. Inspect:
1. Hair part/length, strand color and wetness; no instant dry bangs.
2. Same skin undertone and realistic shine, not uniformly wet plastic.
3. Towel material, wrap side, length and neckline. Real towel gravity: cannot remain perfectly fixed while walking without believable hold.
4. Shoulder width, body proportion, left/right leg, toes, nails and ankle silhouettes.
5. Same softbox direction and studio neutral white balance, with mild variations only.
6. No identity shifts across frames; model's ability to **associate** separate elements is not a guarantee.
7. In concept generation, no claims of a real person; fictional reference only.

**Optional future upgrade:** After the founder signs off four compatible images, assemble them as media inside a *single multi-image Character Element* **if** the current tool/account supports it and an independent approval is granted. Keep the four individual Elements intact for angle-specific control. Do not silently create a new identity.

## Bathroom: preserve the same **Dutch residential space**

Our initial creative approval is a credible, compact Dutch bathroom: matte greige large porcelain tiles with correctly scaled grout, glass walk-in shower with black frame and fixtures, oak floating vanity, niches, warm indirect light and a practical residential footprint. **Not a Spanish villa or an infinite spa.** The founder liked the original scene, not its artificial mat as an exact factory product.

To expand environment views, start with the same source photo and, where relevant, the completed five-second camera test. Prefer cropping/reframing *existing* pixels as candidate assets over inventing a new opposite wall. New genuine room angles need a coherent 3D scene or overlapping camera references, not merely verbal 'same room'.

Current separated examples:
- `Bathroom_01` original approved architecture.
- `Bathroom_Mid_01` at ~2.0 seconds in first motionproof, candidate.
- `Bathroom_Close_01` at ~4.3 seconds in first motionproof, candidate.
- `Bathroom_Shower_01` crop from the original, candidate.

Room QA: location of shower glass and door, direction of oak grain, cabinet layout, lights and niches, tile grout intersection, scale relative to a true 60×39cm mat, shadows and practical walking path. A crop is **not a new camera angle**. Changing camera viewpoint from one photo is still an inference.

## Stone: supplier photo as geometry/calibration only

User-supplied apparent supplier photo shows an asymmetric left-origin wave/groove system. Previous AI concepts introduced broad repeated waves across the whole mat and are therefore **not a source of product truth**.

Current reference types:
- `Stone_Top_01`: original user-supplied source top view (internal only, rights unknown).
- `Stone_Grooves_01`: direct pixel crop of grooves.
- `Stone_Corner_01`: direct pixel crop of corner/grooves.
- `Stone_Oblique_01`: source top view perspectively warped (2D illustration, **not calibrated 3D**).

Do not borrow the 9mm thickness or black anti-slip backing invented in previous AI material. VDSTM-007 listing describes 60×39cm but exact source-to-SKU match, thickness, underside and rights are not verified. In product gallery, numerical dimensions must come from verified supplier data and deterministic design tools, **never AI-generated text**.

### Standalone product photograph prompt for a future **sample-verified** model

~~~text
Produce ONE product-only studio image, never a montage.
Using the exact signed-off product photograph/3D geometry, preserve the
asymmetric upper-left wave design, the right-side smooth field, the actual
mat corners, white color, source grain and real dimensions.
Only the camera, set, light and background may change as explicitly requested.
No new grooves, no broad parallel ridges, no invented rubber base or thickness,
no logo, no certifications, no claim icon and no printed dimensions.
If the requested angle cannot be derived from the supplied photographs without
inventing geometry, RETURN A BLOCKED CONCEPT rather than a product master.
~~~

**For the current SKU:** don't use this prompt to pretend a 3/4 view is factory-accurate. Wait for a sample/authorized multiple-angle photos or a calibrated 3D reconstruction. AI product-in-room videos may be *concept footage*, but product claims must not rely on them.

## Versioning & proof log per file

Every output has:
- immutable logical label `AVELNA/[ENTITY]/[VIEW]/vN`;
- original source SHA, optional rendered output SHA;
- model/provider, prompt ID+hash, reference IDs **in private manifest**;
- actual image pixel dimensions, orientation, color profile (if known);
- `status: candidate / owner_approved / archived` **separate** from Higgsfield `status: completed`;
- visual QA notes, legal rights scope and whether it may be used as proof of physical product details.

End-of-round retrospective: **what changed intentionally**, **what drifted**, **what was accepted**, **what failed**, **cost and time**, **next one-variable correction**. Never call a contact sheet a hero asset.
