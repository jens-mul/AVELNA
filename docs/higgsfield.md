# Higgsfield — CLI-only handoffcontract

Historische bron: [issue #11](https://github.com/jens-mul/AVELNA/issues/11). Het besluit blijft: eigenaar + ChatGPT kiezen een master, Hermes gebruikt alleen exact goedgekeurde referenties en bewaart promptversies. De eerdere MCP/library-, Elements-, Canvas- en sandbox-uitwerking is vervangen door een lokale, versievaste CLI-handoff; zij is geen actuele capability of vereiste.

## Bindende route
CLI-first projectarchitectuur; **CLI-only voor alle Higgsfield remote acties**, inclusief account/catalogus lezen, uploads, training, generatie, jobstatus en upscale. Gebruik uitsluitend de officiële `higgsfield` executable en laad `higgsfield-cli-operations`. Geen Higgsfield MCP, directe API, browsergeneratie of cloud-shellfallback. Ontbrekende CLI-capability betekent **BLOCKED**, niet een routewissel. Lokale planning, validatie, montage en QA blijven toegestaan. Meta Ads MCP verandert niet.

## Wat lokaal bekend is
CLI **v1.2.3** en lokale generic/model-command help zijn bekeken. De generieke mediaflags `--image-references` en `--start-image` zijn waargenomen; lokale paden worden bij daadwerkelijk CLI-gebruik automatisch geüpload. Een flag uit generic help bewijst geen geschiktheid voor een bepaald model/mode, accountrechten of kosten. Modelspecificatie, actuele quote, onafhankelijke grant en job-readback blijven **BLOCKED**. Geen geslaagde live CLI-auth of remote upload claimen.

Een quote met een lokaal mediapad kan al uploaden. Ook zonder generatie vereist dat rechten, privacytoestemming en een expliciete remote opdracht. Deze migratie en lokale demo doen **geen** CLI-uitvoering of providerrequest.

## Centrale contracten
- [Assetcontract](../config/asset-contract.json): generieke velden, rollen, hashes en approvalvoorwaarden.
- [Skillrouting](../config/skill-routing.json): projectgebonden routers en vereiste bestaande shared skills.
- [Prompts](../prompts/): de enige canonieke promptteksten; geen tweede promptlibrary in documentatie of provider-UI.
- [Assetbeheer](library-operating.md): private bestanden, versiebeheer en review.

`scripts/asset_registry.py` valideert lokaal SHA/path/approval; het is geen provideradapter en vertaalt geen aliassen naar provider-UUID-syntax. Een leesbare alias is een lokale registratiesleutel, geen mediaflag of modelinput.

`scripts/asset_handoff.py` levert een **prepared packet**, geen uitvoerbare generate-opdracht. Het legt de exacte prompttekst en SHA-256 vast, plus rolgebonden lokale assetpaden, hashes en generic-help-mediaflags. Model/mode/parametercompatibiliteit, quote, grant en job-readback worden niet uit deze binding afgeleid. Een geldige lokale binding is nog geen toestemming voor upload of betaalde productie.

## Werkvolgorde
1. Lees [creative](creative.md), plan en echte productfeiten; ontbrekende rechten/SKU blijven blocker.
2. Bewaar ontvangen master en echte productreferenties buiten git; leg rol, pad, SHA en rechten vast in een privémanifest volgens het centrale contract.
3. Menselijk akkoord bindt exacte versie/hash en gebruik; nieuwe output erft geen akkoord.
4. Voer eerst de synthetische demo of lokale manifestvalidatie uit volgens het [runbook](runbook.md).
5. Review packet en blockers; publiceer geen private stdout of bestanden in issues/CI-artifacts.
6. Alleen in een later expliciet geautoriseerd traject: via CLI account/model-schema en quote verifiëren, onafhankelijke grant en budgetreservering controleren; daarna pas upload/generatie.
7. Echte jobstatus, kosten en gedownloade output apart teruglezen; inhoud/metadata beoordelen. Timeout blijft onzeker tot reconciliatie; geen blinde retry.

## Acceptatiegrens
Lokaal gereed: exacte bronhashes, padbegrenzing, rechten-/approvalcontrole, reproduceerbare prompttekst en expliciete rolbinding. De demo bewijst alleen de lokale synthetische keten. Remote gereed vereist echte CLI-auth, modelschema, quote, grant, reservering en readbacks. Die zijn niet bewezen. Geen 4K-productie als setupcheck; AVELNA begint met 1080p binnen de €200-totaalgrens en het leveranciersverbod.
