# AVELNA creative workflow — external source register

Checked: 2026-10-31. This is a dated source register. Re-check actual provider schemas, account permissions and pricing before each paid launch.

## Higgsfield primary sources
- [Higgsfield to agent / Hermes official connection](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent): ChatGPT Plugin; Hermes CLI + skills; Elements; credit policy; warns that prompt-level credit caps are not enforced technical limits.
- [MCP vs web](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-higgsfield-mcp): programmatic generations use credits, web unlimited does not automatically apply. Account tool separately reported a specific free Genjutsu-style voucher; that voucher is model- and task-specific, not a generic free-image allowance.
- [Higgsfield CLI guide](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-access-higgsfield-via-cli): existing official skills and CLI; check installed version and actual reference-input syntax, do not invent flags.
- [Canvas](https://higgsfield.ai/creator-hub/help-center/tools/how-do-i-use-canvas): building/storing node graphs without running is free; executing nodes can charge credits.
- [Higgsfield changelog](https://higgsfield.ai/creator-hub/changelog): models, limits and behavior can change.

## Current live Higgsfield observations (this session)
- Separate native Element IDs, source-media IDs and folder placements.
- 14 completed reference Elements in three categories; their technical status does not equal founder approval.
- Native MCP expects `<<<UUID>>>` embedded in prompt for specifically supported Element-capable models. Bare `@name` is not a guaranteed MCP binding. CLI syntax remains to be discovered from Hermes' installed skills.
- A standalone delete-Element tool was not discovered; archiving/removing a placement is not deleting the Element.
- Upload+confirmation+attach+Element creation were actually exercised. No new paid generation was needed for those operations.
- First earlier five-second camera video required a backend-compatible ratio despite advertised model options; actual 856x1072 output size.

## Hermes primary documentation
- [Hermes Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/): project skill directories `.hermes/skills/` and `.agents/skills/`, trust and discovery.
- [Work with Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills/): progressive skill loading and careful versioning.

## Founder-provided video
[How to Use Higgsfield AI Better than 99% of People](https://www.youtube.com/watch?v=dJSJMt4ESEU). Public metadata refers to Elements, consistent character imagery and Angles features. The spoken narration/transcript **was not completely accessed**. We rely on verified current provider behavior, not an assertion that we heard unverified detailed instructions.

## Product and in-repo evidence
- [VDSTM-007 Alibaba candidate](https://www.alibaba.com/product-detail/Fast-Drying-Hard-Bath-Mat-Super_1601587124238.html), 39x60cm white hard diatomite candidate; MOQ information conflicts. The user supplied a visually attributed top-view image. Exact rights, backing and geometry not independently validated.
- [AVE LNA environment concept](https://github.com/jens-mul/AVELNA/blob/main/assets/approved/avelna-dutch-bathroom-approved-v1.webp): founder-approved as a **room** master, not an actual verified supplier Bath Stone.
- [Product shortlist](https://github.com/jens-mul/AVELNA/issues/12): catalog/supplier candidates, not purchase order.
- [Actual motion proof/production prompt, PR #14](https://github.com/jens-mul/AVELNA/pull/14): first paid provider camera test, not merged to main at research date.
- [Product-truth code and notes, PR #13](https://github.com/jens-mul/AVELNA/pull/13): source-pixel mask and 2D dimensions, not a true digital twin.

This source register does not validate the actual factory SKU, physical water performance, customer acquisition cost, or live ad quality.