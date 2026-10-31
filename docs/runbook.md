# AVELNA Runbook — van main naar autonome marketing

## Feitelijke status 31 oktober 2026
GitHub main is door de eigenaar geautoriseerd en geïnitialiseerd. Onderzoeksdocs en offline veiligheidsbibliotheek zijn voorbereid. **Niet** geïnstalleerd: Hermes/Higgsfield/Meta koppeling op de doelhost, fysieke productcontrole, shopcontract of betaalexecutor. Geen deployment, ads of credits zijn door GitHub-commits gestart. Als deze status verandert, voeg echte refs, tests en account-probeverslagen toe.

## Operatie A — account- en toolinventarisatie (no spend)
1. Lees de hoofdbestanden op main, de bestaande issuebesluiten en GitHub-workflowstatus.
2. Gebruik bestaande, geïsoleerde Hermes-omgeving. Inventariseer CLI-versie/help, mcp/auth, Higgsfield workspace, project/folders/Elements, actuele saldo/quote, Meta account, mail scope, Vaultwarden resolver. Geen tokenwaarden loggen.
3. Schrijf privé capability-manifest (provider, werkelijke versie, toolmanifesthash, accountscope, read_probe, betaalregels, bewijs).
4. De verzamelde read-only toestand geeft nog geen toestemming om iets te kopen of te publiceren.

## Operatie B — master asset
1. Werkelijke productinformatie en beeldrechten in productpaspoort.
2. ChatGPT+eigenaar maken/keuren asset met ID + sha256.
3. Open of maak één privé Higgsfield-project na de betreffende opdracht; folders volgens docs/library-operating.md.
4. Uploadbridge testen; bevestigde ID teruglezen. Alleen approved exact productbeeld als `prop`, approved omgeving als `environment`. Het goedgekeurde `@naam` in privémanifest naar echte UUID mappen.
5. Canonieke prompts in git; werkversies in Higgsfield Canvas-node, niet automatisch runnen.
6. Hermes voert pas een kostenquotering + grantcheck uit voor generaties.

## Operatie C — commerce
1. Eigenaar bouwt de productpagina en privacyvriendelijke checkout.
2. Integreer alleen de minimale catalogus/health/metrics interface uit docs/webshop.md of een werkelijk geselecteerde backend.
3. Controleer testbetalingen, cookie-toestemming, dubbele webhooks, refunds en actuele voorraad. Reële klanten tellen pas bij betaalde orders.
4. Bij voorraad 0, mismatch, oude snapshot of checkoutfout: geen nieuwe ad-activatie; actieve eigen campagnes indien binnen bevoegdheid pauzeren.

## Operatie D — campagne
1. Maak assetpakket (bevestigde master, 12sec motion, static 4:5, prijs en CTA) en budgetvoorstel.
2. Maak een native paused/draft-campagne uitsluitend wanneer geautoriseerd en daadwerkelijke Meta-tool dit ondersteunt. Lees providerobject terug.
3. Human review: echte SKU, claims, juridische/retourinfo, account, bereik, looptijd en maximumbedrag. Operator geeft echte grant, platform kan extra expliciete publicatiebevestiging vragen.
4. Shadow: no-spend, fake payments, beperkingstests. Dan pas eenmalige limited live run.
5. Eén dagelijkse samenvatting; budget, spend, nieuwe betaalde klanten en bijdrage; geen automatische verhoging.

## Required acceptance
- [ ] Product/beeldrechten/brand/claim review
- [ ] Werkende Higgsfield-upload + private Element-readback
- [ ] Prompt Canvas opgeslagen zonder kredietkosten
- [ ] Alias vervangen door actuele element-ID in een dry-run
- [ ] Tools getest met kleinste nodige scopes; secrets blijven buiten agentcontext
- [ ] Concurrentenresearch met echte bronlinks, onbekend als null
- [ ] Shop/events/consent tests
- [ ] Budgetconcurrency/idempotency, grant expiry en timeout/reconciliation tests
- [ ] Campagnedraft/paused en preview/readback
- [ ] Native accountgrenzen en operatorgrant
- [ ] Deployment-health + rollback via aparte AVELNA-service

## Deployment en herstel
De repo is een **plan+offline toolkit**; er is bewust nog geen bestaande AVELNA-productieservice om af te schalen. Een werkend 'download -> build -> old off -> new on'-blok wordt pas hostspecifiek wanneer service, runtime, persistente state en healthchecks bekend zijn. Geen willekeurige `docker compose down`, reboot, globale Hermes-gateway-stop of SSH-afsluitende `exit 1`. Bouw eerst staging; verifieer health; switch alleen de gerichte AVELNA-service; behoud laatste werkende release en rollback.

Wanneer de eigenaar later een daadwerkelijke dienst implementeert, moet het bijbehorende deploymentcommit een **bestaand** `deploy/upgrade` entrypoint met geteste rollback opnemen; pas dan één commando publiceren. GitHub zelf online betekent niet dat er een marketingdaemon draait.

## Implemented no-spend control service

`scripts/control_server.py` is a loopback-only health endpoint. `deploy/upgrade.sh` downloads and verifies main, replaces ONLY the dedicated AVELNA control user-service after tests, and attempts rollback on health failure. Full Hermes/Higgsfield/Meta runtime remains separate and uninstalled. See `deploy/README.md`.
