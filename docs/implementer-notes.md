# Implementatienotities — lokale contracten, geen betaalexecutor

Historische bron: [issue #9](https://github.com/jens-mul/AVELNA/issues/9). De werkelijke bestanden in `scripts/`, `tests/` en `config/` vervangen de oude ingebedde codevoorbeelden. Geen duplicerende schema's, prompts of tests in deze notitie. De repository is geïnitialiseerd; initialisatie/materialisatie is geen open taak meer.

## Actuele verdeling
- [AGENTS.md](../AGENTS.md): bevoegdheden en expliciete file-read van vier repo-projectskills; geen persoonlijke installatie.
- [Assetcontract](../config/asset-contract.json) en [skillrouting](../config/skill-routing.json): centrale publieke generieke contracten.
- [Prompts](../prompts/) en [brandtokens](../config/brand.tokens.json): canonieke tekst en merkdata.
- `scripts/asset_registry.py`: lokale SHA/path/approvalvalidator, geen UUID-promptresolver of provideradapter.
- `scripts/asset_handoff.py`: synthetische demo of prepared packet uit private input, zonder netwerk/CLI-uitvoering en zonder uitvoerbaar generate-command.
- `scripts/preflight.py`: offline readiness/rekenwerk; geen machtiging tot uitgaven.
- `scripts/budget_ledger.py`: lokale ledger; aanwezigheid bewijst geen beveiligde live executor of providerreconciliatie.
- `scripts/control_server.py` en [deployinstructies](../deploy/README.md): no-spend healthservice, geen marketingruntime.

## Lokaal verifiëren
```sh
python3 -m unittest discover -s tests -v
python3 -m scripts.asset_handoff --demo
```
Eigen private input en optionele private output: zie [runbook](runbook.md). Rapporteer echte exitcodes/testuitkomsten; aanwezigheid van tests is niet hetzelfde als slagen. De demo bewijst alleen de lokale synthetische keten.

Het packet bewaart exacte prompttekst/hash en rolgebonden assetpad/hash/CLI-mediaflag uit generic help. Geen modelspecifieke uitvoerbaarheid claimen: v1.2.3 local help is geen auth-, quote-, upload- of jobbewijs. Reële provider model-schema/quote/grant/job-readback blijven **BLOCKED**.

## Nog nodig vóór betaalde autonomie
Beschermde onafhankelijke grantverificatie, OS-/credential-isolatie, scoped provideradapters via officiële Higgsfield CLI, echte schema-/quote- en jobreadbacks, kostenreconciliatie, webshop ingress/replay/consent en complete integratie-/security-/deploymenttests. Lokale ledger/tests bewijzen deze combinatie niet. Geen CLI-auth success of bewezen 4K-resultaat afleiden uit fixtures.

CLI-only geldt uitsluitend Higgsfield, niet Meta Ads MCP. Behoud €200 totaal, leveranciersverbod, 1080p-firsttest en persoonlijke Hermes/SSH. Providerwerk, installaties, commits en deployment volgen uitsluitend een afzonderlijk geldige opdracht.
