# Collection 01 — productdossiers

**Dossierdatum: 8 november 2026 · taal: Nederlands · status: voorbereiding, niet live.**

Dit is het centrale overdrachtspunt voor de drie huidige productkandidaten. Het consolideert de keuzes uit het projectgesprek en de beschikbare bronobservaties. Voor de huidige productselectie heeft dit dossier voorrang op de oudere, uitsluitend op de badmat gerichte scope in `docs/strategy.md`. Budget-, veiligheids- en toestemmingsregels uit `AGENTS.md` blijven gelden.

## Leesvolgorde

1. [Collectie en besluiten](collection-01.json).
2. Het JSON-dossier van het betreffende product; daarnaast het onderzoeksbestand.
3. [Bronregister](sources.json): herkomst, datum en beperkingen van iedere bron.
4. [Webshopoverdracht](BUILD-HANDOFF.md): wat de bouwer rechtstreeks kan voorbereiden en wat nog niet gepubliceerd mag worden.
5. [Vervolg: investering, advertenties en oplevering](NEXT-STEPS.md).

| Product | Gegevens voor de bouwer | Onderzoek en controles | Selectiestatus |
|---|---|---|---|
| Harde badmat, Zoso | [bath-stone.json](products/bath-stone.json) | [bath-stone.md](research/bath-stone.md) | Listing gelockt door gebruiker; MOQ 2; vervangt Yongye |
| Crèmekleurige douchehouder, Qimu | [shower-holder.json](products/shower-holder.json) | [shower-holder.md](research/shower-holder.md) | Listing expliciet gekozen door gebruiker |
| Beige Luca-wastafelset | [luca-sink-set.json](products/luca-sink-set.json) | [luca-sink-set.md](research/luca-sink-set.md) | Voorkeurskandidaat; geen inkoop- of verkoopvrijgave |

**Badmat-update 8 november, 16:27 UTC:** Zoso-listing 1601426633204 is gekozen. De aangeleverde screenshot toont EUR 26,92 Standard-verzending voor twee stuks naar Nederland, oftewel EUR 13,46 per mat bij dat aantal. Korting, btw en andere aantallen niet extrapoleren. Exacte bestelvariant blijft open; oude Yongye-conceptbeelden zijn geen Zoso-referentie.

[Markt, Marmoree en positionering](research/market-and-positioning.md) bevat aanvullend onderzoek. Concurrentgegevens zijn nooit automatisch eigenschappen van ons product.

## Wat 'vastgelegd' hier betekent

Een leverancierspagina bewijst wat de leverancier publiceert, niet dat het geleverde product onafhankelijk getest is. Een gekozen listing is evenmin een goedgekeurd sample. De JSON maakt daarom onderscheid tussen brongegevens, rekenaannames, conceptcopy en publicatievrijgave.

Alle productgegevens hebben, waar van toepassing, een `value`, `status`, `source_ids` en `observed_on`:

- `supplier_reported`: opgave van leverancier/platform; niet onafhankelijk productgetest.
- `repository_record`: eerder vastgelegd onderzoek, met de oorspronkelijke datum.
- `conflicted`: bronvelden spreken elkaar tegen; geen stilzwijgende keuze.
- `unknown`: nog onbekend; `value` is `null`, niet nul of een verzonnen schatting.

Selecties staan onder `selection`; aannames onder `planning_assumptions`; marketingvoorstellen onder `content_draft`. Geen van deze secties is onafhankelijk productbewijs. `source_ids` verwijst naar `sources.json`.

**Jouw rekenafspraak is behouden:** bij de als set aangeboden Luca-listing rekenen we één `piece` als één complete set. Die afspraak wordt niet opnieuw als discussiepunt geopend. Het aantal en de maten van de daadwerkelijk te leveren onderdelen moeten wel in de productinformatie komen. Bij de douchehouder betekent één stuk één houder, geen verzonnen accessoiresbundel.

## Datacontract

- Geld: gehele minor units met expliciete bronvaluta, bijvoorbeeld `1949` in USD = US$19,49 en `2692` in EUR = EUR 26,92. Geen stilzwijgende valutaomzetting.
- Leveranciersprijs, samplekosten, landed cost, verkoopprijs en advertentiekosten zijn afzonderlijke velden.
- Verzendbedragen horen bij een vastgelegd aantal, bestemming, dienst en waarneming. Een bedrag per stuk niet gebruiken voor een andere ordergrootte zonder nieuwe quote.
- `observed_on` is de datum van de inhoudelijke waarneming, niet automatisch de datum waarop deze dossiers zijn geschreven.
- `null` betekent onbekend; een lege `approved_claims`-lijst betekent dat nog geen verkoopclaims zijn vrijgegeven.
- Bestel-MOQ is niet hetzelfde als maatwerk-MOQ. Productietijd is niet de Nederlandse bezorgtijd. Bruto verpakkingsgewicht is niet nettogewicht.
- De product-ID's zijn **interne dossier-ID's**, geen verzonnen fabrikant-SKU's. Een fabrikantmodel wordt alleen ingevuld wanneer de bron het noemt.
- `commercial_observations` is interne research en mag niet integraal als publieke product-API worden aangeboden.
- De drie bestanden zijn dossiers versie 1.0.0, geen drop-in vervangers voor `config/product.example.json`.

## Eerlijke definitie van gereed

**Gereed voor ontwerp en technische voorbereiding:** collectie, bronlinks, rollen van de producten, datavelden, productpagina-opbouw en bewijsstatus zijn vastgelegd. De bouwer hoeft de eerdere chat niet door te zoeken.

**Nog niet gereed voor verkoop:** exacte variant, samples, samenstelling/veiligheidsinformatie, gebruiksinstructies, beeldrechten, voorraad, landed cost en goedgekeurde prijs/leverbelofte zijn niet compleet. Zie per product `open_items` en de gezamenlijke lijst in de overdracht. Geen website kan deze ontbrekende feiten eerlijk 'wegontwerpen'.

De volgende fase is het investeringsplan, daarna het advertentieplan. Deze dossiers machtigen geen bestelling, advertentie, leveranciersbericht, extra abonnement of merkclaim.
