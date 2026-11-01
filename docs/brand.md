> Source: [GitHub issue #4](https://github.com/jens-mul/AVELNA/issues/4). **Override 2026-11-01:** the five brand HEX colors of **Palette 04 — Olive Mineral** were explicitly locked by the owner. See [the complete palette decision and implementation guide](brand-palette.md). The actual product, final logo, individual prompts and commercial masters require separate approvals.

# Brand & Creative Bible v1.1

Onderdeel van #3. Bouw voort op #1: **Objects for considered living.** Dit is het creatieve besluitvoorstel, geen claim dat er al assets, een definitieve SKU of een geregistreerd merk zijn. De bredere Collection 01 / Bath blijft bestaan; het eerste betaalde experiment concentreert zich op één hero-product. Accessoires pas adverteren wanneer hun eigen feiten en beschikbaarheid zijn bevestigd.

## 1. Merkpositie
AVELNA verkoopt geen 'goedkope mat met een luxe filter', maar een zorgvuldig gepresenteerd functioneel badkamerobject. Het centrale koopargument is: **de badkamer voelt af zonder een verbouwing**. De functionele uitleg ondersteunt dat argument; het product mag niet onherkenbaar worden door lifestylebeelden.

Werknaam hero: `Bath Stone / 01`. De productnaam en prijs zijn voorstelvelden totdat de eigenaar/SKU-keuze ze vastlegt. Tone of voice: helder, rustig, concreet. Geen hoofdletters met uitroeptekens, 'revolutionair', countdowns, nepkeurmerken, verzonnen reviews of 'eigen ontwerp' bij een catalogusmodel.

Nederlandse campagnezin: **Rust, tot in het detail.** Alternatief voor een latere test: **De finishing touch voor je badkamer.** Engels blijft de merksignatuur, niet de taal van alle verkoopinformatie.

## 2. Vast stijlsysteem

**Locked identity: Palette 04 — Olive Mineral, 2026-11-01.** [Gedetailleerde kleuren-, contrast-, toepassing- en governance-specificatie](brand-palette.md); exact machineleesbaar in [`config/brand.tokens.json`](../config/brand.tokens.json). Palette 03 — Sand & Linen is **uitsluitend de ondersteunende fotografische richting**, geen alternatief logo-/UI-palet.

| Onderdeel | Specificatie |
|---|---|
| Primaire achtergrond | Alabaster `#F5F2EC` — lichte, warme basis |
| Tweede vlak | Stone `#D4C9BC` — rustige panelen/oppervlakken |
| Zacht accent | Sage Grey `#9DA08E` — decoratieve, natuurlijke nuances |
| Herkenningsaccent | Olive Smoke `#7C806E` — klein, consequent terugkerend element; geen standaard kleine tekst |
| Logo, tekst, primaire CTA | Deep Mineral `#31332F` — donker contrast; op donkere vlakken Alabaster als tekst |
| Materialen van de SET | Matte kalkpleister, licht natuursteen, geborsteld metaal, geweven katoen; maximaal twee dominante texturen |
| Productmateriaal | Uitsluitend het echte gekozen materiaal; de set mag natuursteen zijn zonder te zeggen dat de mat dat is |
| Licht | Groot zacht zijlicht, consistente richting linksboven, diepe maar niet dichtgelopen schaduwen |
| Compositie | Geometrische rust, één hero-object, natuurlijke schaal, geen showroom vol accessoires |
| Typografie | Eén goed leesbare sans voor UI/copy; eventueel één contrasterende editorial serif voor korte headings. Alleen correct gelicentieerde bestanden; licentie vastleggen |
| Logo | Eenvoudig AVELNA-woordmerk; niet in de video laten genereren maar deterministisch overleggen |

De vijf exacte HEX-waarden zijn nu **goedgekeurde merkkleuren**, maar **geen bevestigde productkleuren**. De bestaande [goedgekeurde badkameromgeving](../assets/approved/README.md) verandert hierdoor niet, evenmin als de nog onbekende echte SKU. Een AI-kleur mag nooit een niet-bestaande bestelvariant suggereren. Voor gewone tekst: gebruik Deep Mineral op Alabaster/Stone of Alabaster op Deep Mineral. Sage Grey en Olive Smoke zijn **niet automatisch toegankelijk als kleine tekst op lichte vlakken**; zie de berekende contrasttabel in [brand-palette.md](brand-palette.md).

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

Higgsfield documenteert image/video, reference Elements, upscaling en assetbeheer. De officiële handleiding wijst Hermes op de CLI; credits gelden ook buiten de website. Bron: https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent . Exacte upload-/generatiecommando's pas gebruiken na lokale `--help` of MCP-discovery; niet raden.

## 6. Product-lock prompt (template, niet uitvoeren met ontbrekende referentie)
```text
Create an editorial bathroom campaign composition for AVELNA.
Use the uploaded and rights-cleared product reference {product_reference_id} as the exact product, not as loose inspiration.
Preserve its silhouette, edge profile, thickness, surface pattern, actual colour and dimensions relative to the room.
Set: a believable compact contemporary bathroom, matte chalk plaster, warm neutral floor, soft large-window side light from upper left, restrained architectural styling.
Composition: the bath mat is immediately recognisable and occupies roughly one third of the frame. Leave quiet space for later typography. Natural contact shadow, straight architectural lines.
Camera look: 50 mm equivalent, controlled perspective, subtle texture, no excessive blur on the product.
Generate no text, price, logo, labels, certifications or people. Do not add grooves, marbling, bevels, accessories, anti-slip features or water-performance effects that are absent from the source.
Output: {aspect_ratio}. This is an advertising set, not evidence of material or performance.
If the product cannot be preserved, generate the environment without it and return it for deterministic product compositing.
```

## 7. Motion prompt
```text
Animate the approved AVELNA hero composition {approved_frame_id} as a restrained editorial shot.
Duration {verified_model_duration}. Slow lateral camera drift; stable floor geometry and soft natural light.
The product must remain rigid and unchanged in outline, thickness, colour, texture, placement and scale. No bending, morphing, appearing grooves, changing room geometry, floating edges or new reflections.
No water absorption simulation, no hands, no people, no text, no voice and no copyrighted music.
Return the clean clip for external assembly and typography.
```

## 8. Assetcontract en QA
Ieder asset krijgt `asset_id`, `sku`, `concept_id`, `format`, `source_hashes`, `rights_status`, `model_id`, `cost_quote_id`, `actual_credits`, `created_at`, `copy_version`, `offer_version`, `qa_status`, `approved_by`, `output_sha256`.

Hard reject: verkeerde SKU/geometrie, ongeautoriseerde beelden, fictieve prijs/voorraad, niet-goedgekeurde claim, verkeerde CTA-modus, onleesbare tekst, watermerk, niet-gecontroleerde muziek. Alleen daarna visuele beoordeling op rust, productherkenning, licht en consistentie. Een visiemodel kan fouten vinden maar bewijst productidentiteit niet; de eerste master blijft een korte menselijke review.

Wijzigingen aan prijs, product of claim maken bestaande goedkeuring ongeldig. Alleen crops/ondertitelvarianten binnen het goedgekeurde asset- en aanbodmanifest mogen later automatisch worden gepubliceerd.

## Te materialiseren
`docs/brand.md`, `docs/creative.md`, `config/brand.tokens.json`, `prompts/hero.txt`, `prompts/motion.txt`, `schemas/asset.schema.json`, `skills/avelna-creative/SKILL.md`.

Acceptatie: twee productgetrouwe hero's, één 12s-master, één 4:5-static, placement-previews, bronrechtenregister en reproduceerbaar assetmanifest. Nog geen van deze beelden is met dit issue geproduceerd.