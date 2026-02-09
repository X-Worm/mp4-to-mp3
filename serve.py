#!/usr/bin/env python3
"""Local dev server with COOP/COEP headers required by FFmpeg.wasm (SharedArrayBuffer)."""

import http.server
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000


class COEPHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()


print(f"Serving at http://localhost:{PORT}")
http.server.HTTPServer(("", PORT), COEPHandler).serve_forever()
