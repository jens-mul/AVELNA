# CLI-handoff: lokaal verificatiebewijs

Deze verificatie betreft de CLI-first architectuur met uitsluitend CLI voor Higgsfield, niet een actieve providerverbinding of betaalde productierun.

## Uitgevoerd
- Python 3.11.15: 45 tests geslaagd; ResourceWarning als fout en unraisable-fouten verzameld: [].
- Python 3.14.8: 45 tests geslaagd; ResourceWarning als fout en unraisable-fouten verzameld: [].
- Python compileall geslaagd; git diff --check schoon; JSON-contracten en relatieve documentatielinks gecontroleerd.
- Baseline was 27 functioneel geslaagde tests met resourcewaarschuwingen. De ledger sluit nu op succes én fout, behoudt commit/rollback; de HTTPError-response wordt gesloten.
- De tests blokkeren shell/netwerk tijdens handoff en demo. Er zijn geen providerclients in de handoffmodules. De generieke CLI-mediaflags zijn apart aan lokale v1.2.3 help getoetst; geen model-compatibiliteitsclaim.

## Werkelijk uitgevoerde demo
```sh
python3 -m scripts.asset_handoff --demo
```

Onderstaande JSON is het werkelijke resultaat met een tijdelijk aangemaakt synthetisch PNG-bestand en de bestaande gedeelde skills op de testhost. Geen providerresponse of productfoto wordt nagebootst.

```json
{
  "synthetic": true,
  "transport": "cli",
  "local_handoff_verified": true,
  "prompt_path": "prompts/editorial-master.md",
  "prompt_sha256": "d1350c43b2eec69fe7f64e2ecb299ee834d181569fd8362029392c52a6816838",
  "asset_sha256": "e5dd92acd7d1f9550a1848c765289b33b408f0f6c002fd935696ac778965182d",
  "binding_role": "product_reference",
  "cli_flag": "--image-references",
  "shared_skill_files_present": [
    "higgsfield-4k-delivery",
    "higgsfield-ad-creative",
    "higgsfield-cli-operations",
    "higgsfield-content-operations",
    "higgsfield-production-planning",
    "higgsfield-reference-continuity"
  ],
  "provider_calls": 0,
  "credits_spent": 0,
  "authorizes_spending": false,
  "ready_to_execute": false,
  "remote_handoff_verified": false,
  "temporary_sources_removed_after_demo": true,
  "blockers": [
    "live_cli_model_schema",
    "account_workspace",
    "exact_quote",
    "independent_grant",
    "remote_upload_and_job_readback"
  ]
}
```

De tijdelijke asset wordt na validatie verwijderd. Dit is een bewijs van lokale overdracht en afwijzingsregels, geen blijvend uitvoerbaar productiepacket. Echte bronbeelden, rechten en owner-approvals zijn niet met deze fixture bewezen. Tests gebruiken expliciet benoemde synthetische dependency-stubs voor CI-portabiliteit; de bovenstaande hostdemo gebruikt de werkelijk aanwezige shared-skillbestanden.

## Grens
Live CLI-auth/workspace, modelparameters, uploadreadback, kostenquote, onafhankelijke grant en generation-job zijn niet bewezen door deze run. Geen kredietsaldo is opgevraagd of spendactie gestart. Een positief production_preparation-testpacket blijft ready_to_execute=false en authorizes_spending=false. Remote GitHub Actions-status is niet geverifieerd; CI is geconfigureerd voor Python 3.11 en 3.14. De dry-run is geen OS-sandbox of volledige paid-executor.

## Herhalen
```sh
python3 -m unittest discover -s tests -v
python3 -m scripts.asset_handoff --demo
git diff --check
```
Voor strict resource-hygiëne gebruikt de workflow naast ResourceWarning-as-error ook een unraisable-hook plus gc.collect; alleen -W error mist fouten die in finalizers worden afgevangen.
