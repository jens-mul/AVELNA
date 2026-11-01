# AVELNA — Brand Palette Lock: Olive Mineral (04)

**Status:** LOCKED — approved brand color decision, not a completed logo or finished webshop.  
**Decision date:** 2026-11-01 (explicit owner instruction in the AVELNA ChatGPT project).  
**Brand version:** 1.1.0.  
**Authoritative machine-readable colors:** [config/brand.tokens.json](../config/brand.tokens.json).  
**Creative specification:** this file, together with [docs/brand.md](brand.md).  
**Approved bathroom environment:** [assets/approved/avelna-dutch-bathroom-approved-v1.webp](../assets/approved/avelna-dutch-bathroom-approved-v1.webp) and its [approval notes](../assets/approved/README.md).

## 1. Decision and scope

Palette Proposal **04 — Olive Mineral** is the sole approved **brand identity palette** for AVELNA. Palette Proposal **03 — Sand & Linen** is retained only as complementary **photographic/environmental art direction** (warm light, linen, sand, natural oak, stone); it is **not** an alternative logo palette or second set of website/UI tokens.

This approval covers **the five exact digital HEX tokens and their application principles**. It does **not** approve a specific logo, font license, product color, supplier SKU, physical printing proof, creative output, campaign, ad spend, or commercial claim. Do not relabel an AI concept as an actual manufacturer's finish or change a product's appearance to match these tones.

The founder-approved 2026-10-31 bathroom reference remains the **approved environment/composition**. Today's color decision neither recolors it nor makes its rendered Bath Stone a verified product. Image generation and creative direction remain with the founder + ChatGPT; Hermes executes only separately approved masters/prompts (see issue #11 owner decision and existing asset rules).

## 2. Why Olive Mineral

The founders compared Palette 03 and Palette 04 across five qualitative strategic criteria. This is a **design decision, not the result of a randomized consumer study**:

| Criterion | Rationale | Lean |
|---|---|---|
| Fit with approved bathroom scene | Sand & Linen most literally echoes the warm greige tiles, oak and off-white bath stone | 03 |
| Potential distinctiveness | Sage/olive mineral notes can provide a consistent recognizable cue beyond commonplace beige | 04 |
| Premium, long-lived identity | Natural mineral and warm charcoal combination is versatile beyond Bath; longevity remains a hypothesis | 04 |
| UI and packaging system | Light/dark core plus two accents supports editorial use without requiring colored buttons | 04 |
| Intended brand feeling | Calming, considered, architectural, credible, not loud wellness marketing | 04 |

The conclusion was **04 for brand identity + 03 for photography**. It does **not** prove that olive is objectively more memorable or improves conversions. Distinctiveness must later be earned by consistent use and tested with customers (unprompted recall, attributed recognition, accessibility, click/purchase data). Keep one brand palette to avoid fragmentation.

## 3. Locked color inventory

The names and HEX values below are **exact approved digital sRGB tokens**. They are not averages sampled from the AI moodboard and do not describe existing inventory.

| Canonical key | Brand name | HEX | Purpose |
|---|---|---|---|
| alabaster | Alabaster | **#F5F2EC** | Main page canvas; generous negative space; calm warmth |
| stone | Stone | **#D4C9BC** | Secondary surfaces, panels, quiet divisions, packaging substrate inspiration |
| sage_grey | Sage Grey | **#9DA08E** | Soft botanical/mineral accent, noncritical visual layers |
| olive_smoke | Olive Smoke | **#7C806E** | Small, recurring distinctive brand accent; decor and larger motifs |
| deep_mineral | Deep Mineral | **#31332F** | Primary text, wordmark, dark surfaces, primary CTA |

**Role hierarchy:**
1. Alabaster dominates major backgrounds and breathing room.
2. Stone creates a gentle second level; it must not replace text contrast.
3. Deep Mineral carries information and action. Make it immediately legible.
4. Sage Grey is supportive/atmospheric, not the default text color.
5. Olive Smoke is the brand's deliberate visual signature, **not** a permission to put tiny text on muted green.

These are roles, not statistically validated ideal area percentages. In a new composition, aim for an overwhelmingly neutral field with a single restrained sage/olive motif rather than equal-width blocks of five brand colors. Product and photography should remain recognizable.

### What is explicitly superseded

The earlier unapproved tokens Chalk #F3F0E9, Sand #D3C6B6, Charcoal #292A27, Warm Grey #8B877F and Olive Grey #858B7C were **provisional** in Brand Bible v1.0. They must no longer be described as the locked brand colors. A legacy photograph may still contain those hues as environmental lighting/material; this is not permission to use the old values as new interface tokens.

