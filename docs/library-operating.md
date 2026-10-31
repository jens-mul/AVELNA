# Asset approval & lokale library

## Twee soorten beeld
**Concept-master:** AI-scène voor esthetische keuzes, geen bewijs van een echt fabrieksproduct. Alleen interne voorbereiding zolang SKU/vorm niet vaststaat.

**Product-locked master:** werkelijk toegestane SKU-referenties, geometrie en kleur gecontroleerd. Pas na expliciete product-, rechten- en claimreview geschikt voor een commerciële toepassing.

## Centrale contracten, geen tweede schema
Lees [config/asset-contract.json](../config/asset-contract.json), [Higgsfield-handoff](higgsfield.md) en [prompts/](../prompts/). De JSON is leidend voor exacte veldnamen. Geen provider-UUID-resolutie, native Element-status of Canvas-opslag vereist. De historische [issue #11](https://github.com/jens-mul/AVELNA/issues/11) blijft besluitcontext, niet de actuele uitvoeringsinstructie.

## Privéopslag
Bewaar echte assets, manifests, rechtenbewijs, approvals, paden, accountbinding, grants en jobresultaten buiten de openbare repo. Een genegeerde lokale outputmap is alleen een vangnet; geen private bestanden publiceren via connectorwrites, logs, CI-artifacts of issues.

Eventuele lokale organisatie: `00_source_reference`, `10_candidates`, `20_approved_masters`, `30_creative_outputs`, `40_archived_versions`. Dit zijn lokale private categorieën, geen aangemaakte Higgsfield-projectfolders. Geen automatische communitypublicatie.

## Review en wijzigingen
1. Bepaal echte SKU en rol: productwaarheid, stijl/omgeving of goedgekeurd startbeeld zijn niet uitwisselbaar.
2. Bereken SHA-256 uit de echte bytes; controleer pad binnen de toegestane private asset-root en contractvelden met `scripts/asset_registry.py`.
3. Kandidaat blijft kandidaat totdat de eigenaar expliciet de exacte hash/versie en het gebruik goedkeurt. Validatie van approvalvelden is geen onafhankelijke grantverificatie.
4. Maak lokaal het prepared packet: exacte prompttekst + hash en per rol assetpad + hash + CLI-mediaflag. Zie [runbook](runbook.md) voor de twee modes.
5. Veranderde assetbytes, SKU, rechten, claim, aanbod of promptversie vereisen review van afhankelijke besluiten. Archiveer vorige geaccepteerde masters; overschrijf ze niet stilzwijgend.
6. Nieuwe generaties starten weer als kandidaat en krijgen eigen QA/provenance. Een succesvolle upload maakt iets niet goedgekeurd.

## Prompt en uploadgrens
Het private packet bevat ook product-SKU en een SHA-256 van de canoniek geserialiseerde invoermanifestgegevens voor herleidbaarheid. Dit is geen onafhankelijke goedkeuring of handtekening. Bytes/hash en extensie worden gecontroleerd, niet decodeerbaarheid of visuele productjuistheid.
Alle promptmasters staan in git onder `prompts/`; geen tekstduplicaten in provider-UI of projectskills. Het packet fixeert de gelezen exacte tekst/hash en de inputrollen. Geen aliasinjectie in prompttekst of uitvoerbare generate-opdracht.

Een ChatGPT-output is eerst een lokaal ontvangen bestand, niet automatisch een providerasset. CLI v1.2.3 generic help beschrijft mediaflags `--image-references`/`--start-image` die paden automatisch kunnen uploaden bij werkelijk gebruik. De lokale handoff uploadt niets. Modelspecificatie, auth, toestemming voor upload, quote, grant en job-readback blijven afzonderlijke **BLOCKED** providerstappen tot echt bewezen.

## Acceptatie
Test lokaal gewijzigde hashes, padontsnapping/symlinks, ontbrekende rechten of approval en verkeerde rolbinding. Een synthetische positieve demo bewijst geen productwaarheid, remote upload, betaalrecht of echte CLI-generatie. €200 totaal, geen leverancierscontact; eerste productieproef 1080p, geen onbewezen 4K-claim.
