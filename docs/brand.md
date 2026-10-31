> Source: [GitHub issue #4](https://github.com/jens-mul/AVELNA/issues/4). Canonical artistic direction; colors and prompts are proposals until the owner approves the first master.

# Brand & Creative Bible v1.0

Onderdeel van #3. Bouw voort op #1: **Objects for considered living.** Dit is het creatieve besluitvoorstel, geen claim dat er al assets, een definitieve SKU of een geregistreerd merk zijn. De bredere Collection 01 / Bath blijft bestaan; het eerste betaalde experiment concentreert zich op één hero-product. Accessoires pas adverteren wanneer hun eigen feiten en beschikbaarheid zijn bevestigd.

## 1. Merkpositie
AVELNA verkoopt geen 'goedkope mat met een luxe filter', maar een zorgvuldig gepresenteerd functioneel badkamerobject. Het centrale koopargument is: **de badkamer voelt af zonder een verbouwing**. De functionele uitleg ondersteunt dat argument; het product mag niet onherkenbaar worden door lifestylebeelden.

Werknaam hero: `Bath Stone / 01`. De productnaam en prijs zijn voorstelvelden totdat de eigenaar/SKU-keuze ze vastlegt. Tone of voice: helder, rustig, concreet. Geen hoofdletters met uitroeptekens, 'revolutionair', countdowns, nepkeurmerken, verzonnen reviews of 'eigen ontwerp' bij een catalogusmodel.

Nederlandse campagnezin: **Rust, tot in het detail.** Alternatief voor een latere test: **De finishing touch voor je badkamer.** Engels blijft de merksignatuur, niet de taal van alle verkoopinformatie.

## 2. Vast stijlsysteem
| Onderdeel | Specificatie |
|---|---|
| Achtergrond | Chalk `#F3F0E9` |
| Tweede vlak | Sand `#D3C6B6` |
| Hoofdtekst | Charcoal `#292A27` |
| Steunkleur | Warm grey `#8B877F` |
| Spaarzaam accent | Olive grey `#858B7C`, maximaal circa 5% van een compositie |
| Materialen van de SET | Matte kalkpleister, licht natuursteen, geborsteld metaal, geweven katoen; maximaal twee dominante texturen |
| Productmateriaal | Uitsluitend het echte gekozen materiaal; de set mag natuursteen zijn zonder te zeggen dat de mat dat is |
| Licht | Groot zacht zijlicht, consistente richting linksboven, diepe maar niet dichtgelopen schaduwen |
| Compositie | Geometrische rust, één hero-object, natuurlijke schaal, geen showroom vol accessoires |
| Typografie | Eén goed leesbare sans voor UI/copy; eventueel één contrasterende editorial serif voor korte headings. Alleen correct gelicentieerde bestanden; licentie vastleggen |
| Logo | Eenvoudig AVELNA-woordmerk; niet in de video laten genereren maar deterministisch overleggen |

Kleuren zijn merkkleuren, **geen bevestigde productkleuren**. Een lichte AI-kleur mag nooit een niet-bestaande bestelvariant suggereren. Voor langere tekst contrast in de echte component controleren; de steunkleur is niet automatisch toegankelijk op chalk.

## 3. Wat 'premium' hier betekent
Geen generieke mansion, goudkranen, eindeloze slow motion of overdadige rook. Kies één geloofwaardige badkamer: rustige wand, normale douche of badrand, één handdoek. Werk met perspectief en schaduwen zodat de mat daadwerkelijk op de vloer ligt. Geen zwevend product, verbogen rechthoek, extra ribbels, verkeerde dikte of fictieve gravering.

Het product moet in een advertentie binnen de eerste 1,5 seconde identificeerbaar zijn. Voor een static beslaat het bij voorkeur ongeveer 30–45% van het beeld; dit is een compositierichtlijn, geen platformregel. Een extreme wide shot met een onzichtbare mat valt af.

## 4. Videografie
**Hoofdformaat:** 12 seconden, 9:16, 1080×1920, 24 fps, H.264/yuv420p. Afgeleide feed-export 4:5, 1080×1350. Geen betaalde 4K-productie nodig voor de eerste test.

Camerastijl: circa 35–50mm-equivalent voor ruimte/object; 85–100mm-equivalent voor gecontroleerde details. Geen extreem groothoek, whip pans, surrealistische productrotaties of dollyshots door de mat heen. Maximaal 2–3 shots. Micro-dolly of rustige laterale parallax, product vormvast. Tekst komt uit de editor, niet uit het generatiemodel. Lever ook zonder audio een begrijpelijke versie. Alleen eigen of aantoonbaar voor paid social gelicentieerde muziek; geen trending track aannemen als commercieel vrij.

Een eigen conservatieve tekstzone van circa 15% boven en 20% onder is slechts een werkmarge. De echte Meta-placement-preview beslist. Houd mat, prijs en CTA buiten de interface; controleer ook de 4:5-crop.

### Concept A — The finishing touch (eerste motion-ad)
| Tijd | Shot | Overlay |
|---|---|---|
| 0–2 s | De echte productvorm dominant in een rustige badkamer, direct zichtbaar | `Eén detail. Meer rust.` |
| 2–6 s | Subtiele camera/parallax; vloer en schaduw geven schaal | Geen extra tekst |
| 6–9 s | Detail van de echte rand/textuur; alleen referentiegetrouw | `AVELNA · Bath Stone / 01` |
| 9–12 s | Terug naar hero, rustige end card | Werkelijke prijs + leverbare CTA |

CTA bij voorraad: `Bekijk de Bath Stone`. CTA zonder voorraad: `Ontvang de lancering` + zichtbaar `Nog niet verkrijgbaar`. Prijs komt uit het aanbodmanifest; niet hard coderen in een modelprompt.

### Concept B — Editorial object (eerste static)
4:5. Dezelfde set, hetzelfde product en dezelfde boodschap als A. Mat duidelijk in beeld, één korte headline, kleine merknaam, prijs in de advertentietekst of leesbare overlay. Niet product én prijs én voordeel én garantie én reviewbadges op het beeld stapelen.

A en B in dezelfde kleine campagne is een **directionele vergelijking**, geen zuivere A/B-test: Meta verdeelt de impressies niet gegarandeerd gelijk. Niet claimen dat formaat B 'verliest' wanneer het nauwelijks werd uitgeleverd.

### Concept C — Material intelligence (pas na eerste signalen)
Macro, randafwerking en oppervlak. Een grafische absorptie-uitleg kan als illustratie, maar een gegenereerde waterabsorptiesnelheid is geen gemeten demonstratie. Gebruik bestaande toegestane leveranciersbeelden voor echte werking indien exact SKU-geldig; niemand hoeft een telefooncommercial te filmen. Ontbreekt bewijs, dan produceert de agent een esthetische advertentie zonder die specifieke performanceclaim.

## 5. Goedkope productie zonder productmutatie
1. Lees `product.json`, beeldrechten en de referentiehashes. Bestaande concept-renders uit #1 zijn inspiratie, niet het productbewijs.
2. Verzamel toegestane echte aanzichten: bovenkant, driekwart, rand, achterkant. Ontbreekt een hoek, beperk de camerakeuze; verzin de achterkant niet.
3. Maak een productcutout en masker. Genereer vooral de badkamerachtergrond en het lichtconcept. Plaats de productlaag gecontroleerd, met contactschaduw en correcte schaal. Een compositingstap vervangt geen verificatie van kleur/afmeting.
4. Produceer eerst twee lage-kosten hero-composities. Laat één stijlanker goedkeuren, niet ieder toekomstig cropje.
5. Maak vanuit de beste compositie één korte image-to-video-run met minimale camerabeweging. Als de mat verandert: verwerp; maximaal twee betaalde pogingen binnen de expliciete creditcap. Gebruik daarna een deterministische parallax/zoom-compositie op de bestaande productlaag als fallback.
6. Monteer, plaats tekst/prijs/logo en exporteer alle crops lokaal met bestaande tooling. Geen nieuwe generatie voor alleen nieuwe typografie of een andere CTA.
7. Hash bronbeelden en exports; leg model-ID, instellingen, referenties, kosten, rechten, review en campagnestatus vast.

Higgsfield-uitvoering is uitsluitend via de officiële CLI; zie [Higgsfield-contract](higgsfield.md). Geen MCP-discovery of provider-UI-fallback. Lokale help is geen model-/accountbewijs.

## 6. Centrale productieprompts
Alle canonieke teksten staan in [prompts/](../prompts/): [editorial-master](../prompts/editorial-master.md), [motion-master](../prompts/motion-master.md), [static-ad](../prompts/static-ad.md) en [creative-critic](../prompts/creative-critic.md). Deze merkmodule dupliceert ze niet.

## 7. Uitvoering en handoff
Lees [creative](creative.md) en [assetbeheer](library-operating.md). Een prepared packet fixeert exacte prompttekst/hash en rolgebonden assetpad/hash/mediaflag; het is geen uitvoerbaar generate-command, quote of grant.

## 8. Assetcontract en QA
Het generieke assetcontract staat uitsluitend in [config/asset-contract.json](../config/asset-contract.json). Leg echte bronhashes, rechten, exact versieakkoord en later echte provider-/kosten-/QA-provenance vast in private manifests/ledgers; geen tweede veldschema in deze module.

Hard reject: verkeerde SKU/geometrie, ongeautoriseerde beelden, fictieve prijs/voorraad, niet-goedgekeurde claim, verkeerde CTA-modus, onleesbare tekst, watermerk, niet-gecontroleerde muziek. Alleen daarna visuele beoordeling op rust, productherkenning, licht en consistentie. Een visiemodel kan fouten vinden maar bewijst productidentiteit niet; de eerste master blijft een korte menselijke review.

Wijzigingen aan prijs, product of claim maken bestaande goedkeuring ongeldig. Alleen crops/ondertitelvarianten binnen het goedgekeurde asset- en aanbodmanifest mogen later automatisch worden gepubliceerd.

## Acceptatie van echte productie
Twee productgetrouwe hero's, één 12s-master, één 4:5-static, placement-previews, bronrechtenregister en reproduceerbaar privémanifest. Repositorybestanden bestaan; dit is een outputdoel, geen claim dat beelden zijn geproduceerd. De eerste test blijft 1080p; geen bewezen 4K-resultaat.
