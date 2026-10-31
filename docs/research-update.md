# Onderzoeksupdate — 31 oktober 2026

Deze aanvullende bevindingen zijn gecontroleerd via publieke primaire documentatie én de werkelijk geadverteerde capabilities van de gekoppelde Higgsfield-tools. Er zijn geen campagnes of generaties gestart. Mogelijkheden kunnen per account verschillen; bij uitvoering opnieuw ontdekken.

## Higgsfield / ChatGPT / Hermes
- Via de gekoppelde Higgsfield-tools kunnen media in een project/folder worden geplaatst (`create_project`, `create_folder`, `media_upload`/`media_confirm`, `attach_project_asset`), bestaande assets worden teruggelezen en `create_reference_element` kan een herbruikbaar `prop` of `environment` maken uit een bevestigde image input/job. Alleen `completed`-elementen gebruiken.
- De gebruiksvriendelijke referentie heet bijvoorbeeld `@AVELNA_BathStone_01`. Bij de verbonden toolgeneratie hoort daar in de daadwerkelijke prompt een `<<<UUID>>>` bij: de backend voegt vervolgens de Element-referentie toe en vertaalt naar een leesbare @-naam. Letterlijk @ zonder ID is géén gegarandeerde MCP-generatiemethode. Niet ieder model ondersteunt Elements; voor Kling 3.0 is bovendien een startafbeelding vereist volgens de actuele toolbeschrijving.
- Canvas bewaart prompt-/generatienodes zonder dat de generatie wordt uitgevoerd. Uitvoeren via `canvas_run` kan credits kosten. Promptmasters worden daarnaast in deze repository geversioneerd; de gekoppelde canvas houdt de interactieve versie bij.
- ChatGPT-beeldgeneratie besteedt niet automatisch Higgsfield-credits. Automatisch uploaden van de gegenereerde ChatGPT-uitvoer naar Higgsfield is **niet end-to-end geverifieerd**: een gebruikersbijlage heeft een eigen uploadroute; zelfgemaakte bestanden vanuit de Higgsfield sandbox volgen een andere presigned-uploadroute. Niemand mag een project-asset claimen zonder bevestigd media-ID + teruglezing.
- De laatst uitgelezen privéworkspace had 10 credits, free plan, specifieke free-generation grants, een nog niet actieve free trial, géén AVELNA-project, elementen of brandkits. Dit is een momentopname, geen accountgarantie. Higgsfield zegt in algemene documentatie dat MCP-generatie credits kost; het huidige account kan specifieke uitzonderingen melden. Quote + saldo + exacte free-grant zijn bij iedere uitvoering leidend. In de algemene documentatie is geen native harde creditcap beschikbaar.

Primaire documenten:
- https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent
- https://higgsfield.ai/creator-hub/help-center/integrations/what-is-higgsfield-mcp
- https://higgsfield.ai/creator-hub/help-center/tools/how-do-i-use-canvas
- https://higgsfield.ai/creator-hub/changelog

## Hermes
Hermes heeft gescheiden profielen, native MCP-discovery, OAuth-configuratie en cron/scheduled jobs. **Een profiel is geen OS-beveiligingsgrens**: sandbox/process privileges blijven nodig. Gebruik alleen lokaal gedocumenteerde toolnamen en daadwerkelijk ontdekte schema's.
- https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference
- https://hermes-agent.nousresearch.com/docs/user-guide/features/cron
- https://hermes-agent.nousresearch.com/docs/user-guide/security

## Meta Ads
Meta heeft sinds april 2026 een eigen Ads MCP, met uitbreiding van rechten en businessregels in juli en verdere werkprocessen in oktober. Officieel endpoint: `https://mcp.facebook.com/ads`. Toegankelijke read/write acties en publicatiebevestiging moeten in het échte advertentieaccount worden vastgesteld. Geen third-party MCP installeren met brede rechten alleen omdat die meer functies claimt. Een geblokkeerde/beta-beperkte Meta-login is geen reden om automatisch via browserovername te activeren.
- https://www.facebook.com/business/news/meta-ads-ai-connectors
- https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-overview

## Advertentieonderzoek en economie
Triple Whale's rapport **17 aug 2026**, met data aug 2025–jul 2026 en meer dan 40.000 merken, noemt voor Home & Garden mediane Meta-CPA **$47,93** en mediane CVR **1,24%**. Dit zijn brede benchmarks, géén kosten voor de Nederlandse stenen badmat en geen voorspelling voor AVELNA. De €7–€10 CAC uit een vroege chat was een doel, niet gemeten.
- https://www.triplewhale.com/blog/facebook-ads-benchmarks

Productpositionering:
- Dorai laat premium badkamerstyling + echte productdetails, materiaal, maten, gebruik en bundellogica zien: https://doraihome.com/products/bath-stone-mat-current
- Sutera presenteert functie, garanties en reviews sterk; hun eigen claims (60 sec, 5 jaar, antimicrobieel) mogen niet voor AVELNA worden overgenomen: https://sleepsutera.com/products/stone-bath-mat
- Meta Ad Library biedt creatieve observaties, maar géén betrouwbare concurrent-CAC of winst. Registreer alleen werkelijk geobserveerde advertentie-ID's: https://www.facebook.com/ads/library/

## Nederlandse verplichtingen
ACM beschrijft informatieplichten en betaalmogelijkheden; volledige vooruitbetaling mag niet de enige optie zijn bij te leveren goederen. AP vereist vooraf geldige toestemming voor trackingtechnieken. Gebruikersmail en consent blijven gescheiden van technische orderadministratie.
- https://www.acm.nl/nl/verkoop-aan-consumenten/de-koop-sluiten/betaalmogelijkheden-aanbieden
- https://autoriteitpersoonsgegevens.nl/themas/internet-slimme-apparaten/cookies/tracking-cookies

## Open punten
Werkelijke Alibaba-checkout/all-in-kostprijs per SKU, materiaalsamenstelling, slip/stabiliteit, traceerbaarheid, productbeeldrechten, AVELNA merknaamrecht, Hermes accountconfig, Meta accountscopes, shopkoppeling, uploadbrug en echte advertentie-CAC zijn niet bevestigd. Geen dure uitvoering als oplossing voor een ontbrekend feit.
