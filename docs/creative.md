# AVELNA creative — projectgebonden productiecontract

Lees [merkregels](brand.md), [product-QA](product-qa.md), [Higgsfield-handoff](higgsfield.md) en [assetbeheer](library-operating.md). [Issue #4](https://github.com/jens-mul/AVELNA/issues/4) en [#11](https://github.com/jens-mul/AVELNA/issues/11) blijven historische bronnen; actuele repo-contracten gaan voor.

## Plan vóór productie
Quiet Architecture: herkenbaar echt product, rustige badkamer, zacht linksbovenlicht, correcte schaal en contactschaduw. Geen fictieve absorptie/slip/schimmelclaims, reviews, certificeringen, prijs of voorraad. Een ChatGPT-concept is geen geverifieerde SKU-foto.

1. Stel doel, doelgroep, één boodschap, CTA en leverbare verkoop-/interesselijstmodus vast.
2. Verzamel echte SKU-feiten, rechten en referentieaanzichten. Ontbrekende onderzijde niet laten verzinnen; beperk de camera.
3. Kies master met eigenaar; bind goedkeuring aan exacte bytes/hash. Alleen goedgekeurde product-locked inputs voor advertenties.
4. Plan twee hero-composities, één korte motion en één static uit dezelfde geaccepteerde master. Eerst de moeilijkste product-/bewegingsfout testen; geen batch vóór geslaagde pilot.
5. Maak lokaal het prepared packet. Providerstappen blijven geblokkeerd tot CLI-schema, quote, onafhankelijke grant en budgetreservering bewezen zijn.
6. Bij productvervorming: reject, gerichte herstelkeuze binnen goedgekeurde retrycap; anders deterministische parallax/compositing op de geaccepteerde productlaag. Geen steeds nieuwe productrenders.

## Formaat en QA
De **eerste AVELNA-test blijft 1080p**: motion circa 12 seconden, 9:16, 1080×1920, 24 fps; feed 4:5, 1080×1350. Gewenste export H.264/yuv420p, uitsluitend wanneer lokale encoder/decoder en echte output dit toelaten. Tekst, prijs, logo en CTA deterministisch monteren; muziek alleen met aantoonbare paid-socialrechten. Controleer Meta-placement-previews, geluid-uit begrip, tekstleesbaarheid en werkelijke CTA-modus.

Reject vóór esthetische rangschikking: verkeerde SKU/geometrie/kleur, zwevende randen, nieuwe groeven, misleidende werking/claim, onjuiste tekst/prijs/voorraad, ongeautoriseerde audio/beelden of watermerk. Beoordeel complete playback en risicoframes, niet alleen metadata. Een visiemodel helpt fouten vinden, maar vervangt de product-/eigenaarsreview niet.

4K is geen verplichte eerste test. Bij een later expliciet 4K-doel: laad `higgsfield-4k-delivery`, verifieer CLI-route en budget en onderscheid native 4K, reconstructie/upscale en gewone resize. Geen empirische 4K-kwaliteit of provideroutput is met een lokale demo bewezen.

## Centrale prompt- en assetbronnen
Gebruik de exacte versies in [prompts/](../prompts/): [editorial-master](../prompts/editorial-master.md), [motion-master](../prompts/motion-master.md), [static-ad](../prompts/static-ad.md), [creative-critic](../prompts/creative-critic.md). Geen kopieën in docs of skills. Generiek assetcontract: [asset-contract.json](../config/asset-contract.json). Privé assets/manifests/grants blijven erbuiten.

## Skillrouting
Lees projectskill [avelna-creative](../skills/avelna-creative/SKILL.md) expliciet als bestand, uitsluitend binnen dit project. Laad bestaande shared skills op naam: `higgsfield-production-planning`, `higgsfield-cli-operations`, `higgsfield-reference-continuity`, `higgsfield-ad-creative`, `higgsfield-4k-delivery` conform de centrale router; voor varianten/hergebruik ook `higgsfield-content-operations`. Deliverykennis laden verplicht geen 4K-productie en wijzigt de 1080p-firsttest niet. Geen persoonlijke skillinstallatie, kopie of overwrite; ontbrekende benodigde skill = **BLOCKED**.

## Kosten en bewijs
€200 totaal is geen grant; AI-pot €20, media €60, product/logistiek €90, reserve €30. Maximaal twee betaalde motionpogingen alleen binnen expliciet goedgekeurde scope en actuele quote. Geen leveranciersbenadering. De lokale demo bevat synthetische fixtures en voert geen netwerk- of CLI-call uit; packet is geen generate-opdracht. Live CLI-auth, upload, modelschema, quote, grant en job-readback zijn niet bewezen.
