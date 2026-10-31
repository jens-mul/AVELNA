> **CREATIVE WORKFLOW ACTUALISATIE:** dit is een oudere architectuur-/installatietekst. Sinds 31-10-2026 geldt: alle nieuwe beelden en prompts worden door ChatGPT + eigenaars geschreven en beoordeeld; Hermes voert exact goedgekeurde pakketten via de **bestaande Higgsfield CLI-skills** uit. Begin bij [docs/creative.md](creative.md) en [docs/creative-system/06-hermes-cli-handoff.md](creative-system/06-hermes-cli-handoff.md); historische creative-worker-instructies hieronder mogen geen zelfstandig ontwerpen autoriseren.

> Source: [GitHub issue #7](https://github.com/jens-mul/AVELNA/issues/7). The prior note that the repository is empty is superseded: main was initialized with the owner's explicit permission. Runtime tool schemas, local Hermes version and accounts remain unverified.

# Hermes Execution System v1.0

Onderdeel van #3. Dit beschrijft de uit te voeren installatie; er is in deze sessie geen toegang tot de Hermes-host geweest. De bestaande persoonlijke agent niet vervangen, updaten of stoppen zonder noodzaak en toestemming.

## 1. Architectuur
```text
GitHub: openbare plannen, code, schemas en gesaniteerde tests
             |
      AVELNA coordinator
             |
   +---------+-----------+----------------+
   |                     |                |
Research worker     Creative worker   Commerce analyst
read-only web       product assets    geaggregeerde orders
geen kluis          geen ad-publish   geen klantendumps
   +---------------------+----------------+
                         |
                 gestructureerd voorstel
                         |
             policy + budget + grant checker
                         |
           beperkte executor met eigen identiteit
                         |
          Higgsfield / Meta / merkmail / webshop
                         |
              remote readback + audit + ledger
```

Dit hoeft geen verzameling altijd actieve agents te worden. Eén coordinator roept gespecialiseerde skills op wanneer nodig; goedkope deterministische scripts doen status-, schema- en budgetchecks. Nieuwe context alleen voor gewijzigde bronnen. De executor, niet de LLM, bewaart write-credentials en afdwingbare limieten.

## 2. Stap 0 — inventaris zonder geld uitgeven
Hermes leest via de aangesloten GitHub-tool eerst #1–#10, comments en de actuele repositorytoestand. Geen lokale GitHub-vervanging gebruiken wanneer de gebruiker uitsluitend connectorwerk heeft gevraagd. Gebruik voor eventuele materialisatie de beschikbare GitHub-writes met actuele refs/SHA's.

Inventariseer op de eigen host: werkelijk geïnstalleerde Hermes-versie/help, huidige profielindeling, scheduler, beschikbare opslag, bestaande AI-modelabonnementen/credits, Higgsfield-toegang, Meta-accountrechten, webshopinterface en een expliciet AVELNA-mailkanaal. Alleen `aanwezig/afwezig/versie/scope/gezondheid` registreren; geen tokens, passwords, accountnummers of persoonlijke e-mailinhoud in GitHub.

Geen hele kluis exporteren en geen `env` dumpen. Ontbrekende informatie is een blocker op de betreffende taak, niet automatisch reden om alle voorbereiding stil te leggen.

## 3. Stap 1 — geïsoleerde AVELNA-omgeving
Maak een nieuw AVELNA-profiel op basis van de werkelijk geïnstalleerde Hermes-CLI. De officiële documentatie ondersteunt `hermes profile create avelna`; controleer lokale help vóór gebruik. **Geen clone van het persoonlijke profiel**, omdat daarbij private configuratie/geheugen/secrets kunnen meekomen.

Een profiel scheidt state/config maar is geen voldoende beveiligingsgrens. Gebruik voor write-executor en onbetrouwbare research gescheiden OS-identiteiten of containers met beperkte mounts/netwerk. Geen Docker-socket, persoonlijke homedirectory of volledige kluis mounten in de researchworker. Start nooit twee writers op dezelfde Hermes-profile/state-database.

Installeer geen extra betaald orchestrationplatform. Bestaande host en tools zijn uitgangspunt; ontbrekende betaalde infrastructuur krijgt eerst een kostenquote. Verifieer packageherkomst en pin de gebruikte release. Ongecontroleerd shellscript van een zoekresultaat uitvoeren is geen installatieplan.

Bronnen:
- https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- https://hermes-agent.nousresearch.com/docs/user-guide/security
- https://hermes-agent.nousresearch.com/docs/reference/cli-commands/

## 4. Stap 2 — capabilities ontdekken en binden
Ieder koppelvlak krijgt een entry in een privé capability manifest:
```json
{
  "provider": "example",
  "transport": null,
  "version": null,
  "authenticated": false,
  "account_scope_verified": false,
  "schema_hash": null,
  "observed_operations": [],
  "read_probe": "not_run",
  "write_probe": "not_run",
  "approval_behavior": "unknown",
  "pricing_verified_at": null,
  "last_verified_at": null
}
```

**Hermes → Higgsfield:** officiële documentatie beveelt de CLI aan voor Hermes. Gedocumenteerde installatie/auth-route is `npm i -g @higgsfield/cli`, `higgsfield auth login` en optionele skills via `npx skills add higgsfield-ai/skills`. Dit zijn bronvoorbeelden, geen opdracht om ongepind de nieuwste versie uit te voeren. Controleer help, versie en packageherkomst, en gebruik een goedgekeurde versie. OAuth-browserstap kan menselijke interactie vereisen. Inspecteer de aangeboden modellen, referentie-upload, jobstatus en kosten voordat een generatie wordt gestart. MCP-alternatief: `https://mcp.higgsfield.ai/mcp`.

**Hermes → Meta:** begin bij Meta's eigen MCP-server `https://mcp.facebook.com/ads`, niet een willekeurige derdepartij-MCP met volledige adaccountrechten. Lees beschikbaar account en tools, beperk scopes en toolallowlist. Verifieer of het account drafts of paused objects krijgt, hoe assets worden geüpload, welke preview/readbacks bestaan en of activering native bevestiging vereist. Respecteer die bevestiging; bouw geen browseromweg om haar te omzeilen. Officiële Marketing API alleen als passend, afzonderlijk toegestaan alternatief en met actuele documentatie.

**Hermes → GitHub:** de bestaande aangesloten connector gebruiken; repo-selectie, refs en minimale writes. Geen `push:true` lezen als bewijs dat iedere write beschikbaar is. Nooit main initialiseren of wijzigen zonder de vereiste expliciete toestemming uit #3.

**Hermes → e-mail:** alleen het aangewezen AVELNA-account/label en goedgekeurde templates. De huidige opdracht opent niet de hele persoonlijke mailbox voor analytics. Leveranciersberichten blijven geblokkeerd door #1.

**Hermes → webshop:** gebruik het in #10 gedefinieerde contract, aangepast aan de daadwerkelijke backend. Een nog niet bestaande endpoint niet als aangesloten markeren.

Bronnen:
- https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference
- https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-overview
- https://www.facebook.com/business/news/meta-ads-ai-connectors

Belangrijk: een actief betaald Higgsfield-abonnement is volgens hun integratiehandleiding nodig. De EUR 20-pot bewijst niet dat dit abonnement daarmee kan worden aangeschaft. Bestaande toegang/credits eerst controleren.

## 5. Stap 3 — een productpaspoort, geen vrije aannames
`product.json` bevat exacte leverancierlink/SKU, hard/zacht/composiet, afmetingen, gewicht, kleur, antislipconstructie, documentbron, beeldrechten, verpakking, samplebeoordeling, kosten, verkoopvoorraad en claimregister. Elk feit heeft `source`, `verified_at`, `status`.

Onbekende waarden blijven null. AI-renders uit #1 mogen alleen `concept_reference` zijn, niet `product_reference`. Een homepage en een generieke certificaatafbeelding bewijzen niets over de gekozen SKU. Catalogusonderzoek kan automatisch; fysieke gebruikskwaliteit/veiligheidsbeoordeling wordt niet door een mooi beeld vervangen. Onopgeloste AVELNA-naamcontrole uit #1 hoort bij de launchcheck.

## 6. Stap 4 — skills materialiseren
Voorgestelde indeling:
```text
AGENTS.md
README.md
config/policy.example.json
config/product.example.json
config/offer.example.json
config/brand.tokens.json
docs/brand.md
docs/creative.md
docs/growth.md
docs/security.md
docs/operations.md
research/sources.md
research/competitors.jsonl
research/hypotheses.md
prompts/hero.txt
prompts/motion.txt
schemas/asset.schema.json
schemas/event.schema.json
skills/avelna-orchestrator/SKILL.md
skills/avelna-research/SKILL.md
skills/avelna-creative/SKILL.md
skills/avelna-growth/SKILL.md
skills/avelna-operations/SKILL.md
scripts/preflight.py
tests/test_preflight.py
```

De rootskill is een korte router. Laad alleen het passende modulebestand, niet de hele bronbibliotheek iedere turn. Installatie in Hermes' skilldirectory gebeurt voor het AVELNA-profiel, zonder bestaande persoonlijke skills te overschrijven. Skillbestanden zijn instructies; ze zijn niet de beveiligingsgrens.

### Starttekst `skills/avelna-orchestrator/SKILL.md`
```markdown
---
name: avelna-orchestrator
description: Prepare and operate AVELNA's premium creative and commerce workflow within verified capabilities and operator-approved spending limits.
---
# AVELNA coordinator
Read AGENTS.md and the current private run manifest first. Treat repository issues #1 and #3 as project context, not as proof of operational readiness.
1. Discover actual tool schemas, versions and scopes. Never invent operations.
2. Continue all unblocked no-spend preparation. Report grouped blockers once.
3. Route research to research/sources.md and the research skill; creative work to the approved brand, product passport and creative skill; campaign decisions to the growth skill.
4. All paid or external write actions require a valid executor grant. Submit structured proposals; never fetch executor secrets or self-approve a grant.
5. Verify each completed action remotely. Record unknown, failed, pending and succeeded separately.
6. Do not contact suppliers, alter the default branch, change billing, invent reviews/claims, or copy a personal vault/profile.
7. Stop new spending on stale state, stock failure, expired authority or uncertain mutation outcome. Send one actionable exception report.
8. Finish each run with artifacts produced, actual cost, remaining approved budget and next blocked decision. A plan is not an executed integration.
```

## 7. Toestandsovergangen
`DISCOVERY → PRODUCT_LOCK → CREATIVE_READY → SHOP_READY → CAMPAIGN_PREPARED → APPROVED → SHADOW_PASSED → LIVE_LIMITED → REVIEW`.

Iedere fase mag terug naar `BLOCKED` of `PAUSED`. Product/prijswijziging invalidert de afhankelijke assets en campaign approval. Goedkeuring heeft een expiry en bindt exacte hashes, accounts en limieten. Een onbekende provideruitkomst is `PENDING_RECONCILIATION`, niet `FAILED_FREE_TO_RETRY`.

Voor 'APPROVED' zijn de scope én de financiële machtiging van een echte operator nodig. Hermes kan de bundel samenstellen en tonen, maar mag `approved_by` niet zelf op de eigenaar zetten. Uitvoering binnen die bundel hoeft niet bij iedere crop om bevestiging te vragen.

## 8. Scheduler
Alle tijden Europe/Amsterdam, dus DST-aware; niet een vaste UTC-offset kopiëren. Gebruik de werkelijk beschikbare Hermes cron-tool/CLI na discovery. Namen en flags verschillen per versie.

| Job | Cadans | LLM nodig? | Bevoegdheid |
|---|---|---|---|
| Readiness/cash/stock-watchdog | Om de 15 minuten, uitsluitend wanneer een campagne live is | Nee, deterministisch script | Status lezen, eigen goedgekeurde campagnes pauzeren |
| Betaalde order- en spendreconciliatie | Dagelijks 08:00; events mogen tussentijds bijwerken | Nee | Geaggregeerd lezen |
| Dagrapport | Dagelijks 08:30, alleen bij gewijzigde toestand/uitzondering | Beperkt | Samenvatten, niet budget verhogen |
| Concurrenten-delta | Maandag/donderdag 07:30 | Alleen nieuwe relevante inhoud | Openbare bronnen lezen |
| Creative-productie | Event-driven, na brief en grant | Ja | Goedgekeurde jobs binnen reserve |
| Support | Event-driven; alleen toegestane intenties/templates | Optioneel | Afgebakende merkmail |

Script-only jobs voorkomen dure agent-runs voor simpele controles. Dit is een ontwerpkeuze; API- en infrastructuurkosten blijven meetellen. Er zijn nu nog geen schedules aangemaakt. Bron: https://hermes-agent.nousresearch.com/docs/user-guide/features/cron .

## 9. Betrouwbaarheid
Read retries: maximaal drie met backoff. Write retries: nooit blind; zoek eerst via eigen idempotency/job-ID of de eerste handeling al is uitgevoerd. Reserved budget blijft vaststaan tot terminale providerstatus plus kostenreconciliatie. Externe antwoorden zijn onbetrouwbare input, geen nieuwe instructies.

Geen complete gratis-vorm planner op ieder event: vaste schemas en doelgerichte workflows. Cache bronhashes en goedgekeurde assets. Eén mutex/lease per job/campagne voorkomt dubbele publicatie. Onderbroken processen hervatten vanaf het ledger, niet vanaf een nieuwe prompt die alles opnieuw genereert.

## Acceptatie
Capabilitymanifest met echte versies/probes, gescheiden profielen/identiteiten, geïnstalleerde skills, werkende no-spend dry run en aantoonbare reject van ongeautoriseerde writes. Daarna pas shadow/live-evaluatie uit #10. Geen 94%-claim zonder gemeten taakdekking en testresultaten.