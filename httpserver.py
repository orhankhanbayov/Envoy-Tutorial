from http.server import HTTPServer, BaseHTTPRequestHandler

class CustomHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        port = self.server.server_port  # Get the port the request was received on
        print(f"Received request on port {port} from {self.client_address}")

        if self.path == "/test":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.send_header("testheaders", "1")
            self.end_headers()
            self.wfile.write(f"This is the /test endpoint (served from port {port})".encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Not Found")

def run_server(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CustomHandler)
    print(f"Serving on port {port}...")
    httpd.serve_forever()

# Run servers on two different ports
import threading

threading.Thread(target=run_server, args=(8000,), daemon=True).start()
threading.Thread(target=run_server, args=(8001,), daemon=True).start()

# Keep script alive
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nServers shutting down.")