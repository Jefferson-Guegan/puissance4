#!/usr/bin/python3
import cgi

print("Content-Type: text/html; charset=utf-8\n")


html="""
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title> Puissance 4 de la muerte</title>
        <link rel="stylesheet" media="screen" type="text/css" href="../style.css"/>
    </head>

    <body>

        <h1>Bienvenue sur cette version réseau du célèbre jeu : Puissance 4</h1>

        <form id="box" action="http://localhost:8000/cgi-bin/partie.py" method="post">
            <legend> Lancer une partie de puissance 4 </legend>
            <div id="container">
                <div id="user">
                    <label> Nom de guerre </label> <br>
                    <input  type = "text" name = "userName"> <br>
                </div>    
                <div id="perso">    
                    <label> Couleur </label>
                    <input type = "text" name = "userColor">
                </div>
            </div>    
            <input class="btn-grad" type="submit" value="C'est parti !">                  
        </form>
    
    </body>
</html>"""

print(html)
