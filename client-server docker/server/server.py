#!/user/bin/env python3
import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler
print("In server file")
with socketserver.TCPServer(("",1234),handler) as httpd:
        httpd.serve_forever()