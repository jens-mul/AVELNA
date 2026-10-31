> Source: [GitHub issue #5](https://github.com/jens-mul/AVELNA/issues/5). More recent supplier/product observations must carry dated evidence; do not infer competitor purchases from the Ad Library.

# Competitor Intelligence v1.0

Onderdeel van #3. Datum: 31 oktober 2026. Doel: concrete creatieve hypothesen en aanbodinzichten produceren, niet doen alsof openbare advertenties de winst van concurrenten onthullen.

## 1. Wat in dit onderzoek daadwerkelijk is bekeken
| Bron | Waarneming | Vertaling voor AVELNA | Niet bewezen |
|---|---|---|---|
| Dorai Current Bath Stone | Productpresentatie combineert badkamerstyling, steenachtige uitstraling, functionele uitleg en assortiments/bundellogica | Editorial sfeer + herkenbaar product + bruikbare productinformatie | Hun CAC, winst, AI-gebruik of winnend advertentieformaat |
| Sutera Stone Bath Mat | Directe functionele verkooptekst, probleem/oplossing, reviews en vergelijking met stoffen matten | Begrijpelijke categorie-uitleg en bezwaren beantwoorden, zonder onbewezen claims over te nemen | Dat onze SKU even goed presteert of dat hun advertenties winstgevend zijn |
| Minismus | Nederlandstalige categorie, maat/functionaliteit, service- en leveringsinformatie; gevonden 60×40-vermelding EUR 29,99 | Lokale prijs-/vertrouwensbenchmark; AVELNA's premiumprijs moet aantoonbaar waarde toevoegen | Dat de gevonden prijs onze actuele checkout inclusief verzending is |
| Audo, Ferm Living, Aesop | Bestaande inspiratierichting uit #1, geen nieuwe meting van hun advertentieresultaten | Visuele discipline en materiaalrust | Recht op hun beelden, typografie of productdesigns |

Productpagina's zijn onderzocht; **er is in deze sessie geen betrouwbare set individuele live Meta-ad-ID's en geen concurrent-accountperformance opgehaald**. De onderstaande ad-collector is een te activeren uitvoeringsprotocol. De agent moet `not_observed` gebruiken waar geen ad kon worden gelezen.

Primaire productbronnen:
- https://doraihome.com/products/bath-stone-mat-current
- https://sleepsutera.com/products/stone-bath-mat
- https://minismus.nl/
- https://minismus.nl/collections/diatomiet

Lees leveranciersclaims als claims, niet als onafhankelijke veiligheidsdata. Onderzoeksdatum en daadwerkelijke prijs-checkoutdatum zijn afzonderlijke velden.

## 2. Concurrentenlijst en zoekplan
Start met Dorai Home, Sutera en Minismus. Voeg maximaal drie inhoudelijk passende merken toe na verificatie van hun officiële domein en Meta-pagina. Bevestig page-ID via officiële site/profielkoppeling; naamgelijken zijn niet automatisch dezelfde onderneming.

Zoektermen:
- NL: stenen badmat, diatomiet badmat, sneldrogende badmat, design badmat.
- EN: stone bath mat, diatomaceous earth bath mat, bathroom essentials.
- DE: Stein Badematte, Diatomit Badematte.

Begin met NL, daarna DE/BE/EU voor vergelijkbare advertenties. US dient als creatieve referentie, niet als bron van Nederlandse media-kosten. Eén harde plaat is een andere constructie dan een oprolbare zachte diatomietmat; niet in dezelfde prijsgroep gooien.

## 3. Datatoegang: drie niveaus
**A. Officiële Meta Ad Library API** wanneer de eigen accounttoegang en voorwaarden dat toelaten. Deze toegang is niet automatisch hetzelfde als toegang tot je eigen advertentieaccount of Ads MCP. De officiële pagina noemt identity/developer-onboarding. De API ondersteunt onder meer advertenties die in EU/UK zijn uitgeleverd; maak geen aanname dat alle wereldwijde commerciële advertenties historisch beschikbaar zijn.

**B. Gewone openbare Ad Library** voor huidige advertenties en EU-archief, met de bestaande toegestane browsertool. Geen CAPTCHA-, login- of rate-limitomzeiling. Bij blokkade: record `blocked`, geen verzonnen advertentie.

**C. Officiële product-/landingpages** wanneer advertentiedata ontbreken. Dit levert positionering en aanbod op, maar telt niet als een geobserveerde ad.

Primaire bronnen:
- https://www.facebook.com/ads/library/api/
- https://www.facebook.com/ads/library/
- https://about.fb.com/news/2023/08/new-features-and-additional-transparency-measures-as-the-digital-services-act-comes-into-effect/

Meta's openbare documentatie onderscheidt bibliotheek-ID/content/looptijd van aanvullende reach/targetinggegevens. Aankopen, retouren en commerciële CAC van andere bedrijven zijn hier niet als een gecontroleerde winstmeting beschikbaar. Lang actief is hoogstens een selectiesignaal.

## 4. Collectie- en analyseprotocol
1. Leg officiële domeinen en pagina-ID's vast. Maximaal zes merken.
2. Verzamel per merk maximaal vijf relevante concepten; dedupliceer regionalisaties, crops en kleurvarianten. Maximaal dertig records voor de eerste sweep.
3. Leg alleen werkelijk gelezen velden vast. Onbekend = null; nooit 0 wanneer het onbekend is.
4. Analyseer: openingsbeeld, probleem/verlangen, productgrootte, camera, functie versus interieur, concrete claim, bewijssoort, prijs, CTA en landingspagina.
5. Classificeer een observatie als `product_page`, `ad_observed` of `performance_owned`. Alleen de laatste mag winstdata bevatten en betreft uitsluitend AVELNA's eigen account.
6. Cluster concepten: `room_upgrade`, `material_object`, `water_demo`, `care_ease`, `bundle`, `testimonial`, `discount`. Geen willekeurige vijftig scripts.
7. Schrijf drie hypothesen met bron-ID en onzekerheid. Kies één hypothese voor de eerstvolgende productie; rest blijft backlog.
8. Bewaar URLs, eigen samenvattingen, contenthashes en timestamps. Concurrentvideo's niet in de openbare repo herpubliceren. Screenshots indien rechtmatig nodig alleen beperkt en privé opslaan.

## 5. Machineleesbaar record
```json
{
  "record_id": "competitor-0001",
  "brand": null,
  "official_domain": null,
  "page_id": null,
  "ad_library_id": null,
  "source_type": "product_page",
  "source_url": null,
  "retrieved_at": null,
  "published_at": null,
  "first_observed_at": null,
  "last_observed_at": null,
  "reported_start_date": null,
  "status": "not_observed",
  "country_filter": "NL",
  "product_construction": null,
  "format": null,
  "duration_seconds": null,
  "hook_summary": null,
  "claim_summary": null,
  "offer_price": null,
  "offer_currency": null,
  "shipping_included": null,
  "landing_url": null,
  "concept_cluster": null,
  "performance_data_available": false,
  "source_hash": null,
  "limitations": []
}
```

Voor `ad_observed` zijn een daadwerkelijk gelezen bibliotheek-ID of directe ad-URL plus observatietijd verplicht. Geen geschatte impressies als exact bereik opslaan. Zet geen persoonsgegevens van commenters in dit bestand.

## 6. Van observatie naar experiment
**Hypothese 1:** een herkenbaar object in een rustige architecturale badkamer verkoopt de premiumprijs beter dan een losse witte packshot. Gebaseerd op Dorai's presentatie, niet bewezen bij AVELNA. Test met werkelijk betaalde orders en contributie.

**Hypothese 2:** premium klanten willen nog steeds weten hoe een harde mat voelt en wordt onderhouden. Gebruik concrete productinformatie en FAQ naast editorial beeld; test checkout-uitval en relevante supportvragen.

**Hypothese 3:** twee of drie perfect samenhangende assets kunnen goedkoper en consistenter zijn dan generatief volume. Productiekosten per bruikbaar asset en productmutaties meten; niet uitsluitend engagement.

Voor iedere hypothese: variabele, constante factoren, doelgroep, budget, primaire uitkomst, stopconditie en wat de test juist NIET kan bewijzen. Concurrenten zijn input voor ideeën; AVELNA-transacties zijn het bewijs voor AVELNA.

## 7. Cadans en kosten
Eerste sweep eenmalig. Daarna maandag/donderdag 07:30 Europe/Amsterdam, alleen veranderingen. Binnen dezelfde URL/contenthash geen nieuwe modelanalyse. Dagelijkse prijzencheck alleen voor drie relevante producten zolang een aanbodbeslissing openstaat. Geen 24/7 research-subagents.

De researchjob mag URLs lezen en conceptvoorstellen schrijven; hij mag geen kluis ontsluiten, contract afsluiten, leveranciers mailen, advertenties publiceren of budget wijzigen. Bestaand verbod uit #1 op leveranciersbenadering blijft van kracht.

## 8. Rechtmatig hergebruik
Higgsfield Ad Multiplier is bruikbaar voor **eigen of gelicentieerde** uitgangsadvertenties. Niet simpelweg andermans advertentie, audio, acteur of herkenbare branded set klonen. De officiële productpagina vermeldt dat de oorspronkelijke audio en montage behouden kunnen blijven; daarom moet de rechtencontrole vóór die workflow plaatsvinden.
Bron: https://higgsfield.ai/ad-multiplier .

## 9. Technisch bronregister — gecontroleerd versus runtime te bevestigen
| Bron | Onderbouwt | Nog te controleren bij installatie |
|---|---|---|
| https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent | Officiële Hermes-CLI-route, OAuth, referenties, credits, ontbreken native creditcap | Geïnstalleerde versie, betaald account, werkelijke tool/command schemas en beschikbare modellen |
| https://higgsfield.ai/creator-hub/help-center/integrations/what-is-higgsfield-mcp | Historische integratieresearch, geen actuele uitvoeringsroute | Higgsfield is nu uitsluitend CLI; zie [actueel contract](higgsfield.md) |
| https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | MCP-config, discovery en toolfiltering | Werkelijke Hermes-versie en schema; documentatie noemt soms andere namen |
| https://hermes-agent.nousresearch.com/docs/user-guide/profiles | Gescheiden config/state per profile | Hosting, identiteit en OS-isolatie |
| https://hermes-agent.nousresearch.com/docs/user-guide/features/cron | Planning, tijdzones, script-only jobs | Werkelijke cron-toolnaam en CLI-flags |
| https://hermes-agent.nousresearch.com/docs/user-guide/security | Beveiliging en bevoegdheden | Hard afgedwongen tool-/procesgrenzen |
| https://www.facebook.com/business/news/meta-ads-ai-connectors | Meta's eigen connector en business-regels | Account-rollout en huidige draft/paused/publicatie-flow |
| https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-overview | Meta-hosted endpoint `https://mcp.facebook.com/ads` | Toolmanifest, video-upload, preview en activatierechten |
| https://bitwarden.com/help/cli/ | CLI, serverconfig en unlocksessies | Vaultwarden-compatibiliteit van de bestaande installatie; geen aanname over Bitwarden Secrets Manager |
| https://autoriteitpersoonsgegevens.nl/themas/internet-slimme-apparaten/cookies/tracking-cookies | Toestemming voor trackingcookies/pixels | Feitelijke consent-/CAPI-configuratie van de webshop |

Sommige Meta-documentatie is achter login/blokkade en bronnen verschillen over draft versus paused. Niet oplossen door een derdepartijblog als API-contract te behandelen: ontdek de actuele tools en verifieer remote vóór write/launch. Geen operationele toolnamen uit het hoofd gebruiken.

## Acceptatie
Een valide bronregister, nul verzonnen ad-ID's, expliciet onderscheid tussen waarneming/hypothese/prestatie, en drie uitvoerbare creative briefs. Bestanden: `research/sources.md`, `research/competitors.jsonl`, `research/hypotheses.md`, `skills/avelna-research/SKILL.md`.