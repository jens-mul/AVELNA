> **ACTUELE UPDATE:** deze tekst is een vroege ontwerpnotitie. De vijf folders zijn inmiddels aangemaakt; 14 Higgsfield Elements bestaan. Voor bestaande assets, goedkeuringsniveaus, bronrechten, echte uploadstappen en CLI-handoff geldt [het actuele Creative Production System](creative.md). De eerdere uitspraak dat de uploadroute 'niet end-to-end getest' is, geldt niet meer voor de inmiddels bevestigde losse chatbeelden en cloud-sandbox uploads. Dat bewijst geen universele beschikbaarheid voor iedere bestandsreferentie.

# Asset approval & library — uitvoeringscontract

## Twee soorten beeld (niet verwisselen)
**Concept-master:** AI-scène om esthetiek te beslissen; hoeft geen exact fabrieksproduct te tonen. Alleen interne moodboards/campagnevoorbereiding totdat de vorm bevestigd is.
**Product-locked master:** combinatie met werkelijke, toegestane productreferenties, correct geometrisch en kleurgetrouw. Kan na rechten-/claim-/productgoedkeuring voor advertenties dienen.

## Asset-states
`draft -> candidate -> owner_approved -> verified_upload -> element_completed -> production_enabled -> archived`.

`owner_approved` vergt expliciet menselijk akkoord op exacte versie+sha256. Generatieve output krijgt niet automatisch dit akkoord. `verified_upload` vereist media-ID en zichtbare, teruggelezen folderplaatsing. `element_completed` vereist echte UUID en native status. Een `@...`-naam is slechts een mensvriendelijke alias.

## Geplande privéfolders
`00_source_reference`: echte fabriek/SKU-foto's en maten met gebruiksrechten.
`10_candidates`: AI-concepten; nooit direct voor betaalde commerciële claims.
`20_approved_masters`: exact goedgekeurde masterbeelden.
`30_creative_outputs`: afgeleide statics/videos per campaign_id.
`40_archived_versions`: vervangen assets en prompts.

Folders hoeven niet te worden aangemaakt vóór een gebruikersopdracht voor library-inrichting. Geen auto-publicatie naar Higgsfield Cinema/community.

## Gescheiden gegevens
- GitHub: publieke merkregels, prompttemplates, schema's en synthetische voorbeelden.
- Higgsfield privé: daadwerkelijke uploads/jobs/Elements/canvas.
- Private Hermes-runtime: element-UUID's, workspace/project/folder-ID's, cryptografische contenthash, rechtenbewijs, akkoord en accountbinding.
- Geen credentials, pre-signed URLs of klantdata in publieke git.

## Alias-resolutie in Hermes
1. Bepaal de werkelijke `SKU` en controleer de product-lock.
2. Lees privé-manifest: alias, echte `reference_element_id`, hash, rights, owner-approved, usage limits, current Element-status.
3. Lees live supported models of het gevalideerde capability-manifest; gebruik geen Element in een model dat het negeert.
4. Zet in de werkelijke MCP-prompt alle geldige `@AVELNA_...` aliases om naar `<<<UUID>>>`; geen blind global string replace van onbekende tags.
5. Check actuele quote en grant; verifieer dat outputs in de juiste map terechtkomen.
6. Re-read de job, credits, output en asset-QA; noteer de nieuwe versie. Nieuwe creatieve uitvoering vervangt nooit automatisch het approved master.

`scripts/asset_registry.py` is een offline validatie-/aliasresolver; het legt geen verbinding met Higgsfield en verleent geen betaalrechten.

## Promptversies
Een canonieke prompt bevat `id`, semantische versie, modelrol, expliciete productreferentie, positieve en negatieve constraints, aspecten/duurstijlen en bijbehorend goedgekeurd asset-hash. Canvas houdt de creatieve graph aan; GitHub houdt de tekstgeschiedenis aan. Iedere gegenereerde advertentie wordt herleidbaar naar beide.

## Acceptatie (nog niet gedraaid)
- Een correcte productreferentie geüpload en in private folder teruggelezen.
- Een `prop` Element met status completed teruggelezen.
- Een Canvas-node met prompt gemaakt zonder `run`, creditsaldo vóór/na vergeleken.
- Een alias-resolver dry-run met echte UUID en één ondersteund model.
- Een bewust gewijzigd asset-hash of ongeverifieerde rechten worden geweigerd.
- Een betaald experiment pas na aparte machtiging, budgetquote en stoppolicy.

## Uploadbrug: geen valse zekerheid
Connected ChatGPT image creation ≠ automatically accessible Higgsfield media ID.
Higgsfield's `media_upload_and_confirm` accepteert alleen een user-provided ChatGPT attachment; een ChatGPT-genereerd outputfile kan niet zonder bewezen route worden doorgestuurd. De andere route `media_upload -> sandbox_exec PUT -> media_confirm` geldt voor bestanden die in de Higgsfield-sandbox zijn gemaakt, niet zomaar elke lokale ChatGPT-path.
De implementatie moet één werkelijk eind-tot-eind geslaagde bridge-test doen, of de gebruiker laat een goedgekeurd bestand als bijlage toevoegen; pas dan de pipeline als automatisch geverifieerd markeren.
