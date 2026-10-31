# 03 — Multishot continuity, camera grammar and water physics

## Objective and evidence levels

Create a premium AVELNA hero film with *one* coherent space, person, mat, time of day and logically progressing action. The creative goal is a calm Dutch bathroom: a slow architectural push-in, a woman leaving the shower, a foot touching the mat, and a natural product-focused ending.

**Important separation:**
- `cinematic_reconstruction`: an artistic representation of the bathroom; acceptable for pre-launch creative tests when labelled.
- `physical_demonstration`: a measurable, product-specific water absorption/anti-slip/drying claim. **Not supported yet** by the actual supplier sample; do not publish the dramatized dry-down as objective proof.
- `SKU_identity`: exact marketable product appearance. The existing room concept includes an AI mat, the Stone top-view is an attributed supplier source with unverified rights and identity, and new 3D oblique projections remain illustrative.

A strong-looking scene is **not** evidence of accurate product physics.

## World bible — fixed room constraints

Create a small **Dutch residential bathroom**, not a sprawling resort:
- large warm-greige stone-look rectangular tiles, physically sensible spacing and grout alignment;
- walk-in shower with black framed glass, glass edge and threshold grounded in the room;
- oak floating vanity on the *same side* in all shots;
- consistent black shower mixer/head, recessed niches and LED strips;
- towel placement and vanity drawer configuration unchanged;
- same off-white rigid mat beside the shower exit; if the human needs to step directly onto it, verify the distance and orientation.
- realistic dry-side floor, with water confined to inside the shower except localized carry-over from feet or a few droplets.

**Anchor:** `@AVELNA_Bathroom_01` is the approved creative environment. `@AVELNA_Bathroom_Mid_01`, `@AVELNA_Bathroom_Close_01` and `@AVELNA_Bathroom_Shower_01` are derived candidates, not independently verified camera views. A new true reverse angle requires a coherent floor plan / 3D scene.

### Continuity bible per frame

Track these per clip:
1. Camera floor point, yaw/pitch and lens role, horizon, left/right wall orientation.
2. Tile grout intersections (relative to mat corners) and same size/spacing.
3. Shower threshold, shower glass base and opening direction.
4. Mat quadrilateral, mat rotation, corners, grooves and floor contact.
5. Light fixture/niche positions, shadow direction, oak color and fixtures.
6. Character identity, towel hem, left/right moving foot, direction, skin wetness.
7. Wet zone on shower floor (allowed), dry zone outside shower (fixed) and mat contact zones (localized).
8. Water trajectory: source point, gravity, time, amount, destination. If source cannot be explained, remove the droplet.

Record an optical-flow/visual difference of key static landmarks between final frame of shot N and start of shot N+1; new camera angle permits projection differences, **not changes to objects**.

## An operational spatial map

The room should be drawn once as a simple coordinate sketch and approved; this is a production tool, not a new bathroom design. Example relative map, not an exact measured floor plan:

~~~text
                 WALK-IN SHOWER (wet zone)
       ┌────────────────────────────────┐
       │                                │
       │  shower/mixer                  │
       └────────glass / open threshold──┘
                                  ↓ first wet step
       ┌────────────────────────────┐
       │    Bath Stone 60 × 39 cm   │    ← dry-side mat
       └────────────────────────────┘
          dry floor       oak vanity →
~~~

**Mat must occupy a plausible landing zone.** In the existing approved room frame, the visual mat may not be perfectly aligned to the walking path; do not make the person teleport, step across a distant wet floor, or stretch a leg beyond plausible body mechanics. Adjust the *camera/pose staging* after the founder approves a new scene frame, rather than moving the approved mat secretly.

### Shot 1 — The Approach (already performed)

- Intent: visual premium environment introduction, bath mat in frame.
- Reference: original `@AVELNA_Bathroom_01`.
- Existing 5.04s provider clip exists; Cinema Studio Video v2.
- A 3:4 frame was initially rejected (actual endpoint permits only 1:1, 16:9, 9:16 for this call), 9:16 request returned approximately 856×1072/4:5 file. Treat output geometry as measured, not requested.
- No model, no water, no product effect. Zoom/dolly may cause geometry drift; inspect actual footage before reusing the final frame.
- Do not reuse this clip as an approval to depict the exact Alibaba mat.

### Shot 2 — The Step Out (target 3–4s)

- **Camera setup:** low-to-mid position 35–50mm equivalent, 15–30° to the shower exit, dry-side mat visibly connected to shower threshold; lock camera for one take or use a tiny dolly.
- **Action staging:** adult female character, white wrapped towel, realistically wet hair/legs; only knees/thigh down visible for the motion sequence if that preserves focus. One trailing foot still inside wet zone; leading foot travels directly to the mat. Landing position and footprint area must agree with next shot.
- **Source:** original or approved close environment image + `@AVELNA_StepWoman_Front_01` / `@AVELNA_StepWoman_Lower_01`. **These Elements are technical candidates; verify character before paid job**.
- **Water:** wet shower interior, dry floor beyond glass, thin water film on the leading foot, occasional beads along ankle. No flood, shower spray through glass or far-reaching trail.
- **End frame:** foot just touching mat or initial weight transfer. Camera angle and which foot lands must be captured in the next shot's anchor.

### Shot 3 — Foot Contact / Lift (target 3–4s)

