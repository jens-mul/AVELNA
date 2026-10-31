# AVELNA runbook — lokaal voorbereiden, remote geblokkeerd

## Status en scope
De repository, lokale scripts/tests en no-spend controlservice bestaan. Actuele lokale testuitkomsten moeten uit uitvoering komen, niet uit historische issues. Higgsfield CLI v1.2.3 en lokale generic/model-command help zijn bekeken; dit bewijst geen live CLI-auth, upload, modelschema, quote, grant of job-readback. Geen campagne, betaalde productie, deployment of bewezen 4K-resultaat volgt daaruit.

## A — contracten en skills
1. Lees [AGENTS](../AGENTS.md), [strategie](strategy.md), [creative](creative.md), [Higgsfield](higgsfield.md) en [security](security.md).
2. Lees de passende repo-projectskill expliciet als bestand en volg [skill-routing.json](../config/skill-routing.json). Geen projectskill naar een persoonlijk profiel installeren.
3. Laad benodigde bestaande shared Higgsfield-skills op naam. Ontbrekend = **BLOCKED**; niet kopiëren/installeren/overschrijven.
4. Lees [asset-contract.json](../config/asset-contract.json). Bewaar echte media, manifests, approvals en grants buiten git.

## B — lokale synthetische end-to-end demo (geen credits)
Vanuit de projectroot:
```sh
python3 -m unittest discover -s tests -v
python3 -m scripts.asset_handoff --demo
```
De demo maakt/gebruikt synthetische lokale fixtures en doorloopt de lokale validator/handoff zonder netwerk of CLI-uitvoering. Controleer werkelijke exitstatus en packet: exacte prompttekst/hash, per rol assetpad/hash/CLI-mediaflag, providerblockers en geen uitvoerbare generate-opdracht. Demo-approval is fictief en verleent geen echte rechten of betaalmachtiging.

## C — eigen private bestanden voorbereiden
Onderstaande paden zijn uitsluitend placeholders; vervang ze lokaal, publiceer echte paden/packet niet:
```sh
python3 -m scripts.asset_handoff --manifest /PRIVATE/manifest.json --asset-root /PRIVATE/assets
```
Standaard stdout; behandel ook terminal-/agentlogs als privé. Gebruik voor echte inputs bij voorkeur `--output /PRIVATE/handoff.json`: het packet wordt exclusief met 0600 aangemaakt en stdout bevat alleen een geredigeerde status. Een bestaand outputbestand wordt niet overschreven. Geen publiek tracked doel, issues of CI-artifacts. De asset-root begrenst bronpaden; gewijzigde hash, ontbrekende rechten/approval of ongeldig pad moet worden geweigerd volgens het centrale contract.

Dit is uitsluitend een **prepared packet**, geen upload en geen uitvoerbare generate-opdracht. Exacte prompttekst/hash en mediaflag zijn lokale bindingen; de flags `--image-references`/`--start-image` zijn slechts in v1.2.3 generic help bevestigd. Hun echte gebruik kan paden auto-uploaden, ook bij quotering. Voer geen providercommando uit als onderdeel van deze lokale controle.

## D — latere providergates (nu BLOCKED)
Alle Higgsfield remote stappen uitsluitend via officiële CLI volgens `higgsfield-cli-operations`: echte auth/workspace/accountscope, modelspecifiek schema/mode, rechten en uploadtoestemming, actuele quote, onafhankelijke grant, budgetreservering en echte job-/kostenreadbacks. Bij ontbrekende capability stoppen, geen MCP/API/browserfallback. Timeout is onzeker tot reconciliatie; nooit blind opnieuw genereren.

Eerst 1080p-pilot/product-QA; 4K pas na afzonderlijke behoefte/route/budget/inspectie. De €200-totaalgrens en het leveranciersverbod blijven gelden.

## E — webshop en Meta (ongewijzigde route)
1. Eigenaars bouwen checkout/fulfillment; integreer [webshopcontract](webshop.md) pas met echte scopes.
2. Test synthetische betalingen, consent, dubbele events, refunds en voorraad. Bij voorraad/checkoutfout geen nieuwe activering; eigen campagnes alleen binnen grant pauzeren en teruglezen.
3. Meta's officiële Ads MCP blijft de onderzoeks-/integratieroute. Native draft/paused/preview/publicatiebevestiging werkelijk verifiëren, niet omzeilen.
4. Review bundelt SKU, rechten, masterhash, aanbod, account, periode, cash-/creditcaps en testbewijs. Geen automatische activering uit een packet.

## Acceptatie vóór live
- [ ] Echte SKU, veiligheid, beeldrechten, naamrecht en claims beoordeeld.
- [ ] Lokale negatieve/positieve handofftests en exacte hashes/rollen gecontroleerd.
- [ ] Echte CLI-auth, modelschema, upload, quote en provider-readbacks bewezen.
- [ ] Onafhankelijke grant, credentialscheiding, concurrency/idempotency en timeoutreconciliatie getest.
- [ ] Shop/consent/events en Meta paused/draft/preview/accountgrenzen bevestigd.
- [ ] Echte output inhoudelijk, technisch en audio beoordeeld; geen 4K-claim uit alleen dimensies.
- [ ] Afzonderlijk geautoriseerde deployment/health/rollback en beperkte livevrijgave.

## Deployment en herstel
[deploy/upgrade.sh](../deploy/upgrade.sh) en [deploy/README.md](../deploy/README.md) bestaan voor uitsluitend de loopback no-spend controlservice. Dit document voert ze niet uit en bewijst geen geïnstalleerde hostservice. Een betaalde Hermes/Higgsfield/Meta-runtime blijft een aparte beveiligde integratie. Bouw/test vóór vervanging van uitsluitend de dedicated AVELNA-service; bewaar vorige release/private state en rollback. Persoonlijke Hermes/SSH, andere containers en gateways nooit stoppen als shortcut.
