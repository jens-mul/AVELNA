# 06 — Hermes CLI handoff: execution without autonomous creative changes

## Goal

ChatGPT and the founders generate and select **every** initial image and **every** creative prompt. Hermes does not independently pick a brand style, generate an alternative character, rewrite a prompt or choose a different visual. Hermes executes an *approved shot packet* through its existing personal Higgsfield CLI skills, makes mechanical exports, checks outcomes, and reports any missing approval.

This is the chosen **CLI-first** system. **Do not build a second conflicting Higgsfield skill stack inside AVELNA.**

## Verified external documentation

- [Higgsfield's official Hermes/CLI instructions](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent) identify `npm i -g @higgsfield/cli`, `higgsfield auth login` and `npx skills add higgsfield-ai/skills` for CLI-based agents.
- [Higgsfield CLI guide](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-access-higgsfield-via-cli) says the official skills include `generate`, `soul` and `product-photoshoot`. Existing personal skills should be inspected and reused **without forcing installation or upgrades unless necessary**.
- [Hermes Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/) says project-local skills are discovered from `<project-root>/.hermes/skills/` or `.agents/skills/`, after repo trust. The old `skills/avelna-creative` directory is a source bundle, **not automatically a project-local skill**.
- The live Higgsfield MCP adapter uses `<<<Element UUID>>>` in a prompt to bind Elements and then translates it to a visible `@name`. **This is not evidence of equivalent CLI syntax**. Query installed CLI/skill help first. Never insert unsupported flags or assume a bare @name resolves on every model.
- Programmatic generation uses credits; unlimited web usage does not automatically apply. Check the account, quote real costs and grant separately.

## Preflight — no-spend / read-only

Hermes may do the following on its own as inspection:
1. Read `AGENTS.md`, this document, `docs/creative.md`, the exact shot brief and provider instruction version.
2. Locate its **currently installed** upstream Higgsfield CLI skill/command and check model compatibility using documented CLI help or a read-only model listing.
3. Check that the intended workspace/project, four-new StepWoman Elements, Bathroom and Stone names are present and what each references.
4. Check whether a real start frame/end frame is needed by the chosen model. For example, Kling 3.0 via current MCP needs a `start_image` even when an Element is used; CLI behavior must be verified.
5. Read current credit balance and exact per-request cost estimate. No generation by inspection.
6. Validate public manifest against private live element IDs, source SHA if available, creative approval scope and `deprecated` registry.
7. Return `READY_FOR_REVIEW` or an exact reason for `BLOCKED`. E.g. "StepWoman Upper candidate not founder-approved" is a blocker, not a reason to pick the old element.

## Valid signed shot packet

A shot packet has:
- stable shot ID and shot version, human-signed approval timestamp;
- exact immutable source file ID + SHA for each role;
- aliases from `config/creative-element-registry.example.json`, mapped to real live provider IDs *privately*;
- the complete unchanged ChatGPT-authored prompt text and its SHA;
- exact selected model, mode, duration, aspect, sound, reference roles and destination folder;
- credit quote, user-approved max and independent grant (in protected executor, not public git);
- mandatory review criteria and success state.

Hermes may inject technical transport wrappers **only if the semantics do not change**. E.g., converting an approved start image to the CLI's accepted input syntax is transport. Replacing a failed model, adding a new background, changing camera intent or generating a new video prompt is **creative editing** and must return to the founders.

## Execution protocol — finite-state machine

~~~text
INBOX
  ↓ validate signatures & assets
PREFLIGHT
  ↓ runtime tool/CLI capability evidence & quote
AWAIT_OPERATOR_GRANT
  ↓ independently checked explicit grant
SUBMIT_ONE_JOB
  ↓ record job id / external receipt / debit
WAIT_FOR_TERMINAL
  ├── failed/timeout unknown → RECONCILE_AND_BLOCK (no new job)
  └── completed
       ↓ frames/geometry/cost
QUALITY_REVIEW
  ├── failed → REJECTED, send exact artifacts to ChatGPT
  └── candidate passed → AWAIT_FOUNDER_SIGNOFF
                         ↓
                  APPROVED_DELIVERABLE
                         ↓
                  EXPORT / STAGING ONLY
                         ↓
                  SEPARATE PUBLICATION GRANT
~~~

### What Hermes must not do

- No autonomous image or prompt generation. (A founder can explicitly delegate one deterministic transform — cropping, resizing, color correction — as a processing job, not a new visual direction.)
- No supplier outreach, unapproved product switch, fake review/claim or purchasing.
- No retry loop on unknown submission status; don't "fix" content by using an old deprecated element.
- No “unlimited is free” assumption through CLI/MCP; no open-ended shot sequence.
- No moving unpaid image sources to a public CDN/repo when rights unknown.
- No full Vaultwarden export or secrets in model context. Provider credentials belong to independent least-privilege executor.
- No touching personal Hermes daemon/SSH or overwriting an unrelated deployed service.

### CLI compatibility handoff is a verified *adapter*, not magic

To implement:
1. Capture exact installed CLI version + upstream skill revision (no secret outputs in logs).
2. Discover documented models, element lookup, asset upload/list and prompt submission commands.
3. Map canonical aliases to actual supported CLI entity references via **verified** functionality. The public repo's `@names` are labels; literal `<<<UUID>>>` is a current MCP transport detail.
4. Execute a **dry-run parser/parameters check** without spending credits. If the CLI lacks a necessary feature, return a blocker instead of substituting an unsupported command.
5. Use already confirmed account assets where possible. Don't generate duplicate reference uploads by default.
6. Prepare production packet and explicit quote for owner. Submit only after permission scope fits the real request.
7. Report actual asset/job IDs and statuses in private logs, sanitize the user-facing/public report.

## Responsibility matrix

| Situation | Hermes action | Returned to whom |
| --- | --- | --- |
| User says "use old StepWoman_01" | Block + point out deprecation | Founders |
| One of four character views doesn't match the face | Do not silently switch references | ChatGPT + founders for identity QC |
| Bath Stone shows full parallel waves | Reject product fidelity | ChatGPT + founders for source truth |
| Only a crop exists but user wants genuine reverse camera angle | Block/ask for 3D or sample-backed view | Creative team |
| Model says 3:4, backend accepts only 9:16 | Record discrepancy, re-quote **before** any accepted paid job; request approval if change affects composition | Owner |
| Shot 2 floods dry floor | Reject, archive evidence, no auto retry | Creative team |
| Approved shot costs more than granted | Block, no billing | Owner |
| Uploaded media lacks placement or completed Element | Read back/correct placement without generation cost when authorized | Provider/library operator |
| New ad strategy needed | Supply metrics and a brief **request**; do not write ad prompt | ChatGPT + founders |

## The content of the final handoff report

~~~text
AVELNA SHOT REPORT
shot: SHOT-02-STEP-OUT / v1
prompt_sha256: <actual hash>
references: Bathroom_01 + StepWoman_Front_01 + StepWoman_Lower_01 + Stone_Top_01
element_media_check: completed, source role confirmed
product_accuracy: concept_only (no verified exact supplier SKU)
model: <actual supported provider model from CLI>
params: <exact accepted runtime params>
quote_credits: <actual>
grant: <reference to protected grant; no secret>
job_id: <real provider id>
provider_terminal_status: <completed/failed/...>
actual_cost_credits: <verified>
frame_QA: <pass/reject with timestamped reasons>
founder_approval: <pending/approved/rejected>
commercial_publication: blocked until real SKU/rights/claims
~~~

Never produce invented IDs, successful tests, paid job receipts or provider output links. If there are no new generated clips, say so.

## Discovery / commands for the operator (not executed here)

These **read-only** prompts are appropriate for the already installed Hermes agent:

~~~text
Read docs/creative.md and docs/creative-system/06-hermes-cli-handoff.md
on the current approved GitHub ref. Use the installed official Higgsfield
CLI skill, don't reinstall or create a duplicate skill. Show actual CLI version,
available model/Element reference inputs, the 14 reference names with lifecycle
states, and preflight ability to consume SHOT-02 and SHOT-03 packets.
DO NOT run generations, use credits, contact suppliers, publish, change
default branch, or restart personal services. Report exact blockers.
~~~

When the founders approve a new shot and associated credit cap, the executor gets the package and runs one job. **The human visual review remains a required part of the process.**
