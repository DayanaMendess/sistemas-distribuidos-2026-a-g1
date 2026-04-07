from http.server import BaseHTTPRequestHandler, HTTPServer
import os

PORT = int(os.getenv("PORT", "8000"))
MESSAGE = os.getenv("MESSAGE", "Hello from Docker!")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        msg = f"{MESSAGE} Running on port {PORT}\n"
        self.wfile.write(msg.encode("utf-8"))

HTTPServer(("", PORT), Handler).serve_forever()