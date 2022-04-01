#!/usr/bin/python3
import cgi
#import socket

#CGI
form= cgi.FieldStorage()
userName=form.getvalue("userName")

#Socket
#host, port = ('localhost', 6666)
#try:
#    socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
#    socket.connect((host, port))
#    print("Client conecté !")
#except ConnectionRefusedError:
#   print("Connexion au serveur échouée !")
#finally:
#    socket.close()

print("Content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
<title>Partie de puissance 4</title>
<link rel="stylesheet" media="screen" type="text/css" href="../partie.css"/>
</head>
<body>
<h1>Partie</h1>
<div id="game">

<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>

<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>

<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>

<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>

<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>

<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>
<div class="cell"></div>



</div>
<button id="restart" style="visibility:hidden;">Recommencer</button>    
</body>
</html>
"""
print(html)