## 4. Semantic UI mapping

The canonical color names reside in JSON under colors. The semantic_colors entries in the same file contain **references to those keys**, not new HEX values. Resolve those names before use.

| Semantic role | Resolve to | Application |
|---|---|---|
| page_background | alabaster | Main website background |
| section_surface | stone | Alternating bands, soft card surfaces |
| text_primary | deep_mineral | Body, headings, prices, navigation, forms |
| text_on_dark | alabaster | Reversed copy on Deep Mineral |
| primary_cta_background | deep_mineral | Buy/subscribe button |
| primary_cta_text | alabaster | Legible primary CTA label |
| soft_accent | sage_grey | Nonessential rules, motifs, large surfaces with tested text |
| identity_accent | olive_smoke | Small graphic mark, decorative tag, repeatable signature |

Recommended **minimal CSS implementation example** (adapt to the webshop framework; not an existing deployed CSS file):

~~~css
:root {
  --avelna-alabaster: #F5F2EC;
  --avelna-stone: #D4C9BC;
  --avelna-sage-grey: #9DA08E;
  --avelna-olive-smoke: #7C806E;
  --avelna-deep-mineral: #31332F;

  --color-page: var(--avelna-alabaster);
  --color-surface: var(--avelna-stone);
  --color-text: var(--avelna-deep-mineral);
  --color-primary-button: var(--avelna-deep-mineral);
  --color-primary-button-text: var(--avelna-alabaster);
  --color-brand-accent: var(--avelna-olive-smoke);
}
~~~

Use the JSON as the color source, not copied HEX values spread through unrelated application files. Other functional colors (errors, success, warning, focus states) need separate, accessible semantic decisions; do not silently treat Sage Grey as a success indicator or Olive Smoke as a disabled state.

## 5. Contrast and inclusive design

Calculated with the WCAG 2.2 relative-luminance contrast formula for the exact sRGB HEX values above (rounded to 2 decimals). W3C reference: https://www.w3.org/TR/WCAG22/#contrast-minimum and https://www.w3.org/TR/WCAG22/#non-text-contrast .

| Foreground / background | Contrast | Ordinary text (AA 4.5:1) | Decision |
|---|---:|---|---|
| Deep Mineral / Alabaster | **11.42:1** | Pass | Default text and reversed primary button |
| Deep Mineral / Stone | **7.83:1** | Pass | Text on secondary surfaces |
| Alabaster / Deep Mineral | **11.42:1** | Pass | CTA and dark footer |
| Deep Mineral / Sage Grey | **4.77:1** | Pass (limited margin) | Allowed, verify actual rendered states |
| Olive Smoke / Alabaster | **3.64:1** | **Fail** | Decorative, or appropriately large text only |
| Alabaster / Olive Smoke | **3.64:1** | **Fail** | Do not use as ordinary button labels |
| Deep Mineral / Olive Smoke | **3.14:1** | **Fail** | Do not place ordinary body text here |
| Sage Grey / Alabaster | **2.39:1** | **Fail** | Decorative only; never low-contrast fine print |
| Alabaster / Stone | **1.46:1** | **Fail** | Adjacent surfaces, not text |

WCAG 2.2 AA requires a minimum 4.5:1 contrast for normal text and 3:1 for sufficiently large text; meaningful non-text UI indicators generally require at least 3:1 against adjacent colors. A passing color-pair result **does not** establish that the whole page is WCAG-compliant: fonts, opacity, hover/focus, photo overlays, disabled states and actual DOM controls must all be checked. Use shape/text as well as color to indicate state.

**Default safe pairings:** Deep Mineral text on Alabaster or Stone; Alabaster on Deep Mineral. **Never** use Sage Grey on Alabaster for ordinary copy; Olive Smoke is an accent, not a small-label foreground.

## 6. Practical examples by touchpoint

### Webshop / UI
- Header: Alabaster background, Deep Mineral wordmark/navigation, restrained spacing; no sage low-contrast nav labels.
- Product detail: photographs remain true to the actual product; Alabaster canvas; Deep Mineral title, price, size, care and add-to-cart controls.
- Product cards: use Stone only as a considered section surface, not as a filter that changes the product's visible color.
- Primary action: solid Deep Mineral with Alabaster label. Secondary action: quiet outline/text; validate border, focus and hover states in situ.
- Footer: Deep Mineral surface with Alabaster copy; sage/olive can be a small decorative motif, not ordinary footer body text.
- Status messages: explicit accessible functional color/icon/text separate from the five brand tones.

