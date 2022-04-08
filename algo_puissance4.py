################################ PUISSANCE 4 #################################
from calendar import c
from colors import Colors

###### CLASSES ######

# Définition du joueur
class Joueur:
    def __init__ (self,couleur,nom):
        self.couleur = couleur # En fait, soit ROUGE, soit JAUNE
        self.jeton=self.couleur+"O"+Colors.RESET
        self.nom = nom # Le nom du joueur
        self.nb_victoires = int(0) # Nombre de victoires
        # ordi ou 2e personne

    def presentation(self): #présentation
        print(" Nom:  "+self.couleur+self.nom+Colors.RESET)
        print(" Type:    "+self.jeton)
        print("\n")
    
    def Placer_pion(self) : #méthode placement de pion
        self.rep =int(input(joueur.nom+" : Clique sur la colonne de ton choix : "))
        place=False
        while place==False:
            if self.rep<1 or self.rep>7:
                self.rep=int(input(joueur.nom+" t'es débile...C'est pas une colonne! "))
                place=False
            else :
                place=True
        j=5
        while j>=0:     
            if (tab.tab[j][self.rep-1] == "."):
                tab.tab[j][self.rep-1]=joueur.jeton
                self.last=[j,self.rep-1]
                j=-1
            else:
                j-=1
        return self.last 

    def Vertical (self,tab) : #methode victoire colonne
        count_col=0
        if self.last[0]<3 and tab[self.last[0]+1][self.last[1]]==joueur.jeton and tab[self.last[0]+2][self.last[1]]==joueur.jeton and tab[self.last[0]+3][self.last[1]]==joueur.jeton:
                count_col=4
                print(self.nom, "a gagné!")
        return count_col
    
    def Horizontal (self,tab): #methode victoire ligne
        count_lig=0
        if 0<=self.last[1]<4 and tab[self.last[0]][self.last[1]+1]==joueur.jeton and tab[self.last[0]][self.last[1]+2]==joueur.jeton and tab[self.last[0]][self.last[1]+3]==joueur.jeton:
            count_lig=4
            print(self.nom, "a gagné!")
        elif self.last[1]>2 and tab[self.last[0]][self.last[1]-1]==joueur.jeton and tab[self.last[0]][self.last[1]-2]==joueur.jeton and tab[self.last[0]][self.last[1]-3]==joueur.jeton:
            count_lig=4
            print(self.nom, "a gagné!")
        elif 0>self.last[1] and self.last[1]<5 and tab[self.last[0]][self.last[1]-1]==joueur.jeton and tab[self.last[0]][self.last[1]+1]==joueur.jeton and tab[self.last[0]][self.last[1]+2]==joueur.jeton:
            count_lig=4
            print(self.nom, "a gagné!")
        elif 1>self.last[1] and self.last[1]<6 and tab[self.last[0]][self.last[1]-2]==joueur.jeton and tab[self.last[0]][self.last[1]-1]==joueur.jeton and tab[self.last[0]][self.last[1]+1]==joueur.jeton:
            count_lig=4
            print(self.nom, "a gagné!")
        return  count_lig
    
    def Diag_ascendante (self,tab): #methode  victoire diagonale ascendante
        count_diaga=0
        if self.last[0]>2 and self.last[1]<4 and tab[self.last[0]-1][self.last[1]+1]==joueur.jeton and tab[self.last[0]-2][self.last[1]+2]==joueur.jeton and tab[self.last[0]-3][self.last[1]+3]==joueur.jeton:
            count_diaga=4 #diagonale 3 pions au dessus a droite
            print(self.nom, "a gagné!")
        elif self.last[0]>1 and self.last[1]<5 and self.last[0]<5 and self.last[1]>0 and tab[self.last[0]-1][self.last[1]+1]==joueur.jeton and tab[self.last[0]-2][self.last[1]+2]==joueur.jeton and tab[self.last[0]+1][self.last[1]-1]==joueur.jeton:
            count_diaga=4 # diagonal 2 au dessus à droite, 1 en dessous à gauche
            print(self.nom, "a gagné!")
        elif self.last[0]<4 and self.last[1]>0 and self.last[0]<4 and self.last[1]>1 and tab[self.last[0]-1][self.last[1]+1]==joueur.jeton and tab[self.last[0]+1][self.last[1]-1]==joueur.jeton and tab[self.last[0]+2][self.last[1]-2]==joueur.jeton:
            count_diaga=4 # diagonale 1 au dessus à droite, 2 en dessous à gauche
            print(self.nom, "a gagné!")
        elif self.last[0]<3 and self.last[1]>2 and tab[self.last[0]+1][self.last[1]-1]==joueur.jeton and tab[self.last[0]+2][self.last[1]-2]==joueur.jeton and tab[self.last[0]+3][self.last[1]-3]==joueur.jeton:
            count_diaga=4 #diagonale 3 pions en dessous a droite
            print(self.nom, "a gagné!")
        return count_diaga
    
    def Diag_descendante(self,tab):# Conditions Diagonales descendantes
        count_diagd=0
        if self.last[0]<3 and self.last[1]<4 and tab[self.last[0]+1][self.last[1]+1]==joueur.jeton and tab[self.last[0]+2][self.last[1]+2]==joueur.jeton and tab[self.last[0]+3][self.last[1]+3]==joueur.jeton:
            count_diagd=4 #diagonale 3 pions en dessous a droite
            print(self.nom, "a gagné!")
            count_diagd=4 # diagonale 2 en dessous à droite, 1 au dessus à gauche
        elif self.last[0]<4 and self.last[1]<5 and self.last[0]>0 and self.last[1]>0 and tab[self.last[0]+1][self.last[1]+1]==joueur.jeton and tab[self.last[0]+2][self.last[1]+2]==joueur.jeton and tab[self.last[0]-1][self.last[1]-1]==joueur.jeton:
            print(self.nom, "a gagné!")
        elif self.last[0]<5 and self.last[1]>6 and self.last[0]>1 and self.last[1]>1 and tab[self.last[0]+1][self.last[1]+1]==joueur.jeton and tab[self.last[0]-1][self.last[1]-1]==joueur.jeton and tab[self.last[0]-2][self.last[1]-2]==joueur.jeton:
            count_diagd=4 # diagonal 1 en dessous à droite, 2 au dessus à gauche
            print(self.nom, "a gagné!")
        elif self.last[0]>2 and self.last[1]>2 and tab[self.last[0]-1][self.last[1]-1]==joueur.jeton and tab[self.last[0]-2][self.last[1]-2]==joueur.jeton and tab[self.last[0]-3][self.last[1]-3]==joueur.jeton:
            count_diagd=4 #diagonale 3 pions au dessus a gauche
            print(self.nom, "a gagné!")
        return count_diagd

