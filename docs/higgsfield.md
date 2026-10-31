> **ACTUELE UPDATE 31-10-2026:** de hieronder opgenomen tekst bevat een historisch voorstel uit de periode vóórdat de Higgsfield-library en 14 Elements daadwerkelijk zijn aangemaakt. De actuele, geverifieerde operationele waarheid en CLI-first rolverdeling staan in [docs/creative.md](creative.md) en [docs/creative-system/02-higgsfield-elements.md](creative-system/02-higgsfield-elements.md). Gebruik de oude '0 elements / geen project' vermeldingen **niet** meer als actuele status. Geen native Element-delete actie beschikbaar via deze connector.

> Source: [GitHub issue #11](https://github.com/jens-mul/AVELNA/issues/11). This is the chosen and tool-discovered workflow. **No Higgsfield project/Elements or generation was created by this repository commit.**

# AVELNA — Approved Assets & Prompts Pipeline v1.0

Dit is het ontwerp voor de vervolgworkflow **ChatGPT + eigenaar -> goedgekeurde visuele master -> Higgsfield library + Reference Elements -> Hermes video-/ad-productie**. Status op 31 oktober 2026: toolcapaciteiten gecontroleerd, **geen beelden gegenereerd, geen credits verbruikt, geen nieuwe Higgsfield-projecten/elements/brandkits gemaakt**. De gekoppelde private workspace toont bij AVELNA-projectzoekopdracht 0 resultaten, 0 Reference Elements en 0 Marketing Studio brandkits.

## Confirmed Higgsfield capabilities

- `create_project`, `create_folder`, `list_project_assets`, `attach_project_asset` laten een private media library met concrete project-, folder-, upload- en generation-ID's beheren.
- `media_upload` + `media_confirm` ondersteunen presigned upload van bestanden vanuit **Higgsfield sandbox_exec**; `media_upload_and_confirm` is nadrukkelijk **alleen voor een door de gebruiker in ChatGPT aangeleverde bijlage**.
- `create_reference_element` maakt een herbruikbaar **prop**, **environment** of **character** uit een daadwerkelijk bevestigde image-upload of voltooide Higgsfield-image-job. Alleen status `completed` is bruikbaar.
- Via `show_reference_elements` kan Hermes de namen en echte UUID's teruglezen.
- De gebruiker kan een element beschrijven als `@AVELNA_BathStone_01`. In de **MCP generatie-aanroep werkt die letterlijke @naam niet**. Daar moet `<<<element_uuid>>>` in `params.prompt` staan; Higgsfield injecteert de referentie en zet dit intern om naar `@element_name`. De ondersteunde modellen moeten bij runtime uit het modelcatalogus worden gecontroleerd. In de huidige tools ondersteunt dit o.a. Nano Banana 2/Pro, GPT Image 2, Seedream 4.5 / 5 lite / Cinema Studio Image en geselecteerde video-modellen. Kling 3.0 vereist óók een start frame; Elements vervangen dat niet.
- `canvas_create` + `canvas_add` kunnen prompts bewaren in generation nodes, **zonder generatie-credits**; `canvas_run` is een aparte betaalde/genererende actie. Ook tekstnodes kunnen prompts bevatten.
- `get_project_asset_prompt` kan bij bestaande generation placements de promptdetails teruglezen.
- Marketing Studio ondersteunt brand kits. Een `@...`-Element is geen prompt-library alias; promptversies moeten onafhankelijk worden beheerd.

## Designbesluit voor AVELNA

Richt **één** private Higgsfield media-projectstructuur in wanneer de eigenaar dat expliciet vraagt:
- `00_source_reference`: echte en rechten-gecontroleerde SKU-aanzichten, maten, onderzijde.
- `10_candidates`: conceptbeelden die nog niet zijn goedgekeurd.
- `20_approved_masters`: goedgekeurde hero/master beelden.
- `30_creative_outputs`: Higgsfield video en static afgeleiden.
- `40_archived_versions`: vervangen, niet meer actieve masters.

Brandtokens en de canonieke prompttemplates leven versiebeheerbaar in GitHub (documentatie staat voorlopig in #4, #9 en deze issue wegens lege repo). Higgsfield canvas bewaart werkprompts en generatieknopen voor creatieve inspectie. Elke prompt `prompt_id` verwijst naar versie/hash en toegestane productreferentie; niet alleen vrije tekst bij een beeld.

### Voorgestelde namen
- `@AVELNA_BathStone_01` — categorie `prop`; pas aanmaken als exact product bevestigd en beeldrechten bekend zijn.
- `@AVELNA_QuietBath_01` — categorie `environment`; een goedgekeurde, consistente virtuele badkamer.
- `@AVELNA_HeroMaster_01` — interne manifestalias voor een goedgekeurde master-asset, **niet automatisch een native Reference Element**.
- `AVELNA/hero/editorial/v1` — promptversie in GitHub + Higgsfield canvas; **niet native @-aanroepbaar**.

### Voorbeeld manifest: ID's komen UIT ECHTE TOOLRESULTATEN, nooit verzinnen
```json
{
  "alias": "@AVELNA_BathStone_01",
  "kind": "prop",
  "status": "awaiting_product_verification",
  "reference_element_id": null,
  "project_id": null,
  "folder_id": null,
  "source_media_id": null,
  "approved_asset_sha256": null,
  "product_sku": null,
  "rights_status": "unverified",
  "approved_by": null,
  "approved_at": null,
  "prompt_id": "AVELNA/hero/editorial/v1",
  "prompt_sha256": null
}
```

## Levenscyclus van één master

1. **Brief**: ChatGPT en eigenaar bepalen concept, gemeten/geverifieerde productfeiten, kleursysteem en gebruiksrechten.
2. **Genereren**: bij voorkeur een geschikte ChatGPT-beeldgenerator voor concepten zonder Higgsfield-credits; die output verschijnt NIET vanzelf in Higgsfield. Higgsfield-generaties worden alleen met expliciete creditmachtiging gestart. Een ChatGPT-gegenereerd bestand moet langs een echt werkende en geverifieerde uploadbridge; **deze bridge is nog niet end-to-end getest**. Als fallback kan de gebruiker een eigen goedgekeurde afbeelding opnieuw als ChatGPT-bijlage toevoegen, waarna de attachment-uploader daarvoor beschikbaar is.
3. **Review**: status `candidate`; eigenaar geeft expliciet akkoord op exacte afbeelding/versie. Een goedgekeurd AI-concept is nog geen juiste productreferentie voor een niet geverifieerde SKU.
4. **Library**: bevestigd image-job of upload aan de juiste projectfolder koppelen; bevestigde IDs, SHA en rechten vastleggen; remote teruglezen.
5. **Element**: voor een exact product of herbruikbare omgeving een reference element maken uit de bevestigde afbeelding, status `completed` afwachten. Bewaar de geretourneerde echte UUID met de leesbare alias.
6. **Prompt**: de exacte tekst inclusief negative constraints en asset-/model-/versie-ID opslaan in een Higgsfield canvas generation node (alleen opslaan, **niet** runnen), en als versiebeheerbare tekst in GitHub.
7. **Hermes consumeert**: leest manifest, verifieert SKU, reference status, goedkeuring en rechten; vervangt alias via lookup door `<<<UUID>>>` binnen generation prompt voor ondersteund model, schat kosten en vraagt/controleert budgetgrant vóór generatie.
8. **Na output**: controle op geometrie, kleuren, claims en versie; geen automatische vervanging van goedgekeurde master door een nieuwe generatie. Afgekeurde assets mogen niet als Referentie-Element in een betaalde campagne verschijnen.

## Veiligheid en kosten

- Uploaden/plaatsen/bewaren van media moet niet gelijkgesteld worden aan gratis **generatie**. Eerst prijzen checken; wanneer een mutate onverwacht kosten meldt, stoppen en toestemming vragen.
- De enige onderzochte workspace heeft 10 credits en specifieke free_gen vouchers; die vouchers zijn niet algemene gratis still-image generaties. Geen credituitgaven tijdens dit ontwerp.
- Geen publieke Cinema-publicatie; project standaard privé.
- De repo is openbaar: houd beeldrechtenbestanden, private thumbnails, echte accountidentifiers, geheime URLs en klantenbestand buiten GitHub. Een publiek aliaslabel kan wel; opslaglocaties en UUIDs kunnen in een privé operationeel manifest.
- Alles uit #1–#10 blijft gelden, vooral SKU-verificatie, budgetgrenzen, geen leverancier-outreach en gescheiden goedkeuring van uitgaven.

## Acceptatie door Hermes

1. Eén zichtbaar AVELNA-project in de correcte workspace, na expliciete projectaanmaakopdracht.
2. Eén opgevraagd en teruggelezen geüpload goedgekeurd beeld in `20_approved_masters`.
3. Een `completed` Reference Element met werkelijke ID en `@...`-naam.
4. Een canvas met promptversie en generation node die **niet** is gerund; saldo vóór/na controleren.
5. Een dry-run waarin Hermes de alias naar `<<<UUID>>>` vertaalt, maar géén creditjob start.
6. Later pas een gelimiteerde, expliciet geautoriseerde generation job, met prijscontrole en remote readback.
