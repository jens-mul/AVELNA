# AVELNA — AI-Native Brand & Growth System

**Version:** 1.0 — 31 October 2026  
**Owners:** two founders, Netherlands  
**Status:** documentation and code prepared; no live campaign or paid integration implied.  
**Launch cash ceiling:** **€200 total** (not an authorization to spend).

AVELNA is an architecturally minimal, premium bathroom essentials brand. The first validated sale is a single real, hard diatomite Bath Stone SKU; subsequent accessories remain in the catalogue research pipeline.

## Start here

1. **[Agent operating agreement](AGENTS.md)** — permissions, safety, boundaries.
2. **[Strategy and rollout](docs/strategy.md)** — business positioning, product validation, operating roadmap.
3. **[Brand bible](docs/brand.md)** — Quiet Architecture visual system, tone, palette.
4. **[Creative production](docs/creative.md)** — approved ChatGPT → Higgsfield → Hermes pipeline and production QA.
5. **[Higgsfield library handoff](docs/higgsfield.md)** — asset folders, Elements, alias resolution and prompt persistence.
6. **[Competitor intelligence](docs/competitors.md)** — source-backed research, repeatable competitor sweep, creative hypotheses.
7. **[Paid growth playbook](docs/growth.md)** — direct-sale and waitlist modes, CPC/CAC economics, conversion.
8. **[Hermes automation](docs/hermes.md)** — discovery, isolated profile, skills and scheduler.
9. **[Security & cost controls](docs/security.md)** — bounded execution, Vaultwarden, provider reconciliation.
10. **[Webshop integration](docs/webshop.md)** — data contract, consent, purchase events and health.
11. **[Runbook](docs/runbook.md)** — bootstrap, acceptance gates, deployment/rollback and handoff.

Configuration examples are under `config/`; prompt templates under `prompts/`; pure, no-network validation library under `scripts/` with tests under `tests/`. All examples are dry-run only.

## Current status — checked 31 October 2026

- **Read [Creative Production System](docs/creative.md) first** for the exact proven image → Higgsfield Elements → Hermes CLI process, actual asset states, old/deprecated references, water physics and review gates.
- Higgsfield private project **AVELNA Creative Studio** exists, including five folders and **14 technically completed Elements**. The original bathroom is approved for **environment style only**; derived rooms, individual characters, and Stone references remain **candidates / internal product calibration**. The old `@AVELNA_StepWoman_01` Element still exists but is deprecated.
- Four **standalone StepWoman** studio images (Front, Back, Upper and Lower) are uploaded individually. Bathroom/Stone derived images are separately uploaded and registered.
- One **5.04-second** camera-motion technical proof was actually generated and placed in Higgsfield; this is neither the full hero ad nor proof of product water performance. Its exact prompt and results are in [PR #14](https://github.com/jens-mul/AVELNA/pull/14), still under review.
- Exact manufacturer SKU, source-photo rights, product physical test and commercial permission are **not confirmed**. No video has been approved as a water-absorption demonstration.
- **ChatGPT + founders author and approve the creative images/prompts; Hermes is CLI-first execution-only.** Existing upstream official Higgsfield skills are reused. A project-local router is in `.hermes/skills/avelna-creative-handoff/` after repository trust.
- No Meta ad or checkout integration has been activated by this documentation. The existing upgrade script deploys only the no-spend health service.

## Owner workflow

You build the webshop and fulfill orders. Together with ChatGPT you choose/approve the visual master. The Hermes agent receives *only approved assets*, reconstructs the product and prompt references through a private manifest, creates media when authorized, prepares/distributes ads within a fixed grant, and reports exceptions.

**Safety rule:** no one, including an AI agent, gets to infer a €200 spending grant from these documents. Provider costs, quotas, capabilities and permissions must be checked in the actual account before starting paid jobs.

## Research notes

See [source register](research/sources.md). Primary documentation, especially Higgsfield and Hermes, changes over time; reread actual remote tool schemas before implementation.

## One-command control-service upgrade

See [deploy/README.md](deploy/README.md) for the GitHub-main downloader, build/tests, old dedicated AVELNA service replacement, health and rollback. This only runs the **no-spend control health service**, not paid Hermes automation.