class Tableau:
    def __init__ (self):
        self.tab=[]

    def create_tab(self):
        x=7
        y=6
        for j in range(y):
            ligne=[]
            for i in range(x):
                ligne.append(".")
            self.tab.append(ligne)

    def affichage(self):
        space= ""
        absc= " "
        for i in range(len(self.tab[0])):
            absc += str(i+1)+" "
        print(absc)

        for y in range(len(self.tab)):
            chaine = " "
            for point in self.tab[y]:
                chaine+=point+ " "
            print(chaine)



###### MAIN ######            
         
colo=input("Quel couleur est votre jeton? : Y/R  ")#Joueur choix couleur et nom
Nom1=input("Quel est votre nom? :  ")

if colo=="Y" or colo=="y" or colo=="": 

    color1=Colors.YELLOW
    Joueur1=Joueur(color1,Nom1)
    Nom2=input("Joueur2 quel est votre nom? :  ")
    color2=Colors.RED
    Joueur2=Joueur(color2,Nom2)
else:
    color1=Colors.RED
    Joueur1=Joueur(color1,Nom1)
    Nom2=input("Joueur2 quel est votre nom? :  ")
    color2=Colors.YELLOW
    Joueur2=Joueur(color2,Nom2)

Joueur1.presentation() #presentation des joueurs
Joueur2.presentation()

Joueurs=[Joueur1,Joueur2]

tab=Tableau() #appel de la classe Tableau 
tab.create_tab()


victoire=False

while victoire==False:
    
    for joueur in Joueurs:
        count_col=0
        count_lig=0
        count_diaga=0
        count_diagd=0
        tab.affichage()
        joueur.Placer_pion()
        joueur.Horizontal(tab.tab)
        joueur.Vertical(tab.tab)
        joueur.Diag_ascendante(tab.tab)
        joueur.Diag_descendante(tab.tab)
    
    if joueur.Horizontal(tab.tab)==4 or joueur.Vertical(tab.tab)==4 or joueur.Diag_ascendante(tab.tab)==4 or joueur.Diag_descendante(tab.tab)==4:
        victoire=True
        tab.affichage()
        exit




            
                


        
