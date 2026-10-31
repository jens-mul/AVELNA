import json
import tempfile
import threading
import unittest
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import urlopen

from scripts.control_server import make_handler, status_payload

class ControlServerTests(unittest.TestCase):
    def test_no_paid_execution(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "RELEASE_TAG").write_text("sample-r1", encoding="utf8")
            result = status_payload(root)
            self.assertEqual(result["release"], "sample-r1")
            self.assertEqual(result["mode"], "prepare_only")
            self.assertFalse(result["paid_execution_enabled"])
            self.assertFalse(result["meta_ads_live"])

    def test_local_http_health(self):
        with tempfile.TemporaryDirectory() as d:
            server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(Path(d)))
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                base = f"http://127.0.0.1:{server.server_port}"
                with urlopen(base + "/health", timeout=3) as response:
                    payload = json.loads(response.read())
                    self.assertEqual(payload["service"], "avelna-control")
                with self.assertRaises(HTTPError) as cm:
                    urlopen(base + "/invalid", timeout=3)
                self.assertEqual(cm.exception.code, 404)
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=3)

if __name__ == "__main__":
    unittest.main()