- **Camera setup:** true low three-quarter or semi-top product close-up with mat and foot both distinguishable. 70–100mm equivalent look, little perspective distortion.
- **Action:** foot contacts a real rigid mat; normal heel-to-toe load progression for the chosen walking action (not mandatory to be heel-first in every pose); toes flex naturally, no extra toes, ankle not inverted. The mat remains flat, hard, not bending. Weight shifts forward; then that foot lifts.
- **Moisture deposition:** the **actual loaded contact patch** can darken: heel rim, ball of foot/metatarsal heads and toe pads. An arch may contribute little/no contact depending on person's arch and stance; don't stamp a generic perfect complete silhouette. A few gravitational droplets might fall directly to the mat. No uniformly wet stone, flooded surrounding floor or droplets from nowhere.
- **Proof limitation:** a plausible AI wet footprint is a speculative visualization until physically tested. We must not claim it is the factory product's observed performance.

### Shot 4 — Dry-down / Reveal (target 3–6s depending on test)

- **Camera:** match last Shot 3 product crop and **locked** wetness mask; allow slight stable end shot. Do not change mat texture, light, tile color, groove count or camera unexpectedly.
- **Motion:** darkened contact zones may lighten over time in a stylized concept only. In reality, a diatomite mat can absorb moisture into pores before it evaporates; disappearance of visible surface marks does **not** mean complete physical drying.
- **Timing:** no stated "dries in 5s/30s/60s" until measured on the exact sample under declared conditions. No magic instantaneous wipe or synthetic certainty.
- **Final composition:** product visible and recognizable, end-card/logo added in edit outside generation. If true drying footage cannot be substantiated, replace with a close material-detail shot and neutral brand end card without a speed claim.

## Why not generate all four as one prompt?

Past image attempts requested 4–6 storyboard frames and produced grids with **different room topology and incorrect straight/generic grooves**, even when our text said 'same asset'. A long AI video creates even more temporal drift.

Use:
1. **One standalone approved keyframe per shot**, built with actual linked references (not just a text description of `@name`).
2. Start-image / end-image when supported; constrain only a limited action per clip.
3. Resolve and specify exact product, room and character IDs for the **particular model**.
4. Render single clip; inspect frame-by-frame.
5. Extract and review the last frame as potential next-shot continuity anchor; approve it separately, don't treat completed automatically as good.
6. Cut in a conventional editor at action points rather than relying on the model to do transitions. Hard cut on foot movement often hides more artifacts than synthetic crossfades.
7. If the new camera angle is physically impossible from refs, block and create a real 3D scene/sample photos first.

## Seamless editorial transitions

- **Match-on-action:** Shot 2 ends with leading foot lowering; Shot 3 starts with foot at same stage, same direction of movement and weight distribution. Match animation pace, not just colors.
- **Axis of action:** choose one camera side of shower-to-mat direction. Only change to other side if a spatial establishing angle establishes direction first.
- **Continuity marker:** mat's distinctive upper-left wave source must stay on the same logical mat corner. No mirroring product left/right to make a pose fit.
- **Color:** sample neutral tile regions and towel white, record a shared contrast/WB reference. Do not equalize away true product color.
- **Motion cadence:** 24 or 25 fps, mild motion blur consistent between shots; no giant slow-motion splash. Intermediate outputs may be 856×1072, so conform with a safe edit crop after preview.
- **Audio:** at most subtle wet bare-foot contact and room ambience, rights-verified; not required for the hero. Autoplay muted, accessible overlay and reduced-motion alternative on webshop.

## Wetness QA — physical logic and editorial truth

Water transfer depends on skin hydration, foot orientation/contact area, pressure/time, temperature, humidity and actual mat porosity. We have not measured these for VDSTM-007.

**Pass physical plausibility:**
- source of water = last shower or wet lower legs;
- floor outside shower = mostly dry;
- droplet arcs = gravity-driven and limited;
- wet contact corresponds to foot in position;
- dark imprint limited to zones that touched;
- matte stone stays stone, without becoming rubber or soft fabric.

**Fail:**
- entire bathroom floor suddenly wet, as in earlier failed attempt;
- foot hovering but already leaving a full foot-shaped stain;
- toe count wrong, multiple identical imprints from a single step;
- water appearing beyond the foot at arbitrary distance;
- stain shrinking at exact uniform speed without test evidence;
- product surface changing from left-origin wave to full-width rows;
- a shot using a different bathroom vanity/fixture layout.

Do not misuse an imagined imprint as a false speed/durability/anti-slip proof; finish with a restrained, aspirational commercial only after claims reviewed.

## Keyframe / prompt source of truth

- Original authored prompts for Shots 2 and 3 in `prompts/shot-02-step-out-v1.md` and `prompts/shot-03-foot-contact-v1.md`.
- The first actual Shot 1 prompt is preserved in [PR #14](https://github.com/jens-mul/AVELNA/pull/14) pending merge. Do not duplicate it with a subtly different phrase.
- Use a frozen per-shot manifest: asset aliases+versions, reference hashes, actual model ID, camera, timeline, seed if supported, cost quote, date and explicit owner review.
- The model's response is not immutable proof of the keyframe continuity; independently inspect outputs.

## Pass standard for a real product advertisement

A good demo must have **both** cinematic craft and product fidelity. If we cannot hold the exact mat while generating foot contact and wetness, fall back to **a product-truth packshot + independently shot proof**. Don't push a cinematic hallucination into a commercial product claim.
