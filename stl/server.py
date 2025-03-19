from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")  # CORSを許可
        self.send_header("Access-Control-Allow-Methods", "GET")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

httpd = HTTPServer(("0.0.0.0", 8000), CORSRequestHandler)
print("Serving at port 8000")
httpd.serve_forever()

