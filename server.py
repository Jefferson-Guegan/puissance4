#!/usr/bin/python3
import http.server

#Intialisation du port et de l'addresse
port = 8000
address = ("", port)

server = http.server.HTTPServer

#Configuration du script directory
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/cgi-bin"]
print("Serveur actif sur le port :", port)

httpd = server(address, handler)
httpd.serve_forever()