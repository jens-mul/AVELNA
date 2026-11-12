# AVELNA — AI-Native Brand & Growth System

**Version:** 1.0 — 31 October 2026  
**Owners:** two founders, Netherlands  
**Status:** documentation and code prepared; no live campaign or paid integration implied.  
**Launch cash ceiling:** **€200 total** (not an authorization to spend).

AVELNA is an architecturally minimal, premium bathroom essentials brand. The first validated sale is a single real, hard diatomite Bath Stone SKU; subsequent accessories remain in the catalogue research pipeline.

## Collection 01 — actuele geselecteerde productlinks (12 november 2026)

De actuele collectiebronnen zijn vastgelegd in **[Collection 01: badmat, goudkleurige douchehoektray en frosted Longan-flessen](docs/collection-01-supplier-selection.md)**. De gouden tray is specifiek [Homedec HD-4590 / Alibaba #62481855179](https://www.alibaba.com/product-detail/Space-Aluminum-Wall-Mounted-Bathroom-Accessories_62481855179.html), niet GAIA of Tranjoy. Dit is een productselectie voor verdere validatie, geen bevestigde bestelklare SKU of veiligheidscertificatie. Oudere catalogusschema's zijn historische context.

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

## Current status

- Earlier research and decision history remain in [GitHub issues #1–#11](https://github.com/jens-mul/AVELNA/issues).
- Exact manufacturer SKU, approved rights, actual cost and regulatory readiness have **not** been confirmed.
- ChatGPT can ideate masters; uploading a ChatGPT-generated file into Higgsfield and attaching it to a project is **not yet tested end to end**.
- Higgsfield library, Elements and prompt canvas are supported by the connected tool surface but are **not created merely by this commit**.
- No Meta campaign, live spend, Hermes deployment, checkout integration or external communication is performed by repository changes.

## Owner workflow

You build the webshop and fulfill orders. Together with ChatGPT you choose/approve the visual master. The Hermes agent receives *only approved assets*, reconstructs the product and prompt references through a private manifest, creates media when authorized, prepares/distributes ads within a fixed grant, and reports exceptions.

**Safety rule:** no one, including an AI agent, gets to infer a €200 spending grant from these documents. Provider costs, quotas, capabilities and permissions must be checked in the actual account before starting paid jobs.

## Research notes

See [source register](research/sources.md). Primary documentation, especially Higgsfield and Hermes, changes over time; reread actual remote tool schemas before implementation.

## One-command control-service upgrade

See [deploy/README.md](deploy/README.md) for the GitHub-main downloader, build/tests, old dedicated AVELNA service replacement, health and rollback. This only runs the **no-spend control health service**, not paid Hermes automation.
