# Webshopoverdracht — bouwen zonder opnieuw de chat te doorzoeken

Status: 8 november 2026. Productdossiers ondersteunen ontwerp en implementatie; zij zijn nog niet publicatiegereed. Start bij [README](README.md) en [collection-01.json](collection-01.json).

## Gegevens gebruiken

Lees de drie JSON-bestanden als interne redactionele records. Gebruik `product_id` als interne stabiele sleutel. `identity.listing_id` is een leverancierslisting, niet de uiteindelijke webshop-SKU. Publiceer geen leveranciersprijs, risicolog, bronverwijzing of ongecontroleerde claim doordat de hele JSON naar de frontend wordt doorgestuurd.

Het compacte fact-object heeft `value`, `status`, `source_ids` en `observed_on`. De toegestane statussen zijn beschreven in de catalogus-README. Een onbekende waarde is `null`. `publication.ready=false` en `checkout_enabled=false` moeten fail-closed blijven: niet automatisch wijzigen omdat de JSON syntactisch geldig is.

### Koppeling met bestaande config/product.example.json

| Bestaand veld | Herkomst uit dossier | Voorwaarde |
|---|---|---|
| sku | Later toe te kennen interne verkoop-SKU | Niet fabrikantmodel verzinnen |
| product_url | identity.product_url | Bestaande listing |
| supplier | facts.supplier_name.value | Bewaar bewijsstatus intern |
| dimensions_mm | Goedgekeurde samplematen | Niet package_size of unmapped dimensions |
| actual_color | Bevestigde variant/sample | Niet merkpalet |
| weight_grams | Gemeten nettogewicht | Niet bruto pakketmassa |
| landed_cost_cents_ex_recoverable_vat | commercial_observations.landed_cost_eur_minor_ex_recoverable_vat | Werkelijke kosten, geen USD-prijs zonder freight |
| published_moq | Goedgekeurde bestelling/variant | Geen conflict wegpoetsen |
| approved_claims | content_draft.approved_claims | Alleen claims met bewijs en expliciete vrijgave |
| saleable_stock | publication.saleable_stock | Aantal werkelijk verkoopbare artikelen; sample niet meetellen |

Dit is een mappingvoorstel, geen geïmplementeerde importadapter.

## Vast te bouwen structuur

- Homepage met één collectiebeeld en drie productkaarten; geen onbewezen klantenclaims.
- Eén collectiepagina en drie productpagina's, geen drie lege categorieën met onnodige filters.
- Materialen/onderhoud, over het merk en servicepagina's.
- Winkelmand/checkout met expliciete totale kosten, echte beschikbaarheid en gekozen levervoorwaarden.
- Eventuele bundel pas activeren wanneer beide producten beschikbaar zijn; voorraad per component afboeken.

### Herbruikbare productpagina

1. Werkelijke productnaam, variant, prijs inclusief toepasselijke belastingen, beschikbaarheid en leverinformatie.
2. Eigen of toegestane productfoto's, een schaalbeeld en indien beschikbaar een echte gebruiksvideo.
3. Wat zit er in de verpakking? Exacte onderdelen en hoeveelheden.
4. Materiaal, afmetingen, gewicht, installatie/pasvorm waar relevant.
5. Gebruik, onderhoud, beperkingen en veiligheidsinformatie.
6. Verzending, retouren, bereikbare klantenservice en bedrijfsgegevens.

Sfeercopy kan voorbereid worden; feitelijke productieclaims mogen niet uit conceptcopy worden afgeleid.

## Ontbrekende informatie, in één lijst

**Per product:** exacte variant; definitieve inhoud/maten; productveiligheidsinformatie en traceerbaarheid; juiste gebruiksinstructies; samplekwaliteit; rechten op exact beeld; actuele inkoop/transport/heffingen; retailprijs; verkoopbare voorraad.

**Voor de winkel:** definitieve merknaam en merkcheck; juridische verkoper en contactgegevens; btw-regime; betaalmethoden; verzendtarief en haalbare leverbelofte; retourproces; privacy/cookiekeuzes; support- en klachtenproces. Niet stellen dat bestaande KVK of belastingstatus gecontroleerd is: dat is niet gedaan in deze taak.

**Voor claims:** materiaal/certificaten niet automatisch overnemen; handwerkbewijs voor 'handgemaakt'; montagebewijs voor draaglast/ondergrond; productbewijs voor badmatwerking. Zie per product `do_not_publish_without_evidence`.

Deze punten blokkeren een definitieve publieke verkoopomgeving, niet het bouwen van de interface met afgeschermde conceptdata.

## Assets

Per artikel: totaalbeeld, relevante details, onderzijde/achterzijde, maatbeeld, inhoud verpakking en werkelijk gebruik. Voor de set: alle onderdelen afzonderlijk en samen. Voor de houder: montageonderdelen en echte flessen. Voor de mat: randen/onderzijde en werkelijke vorm. Bewaar een rechten- en goedkeuringsrecord; conceptbeelden onder `assets/concepts` zijn niet automatisch toegestaan productmateriaal.

## Technische acceptatie vóór livegang

Test minimaal mobiele productselectie, variant-/prijsconsistentie, betaling in testmodus, annuleren/refund, voorraadvermindering, uitverkochtgedrag, bundelvoorraad en foutmeldingen. Meet betaalde orders via unieke order-ID's en dedupliceer dubbele events. Tracking en toestemming moeten afzonderlijk worden ingericht; zet geen marketingtracking aan door deze documentatiecommit.

Een nieuw productdossier wijzigt geen draaiende app. De bestaande repository bevat een no-spend controlservice, geen bewezen live webshop. Deze taak levert geen nieuwe checkout of deployment.
