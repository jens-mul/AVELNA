#!/usr/bin/env bash
# Update ONLY the dedicated AVELNA no-spend control service. SSH and Hermes untouched.
set -u -o pipefail

upgrade_avelna() {
  local root="${AVELNA_HOME:-$HOME/.local/share/avelna-control}"
  local port="${AVELNA_PORT:-8765}"
  local unit="$HOME/.config/systemd/user/avelna-control.service"
  local stage release tag old old_unit python_bin health ok i
  case "$root" in *" "*|*$'\n'*) printf '%s\n' 'Choose AVELNA_HOME without whitespace.'; return 2;; esac
  case "$port" in ''|*[!0-9]*) printf '%s\n' 'AVELNA_PORT must be a number.'; return 2;; esac
  if [ "$port" -lt 1024 ] || [ "$port" -gt 65535 ]; then
    printf '%s\n' 'AVELNA_PORT must be between 1024 and 65535.'
    return 2
  fi
  for x in curl tar python3 systemctl mktemp mv ln grep; do
    if ! command -v "$x" >/dev/null 2>&1; then
      printf 'Missing dependency: %s\n' "$x"
      return 2
    fi
  done
  if ! systemctl --user show-environment >/dev/null 2>&1; then
    printf '%s\n' 'No active systemd user manager; existing services were not changed.'
    return 2
  fi
  mkdir -p "$root/releases" "$HOME/.config/systemd/user" || return 2
  stage="$(mktemp -d "$root/.incoming.XXXXXXXX")" || return 2
  release="$(mktemp -d "$root/releases/version.XXXXXXXX")" || return 2

  printf '%s\n' 'Downloading GitHub main and building BEFORE touching the current service...'
  if ! curl -fLsS --retry 2 --connect-timeout 10 --max-time 90 \
      'https://github.com/jens-mul/AVELNA/archive/refs/heads/main.tar.gz' \
      -o "$stage/source.tar.gz"; then
    printf '%s\n' 'Download failed; existing service is untouched.'
    return 2
  fi
  if ! tar -xzf "$stage/source.tar.gz" -C "$release" --strip-components=1; then
    printf '%s\n' 'Archive extraction failed; existing service is untouched.'
    return 2
  fi
  tag="$(basename "$release")"
  printf '%s\n' "$tag" > "$release/RELEASE_TAG"
  if ! (cd "$release" &&
         python3 -m compileall -q scripts tests &&
         python3 -m unittest discover -s tests -v &&
         python3 scripts/control_server.py --self-check >/dev/null); then
    printf '%s\n' 'Build/tests failed. Existing AVELNA service remains online.'
    return 2
  fi

  old="$(readlink "$root/current" 2>/dev/null || true)"
  old_unit="$stage/prior.unit"
  if [ -f "$unit" ]; then cp "$unit" "$old_unit" || return 2; fi
  python_bin="$(command -v python3)"
  cat > "$unit" <<UNIT
[Unit]
Description=AVELNA No-Spend Control Health Service
After=network.target

[Service]
Type=simple
WorkingDirectory=$root/current
ExecStart=$python_bin $root/current/scripts/control_server.py --host 127.0.0.1 --port $port
Restart=on-failure
RestartSec=2
NoNewPrivileges=true

[Install]
WantedBy=default.target
UNIT
  if ! systemctl --user daemon-reload; then
    printf '%s\n' 'User service reload failed; existing service not switched.'
    if [ -f "$old_unit" ]; then cp "$old_unit" "$unit"; fi
    return 2
  fi
  if ! ln -s "$release" "$root/next.$$" || ! mv -Tf "$root/next.$$" "$root/current"; then
    printf '%s\n' 'Release switch failed; investigate the current symlink.'
    return 2
  fi
  if ! systemctl --user enable avelna-control.service >/dev/null 2>&1 ||
     ! systemctl --user restart avelna-control.service; then
    printf '%s\n' 'Start failed; trying to restore previous AVELNA version.'
    if [ -n "$old" ]; then
      ln -sfn "$old" "$root/back.$$" && mv -Tf "$root/back.$$" "$root/current"
    fi
    if [ -f "$old_unit" ]; then cp "$old_unit" "$unit"; fi
    systemctl --user daemon-reload >/dev/null 2>&1 || true
    if [ -n "$old" ]; then systemctl --user restart avelna-control.service || true; fi
    return 2
  fi
  ok=0
  for i in 1 2 3 4 5 6 7 8; do
    health="$(curl -fsS --max-time 2 "http://127.0.0.1:$port/health" 2>/dev/null || true)"
    if printf '%s' "$health" | grep -Fq "$tag"; then ok=1; break; fi
    sleep 1
  done
  if [ "$ok" -ne 1 ]; then
    printf '%s\n' 'Health failed; attempting rollback of AVELNA service.'
    if [ -n "$old" ]; then
      ln -sfn "$old" "$root/back.$$" && mv -Tf "$root/back.$$" "$root/current"
    fi
    if [ -f "$old_unit" ]; then cp "$old_unit" "$unit"; fi
    systemctl --user daemon-reload >/dev/null 2>&1 || true
    if [ -n "$old" ]; then
      systemctl --user restart avelna-control.service || true
    else
      systemctl --user stop avelna-control.service || true
    fi
    return 2
  fi
  printf 'AVELNA control ONLINE: http://127.0.0.1:%s/health\n' "$port"
  printf 'New release: %s | Old retained: %s\n' "$tag" "${old:-none}"
  printf '%s\n' 'This only activates a no-spend localhost service, NOT Hermes/Meta paid automation.'
  rm -rf "$stage" || true
  return 0
}
upgrade_avelna "$@"
