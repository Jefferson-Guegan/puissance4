from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter import Tk, StringVar, Label, Entry, Button
from functools import partial

def Bonjour():
    print ("bonjour")


#taille des cases 
c = 50
#nombre de lignes
n = 7
l = 6
cases = []

puissance4 = Tk()
puissance4.title("Notre puissance4")


#création des boutons
 
bouton_quitter = Button(puissance4, text='Quitter',command=puissance4.quit)
bouton_quitter.grid(row = 1, column = 1, sticky = W+E, padx=3, pady=3)

#création du caneva
dessin = Canvas(puissance4, width=n*c,height=l*c, bg='white')
dessin.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3)


#création des figures
for ligne in range(n):
    transit=[]
    for colonne in range(n):
        transit.append(dessin.create_rectangle(colonne*c+2, ligne*c+2, (colonne+1)*c+2, (ligne+1)*c+2))
    cases.append(transit)


# --- Activation de la surveillance sur l'application graphique
    
puissance4.mainloop ()


