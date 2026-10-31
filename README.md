# AVELNA — AI-Native Brand & Growth System

**Architectuur:** CLI-first, prepare-only. **Higgsfield:** uitsluitend officiële CLI.
**Lancering:** Nederland, twee eigenaars; **€200 totaal**, geen uitgavemachtiging.

AVELNA bouwt een architecturaal, premium badkamermerk. De eerste verkooptest richt zich op één echte, geverifieerde harde Bath Stone-SKU; accessoires blijven onderzoek totdat hun eigen feiten en leverbaarheid vaststaan.

## Begin hier
1. [AGENTS.md](AGENTS.md) — bevoegdheden en expliciete projectskill-routing.
2. [Strategie](docs/strategy.md), [merk](docs/brand.md) en [product-QA](docs/product-qa.md).
3. [Creative](docs/creative.md) — plan, product-lock, 1080p-firsttest en QA.
4. [Higgsfield CLI-handoff](docs/higgsfield.md) en [assetbeheer](docs/library-operating.md).
5. [Concurrenten](docs/competitors.md), [growth](docs/growth.md) en [webshop](docs/webshop.md).
6. [Hermes-architectuur](docs/hermes.md), [security](docs/security.md), [runbook](docs/runbook.md) en [implementatie](docs/implementer-notes.md).

## Centrale bron en private uitvoering
- Alle canonieke prompts staan in [`prompts/`](prompts/); merkregels in [`config/brand.tokens.json`](config/brand.tokens.json).
- [`config/asset-contract.json`](config/asset-contract.json) definieert het generieke assetcontract; [`config/skill-routing.json`](config/skill-routing.json) de project-/shared-skillrouting.
- De vier projectskills onder [`skills/`](skills/) worden uitsluitend expliciet als bestand gelezen via AGENTS, niet persoonlijk geïnstalleerd. Bestaande gedeelde Higgsfield-skills worden op naam geladen; ontbreekt er één die nodig is, dan is die taak **BLOCKED**. Niet kopiëren of overschrijven.
- Echte assets, manifests, paden, rechtenbewijzen, account-ID's en grants blijven buiten de openbare repo. Lokale packetoutput is privé, ook wanneer die geen credentials bevat.

## Lokale no-spend verificatie
Vanuit de projectroot:
```sh
python3 -m unittest discover -s tests -v
python3 -m scripts.asset_handoff --demo
```
De demo gebruikt synthetische lokale fixtures en doorloopt de handoff zonder netwerk of Higgsfield CLI-uitvoering. Het packet bevat exacte prompttekst + hash en per rol een assetpad + hash + generieke CLI-mediaflag, **geen uitvoerbare generate-opdracht**. Eigen bestanden voorbereiden: zie het [runbook](docs/runbook.md). `--output` is optioneel en alleen voor private/ignored output; bij opslaan verschijnt uitsluitend een geredigeerde status op stdout. Zonder `--output` is de volledige packetoutput privé te behandelen.

Het uitgevoerde lokale test-/dry-runbewijs staat in [verification.md](docs/verification.md).

## Bewijsgrens en status
Repo, scripts, tests en documentatie bestaan; oude issueblokkades over initialisatie gelden niet meer. De CLI v1.2.3 en lokale generic/model-command help zijn bekeken. Generic help toont `--image-references` en `--start-image`; lokale paden kunnen bij werkelijk CLI-gebruik automatisch uploaden. Dat is **geen** bewijs van live CLI-auth, een modelspecifiek schema, upload, quote, grant, job-readback of paid readiness. Die providerstappen blijven **BLOCKED**. Geen 4K-resultaat bewezen; de eerste AVELNA-test blijft 1080p.

Geen provideractie, campagne, deployment, inkoop of leverancierscontact volgt uit een repowijziging. Exacte SKU, rechten, naamrecht, veiligheid, kostprijs en shop-readiness vereisen afzonderlijk bewijs. Eigenaars bouwen de shop, keuren product/aanbod/master goed en verzorgen fulfillment.

## Historie en deployment
[Issues #1–#11](https://github.com/jens-mul/AVELNA/issues) bewaren de besluitgeschiedenis; huidige repo-contracten zijn leidend. Het vroegere Higgsfield MCP/library-ontwerp is geen uitvoeringsroute. CLI-only geldt **alleen Higgsfield**; Meta's officiële Ads MCP blijft ongewijzigd.

Het [no-spend control-service upgradepad](deploy/README.md) bestaat, maar is geen live marketingruntime of toestemming om te deployen. Behoud persoonlijke Hermes/SSH en rollback. [Bronregister](research/sources.md).
