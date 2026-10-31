"""Local-only AVELNA control health service. No paid integrations or credentials."""
from __future__ import annotations
import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

def status_payload(root: Path) -> dict:
    p = root / "RELEASE_TAG"
    release = p.read_text(encoding="utf8").strip()[:80] if p.is_file() else "source-checkout"
    return {
        "service": "avelna-control",
        "mode": "prepare_only",
        "release": release,
        "paid_execution_enabled": False,
        "hermes_connected": False,
        "meta_ads_live": False,
        "note": "No-spend control health endpoint, NOT a paid marketing executor.",
    }

def make_handler(root: Path):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path not in ("/health", "/status"):
                self.send_error(404, "Not found")
                return
            content = json.dumps(status_payload(root)).encode("utf8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        def do_POST(self):
            self.send_error(405, "No write actions")
        def log_message(self, fmt, *args):
            pass
    return Handler

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--self-check", action="store_true")
    options = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    if options.self_check:
        print(json.dumps(status_payload(root), indent=2))
        return
    if options.host != "127.0.0.1" or not 1024 <= options.port <= 65535:
        parser.error("Only loopback and a non-privileged port are supported.")
    with ThreadingHTTPServer((options.host, options.port), make_handler(root)) as server:
        server.serve_forever(poll_interval=0.25)

if __name__ == "__main__":
    main()
