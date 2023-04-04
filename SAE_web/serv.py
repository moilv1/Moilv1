import http.server
import socketserver
import socket

print("serveur is on IPv4 adresse :",socket.gethostbyname(socket.gethostname()))

PORT = 7070
Handler = http.server.SimpleHTTPRequestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
    
#pour lancer le serveur, F5, pour l'arrêter, Ctrl+F2