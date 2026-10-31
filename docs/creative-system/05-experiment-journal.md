# 05 — Evidence journal: experiments and lessons from our first AVELNA sessions

This is a historical record of **what was actually attempted** in the ChatGPT–Higgsfield workflow, with observed outcomes and limits. It is not a collection of success claims. Dated 2026-10-31. Future rounds append an immutable entry with file hashes and actual provider readbacks.

## Context — product and art direction

- Business: AVELNA, two founders, total initial cash ceiling €200, self-managed fulfillment and webshop, **individual product sales**.
- Supplier: Longyan Yongye VDSTM-007 hard stone mat candidate, publicly described as white and 39×60 cm, but the Alibaba page has a **1-unit tier conflicting with 'MOQ 100'**. Product construction, exact thickness, backing, shipping, weight, legal image rights and sample not yet verified. [Supplier listing](https://www.alibaba.com/product-detail/Fast-Drying-Hard-Bath-Mat-Super_1601587124238.html).
- Initial AI concept images of a smooth ivory mat contained no supplier-specific asymmetric grooves. Later three wavy concept renders also used a different groove path from the source. This demonstrated why descriptive 'use exactly this mat' prompting alone is unreliable.
- Accepted **environment mood**: recognizably Dutch contemporary residential bathroom with larger warm-greige tiles, black glass/fixtures, oak vanity and warm LED light. Spanish/Mediterranean and Japandi were exploratory, not approved locks.

## Chronological learning record

| Phase | What we did | Observed outcome | Decision |
| --- | --- | --- | --- |
| **A. Concept image** | Approved an AI Dutch bathroom hero with off-white stone-like mat | User liked composition and motion potential; mat was imaginary | **Room art direction approved only**, not SKU |
| **B. Product sheet** | Generated multi-view 'technical' sheet without complete source geometry | Invented 9mm thickness / dark underside / wrong repeated grooves | Rejected as product evidence. No text-only product claims |
| **C. Supplier truth** | Compared user-supplied Alibaba top photo with AI product stills | Real asymmetric left-origin arcs differ strongly | Original supplier photo becomes **internal geometry calibration** |
| **D. Controlled crop** | Retained supplier-source top pixels, masked surroundings, made source-derived detail/size image | Product groove path preserved (RGB unchanged within crop), labels deterministic | Useful 2D identity, **not a 3D digital twin** |
| **E. First video** | One image-to-video camera-only 5s Higgsfield Cinema Studio Video v2 | Job completed; 5.042s, 856×1072, 5 credits after first rejected 3:4 parameter | Valid **provider motion technical proof**, framing and product continuity require review |
| **F. Full water storyboards** | Multiple AI still attempts asking for complete foot/water/drying sequence | Repeatedly produced contact sheets, changed room topology and product grooves | **Do not use as production frames**, no physical evidence |
| **G. Source-locked composite** | Perspective-warped original product top source into existing room, added concept wet-foot mask | Product source geometry more stable, dry surrounding floor | Promising controlled visual method, physics still **simulated and unverified** |
| **H. StepWoman V0** | Extracted a model from a concept shot and attached to previous scene | Poses/contact shadows and perspective inadequate | Rejected as final shot, keep concept-only |
| **I. Standalone character images** | Several failed multi-panel outputs, then **four independent higher-resolution studio photos** (front/back/upper/lower) | Crisp separate images; visually related fictional character | Uploaded individually and registered as character Elements; owner review of cross-angle identity still required |
| **J. First 3 reference Elements** | Saved one bathroom, one supplier-based prop and old model mosaic/crop as reusable Elements | Three provider status `completed` | Technical experiment; **old StepWoman later deprecated** |
| **K. Current 4+7 Elements** | Added four StepWoman and seven Bathroom/Stone Elements, individual sources and proper library placements | Provider readback now shows **14 Elements total**, all `completed` | Reuse names/IDs, distinguish completed vs approved |
| **L. Old StepWoman retirement** | Attached old source to archive folder | Old `StepWoman_01` Element remains in index; no standalone delete action exposed by MCP | Mark `deprecated_but_exists`, never generate using old alias |

## Specific 5s motion experiment

- **Exact prompt and readbacks** are recorded in [PR #14](https://github.com/jens-mul/AVELNA/pull/14), pending merge.
- Cost quotes at the moment: Cinema Studio Video v2 **5 credits** for 5s, Kling v3 std 7.5, Seedance 2.0 Mini 5, Grok 1.5 Lite 5; not tested as quality head-to-head.
- Model discovery claimed `3:4` available; backend rejected, allowing `1:1`/`16:9`/`9:16`. A re-quote for `9:16` still said 5 credits and one job submitted.
- Delivered MP4 dimensions ~856×1072 (closer to 4:5) despite requested 9:16. **Never assume output aspect from request only.**
- Balance after first test read as 5 credits, later 55; reasons for the intervening change have **not been established** and shouldn't be attributed to this workflow. Always check live.
- No proof of 'ready for paid ad' from video completion.

## Current library inventory and provenance

`@AVELNA_Bathroom_01` — founder-liked *room composition*; created as environment Element. Room includes an AI-mat whose manufacturing accuracy is not proven. 
`@AVELNA_Bathroom_Mid_01` and `@AVELNA_Bathroom_Close_01` — still frames at ~2.0 and ~4.3 seconds of first motion clip. They are **generated motion frames** rather than additional physically photographed locations.
`@AVELNA_Bathroom_Shower_01` — crop of original, no new viewpoint.

`@AVELNA_StoneConcept_01` — earlier concept; `@AVELNA_Stone_Top_01` actual supplied top-view supplier photo; `@AVELNA_Stone_Oblique_01` a 2D perspective transform of the top view; `@AVELNA_Stone_Grooves_01` and `@AVELNA_Stone_Corner_01` genuine pixel crops. No independent full 3D verification.

`@AVELNA_StepWoman_Front_01`, `Back_01`, `Upper_01`, `Lower_01` — separate images generated individually and uploaded. `@AVELNA_StepWoman_01` exists but must no longer be selected.

Provider Element IDs, media IDs and folder UUIDs are **private operational metadata**, discoverable live. Do not paste account URLs or personal identifiers in the public repo. Safe names and status only are in the public template.

## Our strongest current lessons

1. **Single-image brief is essential.** “One image only, no grid” is required but not sufficient; inspect output and reject montage anyway.
2. **Never call a source crop a new camera angle.** Move to real multi-view capture / 3D if true physical accuracy is required.
3. **An Element is an identity aid, not a guarantee.** It anchors reference media, but geometry and person can still drift.
4. **Technical completion is not founder approval.** All 14 Elements can be completed and still largely candidates.
5. **One variable per test.** Camera motion separately, then foot landing, then wet imprint, then fade. Keep source images frozen.
6. **Water needs causal staging.** Water stays behind glass or on actual foot/mat contact; not the whole bathroom floor.
7. **Animation and product proof differ.** For a commercial demonstration of drying time, use actual measured footage and the real SKU.
8. **Quote and read back costs.** Tool schema and backend reality can conflict, and prompts do not enforce a credit cap.
9. **Hermes CLI-first** is the chosen execution route; ChatGPT authors images/prompts, founders approve.
10. **Don't erase failures.** They reveal the precise missing capability and drive better asset models.

## Next experiment (not yet performed)

A **single Shot 2 keyframe using linked environment+character+product Elements** with a dry floor and realistic foot on mat, followed by manual art-direction review. Only then a **separately budget-authorized** 3–5s video (if appropriate). We have not yet proven one-pass controlled body motion, true video water physics, or exact material performance.

If the model cannot preserve the top-left groove geometry while adding a woman, favor compositing a true source-backed mat or a calibrated 3D model and treat the rest as creative CGI.

**No future operator should report 'complete AVELNA hero ad' based solely on these experiments.**
