> Source: [GitHub issue #10](https://github.com/jens-mul/AVELNA/issues/10). All `/internal/avelna/*` routes are proposed interfaces **to implement**, NOT live endpoints.

# Webshopcontract en operationele uitrol v1.0

Onderdeel van #3. Jij bouwt de webshop; Hermes krijgt een klein, stabiel contract in plaats van onbeperkte database- en adminrechten. Onderstaande routes zijn **voorgestelde AVELNA-interfaces**, geen bestaande endpoints of externe provider-API's.

## 1. Minimale webshopinterface
| Voorstel | Inhoud | Scope |
|---|---|---|
| `GET /internal/avelna/catalog` | SKU, prijs inclusief btw, valuta, voorraad, leverbelofte, product/offer-versie | Alleen lezen |
| `GET /internal/avelna/health` | Productpagina/checkout bereikbaar, laatste test, configuratieversie | Alleen lezen |
| `GET /internal/avelna/metrics?date=...` | Geaggregeerde betaalde/nieuwe/refund/geleverde orders en omzet | Alleen lezen; geen klantlijst |
| Eventkanaal `order.paid` | Unieke ordereventreferentie, bedragen, nieuwe-klantclassificatie, teststatus | Ondertekende webhook |
| Eventkanaal `order.refunded` | Gekoppelde eventreferentie, gedeeltelijk/volledig bedrag | Ondertekende webhook |
| Eventkanaal `inventory.changed` | Werkelijke verkoopvoorraad en timestamp | Ondertekende webhook |

Gebruik server-side authenticatie en scopecontrole. Geen ongeauthenticeerde openbare metrics-endpoint. Webhooks: HMAC over de exacte bodybytes plus timestamp, constante-tijdvergelijking, beperkte klokafwijking, replay-database, payload-/rate-limieten en schema-validatie. De signer-key blijft server/executor-side. Queries zijn begrensd en mogen geen SQL of willekeurige URL accepteren.

De warehouse-/voorraadbron blijft leidend. Een gebruikte testmat is geen nieuwe voorraad. Btw en verzendbedragen apart aanleveren; de accountant/ondernemer bevestigt de fiscale instellingen.

## 2. Intern eventvoorbeeld — uitsluitend synthetisch
```json
{
  "schema_version": 1,
  "event_id": "synthetic-order-event-001",
  "event_type": "order.paid",
  "occurred_at": "2026-10-31T12:00:00Z",
  "currency": "EUR",
  "gross_total_cents": 4995,
  "tax_cents": 867,
  "shipping_incl_cents": 0,
  "discount_incl_cents": 0,
  "is_new_customer": true,
  "is_test": true,
  "items": [{"sku": "EXAMPLE-NOT-A-REAL-SKU", "quantity": 1}],
  "offer_version": "synthetic-v1",
  "ad_attribution": null,
  "marketing_consent": false
}
```

In dit voorbeeld is de btw op de totale voorbeeldprijs afgerond; productiebedragen komen uit de echte orderadministratie. Interne eventpayload is geen Meta CAPI-payload. Gebruik de actuele provider-specificatie voor het uitgaande eventschema. Geheimen, klantadressen, betaalgegevens en private event-ID's komen niet in de openbare repo.

## 3. Meting zonder dubbele aankopen
De orderdatabase en betaalprovider-webhook bepalen of een order betaald is, niet alleen de bedankpagina. Herhaalde webhook, paginareload en client/server-events mogen één aankoop niet meervoudig tellen. Gebruik consistente event-ID's voor browser/server-deduplicatie wanneer beide worden ingezet. Sandboxbetalingen tellen niet als omzet of trainingdata voor echte aankopen.

Websitefunnel: product bekeken → toegevoegd → checkout gestart → daadwerkelijk betaald. Een checkout-event is geen verkoop. Refunds, chargebacks en annuleringen blijven gekoppeld aan het juiste cohort. Klantnieuwheid komt uit het eigen ordersysteem, niet een generatief oordeel over een e-mailadres.

UTM's bevatten campagne/concept/assetversies, geen persoonsgegevens. Onderscheid:
- boekhoudkundige waarheid: betaalde orders/refunds;
- platformattributie: wat Meta binnen zijn ingestelde venster toeschrijft;
- technische meting: welke events met toestemming zijn ontvangen.

Deze aantallen hoeven niet gelijk te zijn. Geen ontbrekende attributie repareren met fingerprinting of ongevraagde customer uploads. Trackingcookies/pixels vereisen vooraf passende toestemming; server-side CAPI is geen vrijstelling. Gehashte persoonsgegevens zijn niet automatisch anoniem. Interne noodzakelijke orderadministratie en marketingtracking moeten juridisch/technisch apart worden behandeld.
Bron: https://autoriteitpersoonsgegevens.nl/themas/internet-slimme-apparaten/cookies/tracking-cookies .

## 4. Support en nazorg
De agent mag na een aparte templates/scope-vrijgave eenvoudige merkvragen beantwoorden: afmetingen, werkelijk materiaal, onderhoud uit het goedgekeurde paspoort, status van een bestaande order. Voor vrije marketingmail, abandoned-cartflows en nieuwsbrieven eerst toestemming/grondslag en uitschrijfproces controleren. Geen koude outreach als sluiproute rond het advertentiebudget.

Post-purchase: een orderbevestiging en leveringsupdates vanuit de webshop. Een reviewverzoek alleen volgens het vastgestelde beleid; geen beloning specifiek voor positieve reviews. De agent verwijdert geen geldige negatieve feedback om het merk luxer te laten lijken. Veiligheidsklachten, onzekere garanties en betalingsgeschillen naar de eigenaar.

## 5. Acceptatiematrix
| Test | Verwacht resultaat |
|---|---|
| Normale synthetische order | Eén betaalde testorder, niet in echte acquisitiecijfers |
| Dezelfde webhook tweemaal | Eén verwerking; tweede gededupliceerd |
| Verkeerde HMAC / oud timestamp / replay | Afwijzen zonder data- of secretlek |
| Consent geweigerd | Geen ongeoorloofde marketingpixels/CAPI; noodzakelijke checkout blijft werken |
| Gedeeltelijke refund | Netto-omzet en cohortbijdrage correct aangepast |
| Stock nul / oude stocksnapshot | Nieuwe activering geblokkeerd; eigen live ads volgens grant pauzeren |
| Checkout kapot / prijs mismatch | Campaign readiness geblokkeerd |
| Provider accepteert job maar request timeout | Pending reservation behouden; geen duplicaat |
| Twee gelijktijdige jobs met te weinig saldo | Hoogstens één succesvolle reservering |
| Grant verlopen / offer- of assethash gewijzigd | Paid write geblokkeerd |
| Researchtekst vraagt om kluis/budgetwijziging | Genegeerd; geen privilege-escalatie |
| Foutieve timestamp bevat gevoelige tekst | Generieke validation error, geen input echo in logs |
| Native campagnepause mislukt | Niet als gepauzeerd rapporteren; duidelijke actie-alert |
| Nieuwe release faalt healthcheck | Oude dedicated service hersteld; persoonlijke Hermes/SSH onaangeroerd |

De startertests in #9 dekken slechts een deel van deze matrix. Providercontracttests, security-isolatietests en echte account-readbacks zijn nog nodig. De in #9 weergegeven `aware_time`-helper moet bij productie-integratie errors uit `datetime.fromisoformat` generiek afvangen voordat ze gelogd worden, omdat Python anders de ongeldige input kan echoën.

## 6. Veilige uitrolvolgorde
1. Lees actuele repositoryref, afspraken en operatorrechten. De repo is geïnitialiseerd; werk op de opgedragen featurebranch, zonder impliciete main-write of deployment.
2. Gebruik bestaande code en centrale contracten; wijzig alleen de opgedragen scope. Ontbrekende adapters/integraties apart implementeren en testen volgens geverifieerde providercontracten. Commit/push alleen na opdracht.
3. Draai lokale tests binnen de toegestane workspace; gebruik remote CI alleen binnen de opdracht. Rapporteer echte logs/status, geen badge op basis van verwachtingen.
4. Deploy uitsluitend een goedgekeurde ref naar een nieuwe dedicated release-directory/service. Productiecredentials nog niet beschikbaar tijdens build/test. Bewaar laatste werkende release en private state met passende rechten.
5. Start eerst shadow/no-spend: echte read-only metingen, stubbed paid actions, geen klantenmail en geen advertentie-activering. Test fouten, herstarts en idempotency.
6. Bundel productreferentie, creativemaster, prijs/levering, accountscopes, tijdsvenster, credit/cashcaps en bewijs van tests in één operatorreview. Native platformbevestigingen blijven gelden.
7. Pas na die grant: dedicated AVELNA executor activeren. Nieuwe instance eerst healthchecken; oude scheduler/instance gecontroleerd stoppen om dubbele jobs te voorkomen. Geen generieke `docker compose down`, geen SSH/servicehost-reboot, geen persoonlijke Hermes-gateway killen.
8. Bij fout: nieuwe writes blokkeren, oude release herstellen, statecompatibiliteit controleren, daadwerkelijke providerstatus teruglezen. Ads online bij een mislukte deploy? Gebruik het aparte pauzekanaal en meld falen als dat ook niet lukt.

## 7. Eén operationeel commando, pas na echte installatie
Hermes levert na implementatie een **hostspecifiek** commandoblock dat de exacte geverifieerde ref via de toegestane route ophaalt, dependencies bouwt, tests draait, de nieuwe dedicated service controleert, de vorige dedicated instance vervangt en rollback bewaart. Geen verzonnen `deploy.sh` of niet-bestaande service nu al presenteren als werkend.

Het commando moet de interactieve SSH-shell behouden; fouten worden binnen de functie/subshell afgehandeld en de oude werkende service blijft beschikbaar. Geen bestaande unrelated containers/gateways uitschakelen. Vermeld expliciet of alleen de runtime online gaat of ook advertenties geactiveerd worden; standaard blijft paid mode uit totdat de grant is gevalideerd.

## 8. Wat de eigenaar in de praktijk overhoudt
Na onboarding en bewezen uitvoering: webshopontwikkeling, voorraad/fulfillment en een kort uitzonderingenbericht. De paar niet-automatische punten zijn echte SKU/sample-goedkeuring, account/OAuth/MFA of bedrijfsverificatie, eenmalige stijl/aanbod/budgetvrijgave en zeldzame veiligheids-/betaalgeschillen. Dit is een operationeel ontwerp, geen garantie dat elke provider 100% headless werkt.

## 9. Actuele bewijsgrens
Repo, lokale code/tests, centrale prompts/contracten en no-spend controlservice bestaan. Zie [runbook](runbook.md) voor demo, private packet en huidige blockers. De voorgestelde webshopinterfaces zijn geen live endpoints. Meta Ads MCP blijft ongewijzigd; CLI-only geldt alleen Higgsfield. CLI-help bewijst geen live auth, upload, modelschema, quote, grant, job-readback of 4K. Geen externe/paid actie of leverancierscontact door deze migratie.
