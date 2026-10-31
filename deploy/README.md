# AVELNA — safe upgrade of the no-spend control scaffold

This deploys a **loopback-only health service**, NOT the production Hermes, Meta or Higgsfield paid executor.

- Linux host with running systemd user manager, Python 3.11+, curl and tar.
- Downloads the current GitHub main source archive, builds/compiles/runs offline unit tests before replacing anything.
- Switches only the `avelna-control.service` user unit after tests pass, verifies the new local `/health` response, and attempts rollback on failure.
- The previous source release remains on disk. SSH, personal Hermes, other containers/services and paid provider accounts are not touched.
- Supports `AVELNA_HOME` and `AVELNA_PORT` (default 8765); choose a free port. Changing the port of a pre-existing AVELNA service can require separate rollback verification.
- If systemd user manager isn't active, reports this without changing services.

## One-command install/upgrade (on your own SSH host)

~~~bash
curl -fsSL https://raw.githubusercontent.com/jens-mul/AVELNA/main/deploy/upgrade.sh -o /tmp/avelna-upgrade.sh && bash /tmp/avelna-upgrade.sh
~~~

Afterwards, check `systemctl --user status avelna-control.service` and `curl -fsS http://127.0.0.1:8765/health`.

**NOT YET:** actual Hermes credential binding, Higgsfield upload bridge, independent spend executor, Meta drafts/activation, order-data integration and live ads. Those need host/account capability discovery, external approval and real integration tests. A green `/health` endpoint only means the no-spend scaffold is online.