### Packaging / printed matter
- Off-white substrate inspired by Alabaster; Deep Mineral high-contrast wordmark, instructions and essential legal/importer information.
- Stone for restrained supporting panels; an Olive Smoke motif or small signature can recur on label, insert and thank-you card.
- Real print stocks, coatings, CMYK/profile and proofing can materially change appearance: **do not assert digital HEX equals a confirmed printed color**. Check legibility of mandatory information and test actual print samples.

### Logo, icon and type (still open design tasks)
- Prefer an architectural, distinguishable wordmark concept, **not yet approved or trademark-cleared**. Test dark Deep Mineral on Alabaster and light Alabaster on Deep Mineral before adding variants.
- Do not automatically make the wordmark sage or olive; novelty must not come at the cost of legibility.
- Use a licensed, readable sans for UI; restrained serif may be explored for editorial headings. The serif wordmark appearing on generated moodboards **is a concept, not a chosen final logo**.
- A future symbol must work in a single ink color, at favicon scale and without a styled bathroom photo; repeat it across media only after separate approval.

### Creative / paid social
- Use the approved Dutch bathroom environment as the visual reference: large warm greige stone-look tiles, black trim/fixtures, floating oak vanity, warm recessed lighting, calm styling and an obvious light Bath Stone concept.
- Keep the true verified product materially unchanged. The reference is **not SKU proof**.
- Put readable text and CTA in the editing stage, not in the generated product or scene. On light backgrounds use Deep Mineral; on dark panels use Alabaster.
- Check 9:16 and 4:5 placement crops; the product should stay recognizable. Palette lock does not grant rights, budget, promotional claims or asset approval.

## 7. Palette 03: supporting photographic language, not identity

Sand & Linen (03) remains a **styling guide only**. Its original proposed colors were Linen #F4F0E8, Dune #DCCDBA, Oat #C8B79E, Driftwood #A89783 and Warm Ink #343230. Treat them as moodboard annotations for light, linens, stone and wood, **not** as website/brand HEX assignments.

Use this photographic direction for:
- Warm greige stone and real-looking oak (compatible with the approved bathroom reference).
- Controlled, soft warm light, realistic grain and tactility.
- Light neutrals that support an immediately identifiable bathroom object.
- Editorial compositions, calm shadows, no overly styled luxury set.

Do not apply Palette 03 colors to the AVELNA logo, CTA buttons, nav text or packaging ink by default; those use Palette 04. Do not force a physical product to be sand/olive if its verified catalog variant is different.

## 8. Governance, versions, approval boundaries

- **Owner-approved decision:** Palette 04 HEX values and identity hierarchy, 2026-11-01. No implied approval of final rendered moodboard output as commercial product evidence.
- **Previously approved asset:** bathroom environment/composition from 2026-10-31, referenced above. Remains unchanged and separate.
- **Pending:** actual product/SKU identity and safety, real product colors, final logo/type licensing, printed proofs, master campaign assets and live implementation.
- **No autonomous redesign:** Hermes, growth scripts and content agents may not substitute 03, re-pick colors, invent a shade, or produce new masters without the owner's + ChatGPT creative process. Reuse the locked tokens in prepared work; pay/spend and publication still require their independent controls.

To revise the locked palette in the future:
1. Record a new explicit owner decision with the reason and desired usage.
2. Change this document and config/brand.tokens.json together, incrementing the palette/version identifier.
3. Update the contrast test and any dependent UI/creative references; review impact on approved masters and logos.
4. Review actual mobile contrast, visuals and rights before production. Do not treat a commit or palette update as approval to relaunch ads.
5. Preserve the old decision in version history instead of quietly overwriting historical asset approvals.

## 9. Review checklist

- [ ] All five canonical HEX values match Palette 04 exactly.
- [ ] UI semantic keys resolve to approved colors; no legacy 'Chalk/Sand/Charcoal/Warm Grey/Olive Grey' in the **active brand tokens**.
- [ ] Palette 03 appears only in photography/environment styling, not interface defaults.
- [ ] Regular copy/CTA labels pass WCAG AA contrast in actual components, including states.
- [ ] Wordmark/final logo and license are separately reviewed; moodboard lettering is not mistaken for an approved logo.
- [ ] The approved bathroom reference remains intact and any real SKU/product claims are independently verified.
- [ ] No creative media, ads, spend, manufacturing specification or physical print is implicitly approved by this lock.

**Change log**
- **2026-11-01 / v1.1.0:** locked Palette 04 Olive Mineral, assigned semantic UI roles; retained Palette 03 only as photographic direction. Replaced provisional palette from brand bible v1.0.
