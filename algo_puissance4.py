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

    def presentation(self):
        print(" Nom:  "+self.couleur+self.nom+Colors.RESET)
        print(" Type:    "+self.jeton)
        print("\n")

    

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
         
colo=input("Quel couleur est votre jeton? : Y/R  ")
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

Joueur1.presentation()
Joueur2.presentation()

Joueurs=[Joueur1,Joueur2]

tab=Tableau()
tab.create_tab()

rep=0

count_col=0
count_lig=0
victoire=False

while victoire==False:
    
    for joueur in Joueurs:
        count_col=0
        count_lig=0
        count_diaga=0
        count_diagd=0
        tab.affichage()
        rep=int(input(joueur.nom+" : Dans quelle colonne voulez-vous placer votre pion (1-7): "))
        
        while rep<1 or rep>7:
            rep=int(input(joueur.nom+" t'es débile... : ENTRE 1 ET 7 : "))


        if rep>0 and rep<8:
            j=5
            while j>=0:     
                if (tab.tab[j][rep-1] == "."):
                    tab.tab[j][rep-1]=joueur.jeton
                    Last_jeton=[j,rep-1]
                    j=-1
                else:
                    j-=1
            # Condition victoire colonne
            if Last_jeton[0]<3 and tab.tab[Last_jeton[0]+1][Last_jeton[1]]==joueur.jeton and tab.tab[Last_jeton[0]+2][Last_jeton[1]]==joueur.jeton and tab.tab[Last_jeton[0]+3][Last_jeton[1]]==joueur.jeton:
                count_col=4
            
            # Conditions victoire lignes
            elif 0<=Last_jeton[1]<4 and tab.tab[Last_jeton[0]][Last_jeton[1]+1]==joueur.jeton and tab.tab[Last_jeton[0]][Last_jeton[1]+2]==joueur.jeton and tab.tab[Last_jeton[0]][Last_jeton[1]+3]==joueur.jeton:
                count_lig=4
            elif Last_jeton[1]>2 and tab.tab[Last_jeton[0]][Last_jeton[1]-1]==joueur.jeton and tab.tab[Last_jeton[0]][Last_jeton[1]-2]==joueur.jeton and tab.tab[Last_jeton[0]][Last_jeton[1]-3]==joueur.jeton:
                count_lig=4
            elif 0>Last_jeton[1] and Last_jeton[1]<5 and tab.tab[Last_jeton[0]][Last_jeton[1]-1]==joueur.jeton and tab.tab[Last_jeton[0]][Last_jeton[1]+1]==joueur.jeton and tab.tab[Last_jeton[0]][Last_jeton[1]+2]==joueur.jeton:
                count_lig=4
            elif 1>Last_jeton[1] and Last_jeton[1]<6 and tab.tab[Last_jeton[0]][Last_jeton[1]-2]==joueur.jeton and tab.tab[Last_jeton[0]][Last_jeton[1]-1]==joueur.jeton and tab.tab[Last_jeton[0]][Last_jeton[1]+1]==joueur.jeton:
                count_lig=4

            # Conditions Diagonales ascendantes
            
            elif Last_jeton[0]>2 and Last_jeton[1]<4 and tab.tab[Last_jeton[0]-1][Last_jeton[1]+1]==joueur.jeton and tab.tab[Last_jeton[0]-2][Last_jeton[1]+2]==joueur.jeton and tab.tab[Last_jeton[0]-3][Last_jeton[1]+3]==joueur.jeton:
                count_diaga=4 #diagonale 3 pions au dessus a droite
            elif Last_jeton[0]>1 and Last_jeton[1]<5 and Last_jeton[0]<5 and Last_jeton[1]>0 and tab.tab[Last_jeton[0]-1][Last_jeton[1]+1]==joueur.jeton and tab.tab[Last_jeton[0]-2][Last_jeton[1]+2]==joueur.jeton and tab.tab[Last_jeton[0]+1][Last_jeton[1]-1]==joueur.jeton:
                count_diaga=4 # diagonal 2 au dessus à droite, 1 en dessous à gauche
            elif Last_jeton[0]<4 and Last_jeton[1]>0 and Last_jeton[0]<4 and Last_jeton[1]>1 and tab.tab[Last_jeton[0]-1][Last_jeton[1]+1]==joueur.jeton and tab.tab[Last_jeton[0]+1][Last_jeton[1]-1]==joueur.jeton and tab.tab[Last_jeton[0]+2][Last_jeton[1]-2]==joueur.jeton:
                count_diaga=4 # diagonale 1 au dessus à droite, 2 en dessous à gauche
            elif Last_jeton[0]<3 and Last_jeton[1]>2 and tab.tab[Last_jeton[0]+1][Last_jeton[1]-1]==joueur.jeton and tab.tab[Last_jeton[0]+2][Last_jeton[1]-2]==joueur.jeton and tab.tab[Last_jeton[0]+3][Last_jeton[1]-3]==joueur.jeton:
                count_diaga=4 #diagonale 3 pions en dessous a droite

            # Conditions Diagonales descendantes

            elif Last_jeton[0]<3 and Last_jeton[1]<4 and tab.tab[Last_jeton[0]+1][Last_jeton[1]+1]==joueur.jeton and tab.tab[Last_jeton[0]+2][Last_jeton[1]+2]==joueur.jeton and tab.tab[Last_jeton[0]+3][Last_jeton[1]+3]==joueur.jeton:
                count_diagd=4 #diagonale 3 pions en dessous a droite
            elif Last_jeton[0]<4 and Last_jeton[1]<5 and Last_jeton[0]>0 and Last_jeton[1]>0 and tab.tab[Last_jeton[0]+1][Last_jeton[1]+1]==joueur.jeton and tab.tab[Last_jeton[0]+2][Last_jeton[1]+2]==joueur.jeton and tab.tab[Last_jeton[0]-1][Last_jeton[1]-1]==joueur.jeton:
                count_diagd=4 # diagonale 2 en dessous à droite, 1 au dessus à gauche
            elif Last_jeton[0]<5 and Last_jeton[1]>6 and Last_jeton[0]>1 and Last_jeton[1]>1 and tab.tab[Last_jeton[0]+1][Last_jeton[1]+1]==joueur.jeton and tab.tab[Last_jeton[0]-1][Last_jeton[1]-1]==joueur.jeton and tab.tab[Last_jeton[0]-2][Last_jeton[1]-2]==joueur.jeton:
                count_diagd=4 # diagonal 1 en dessous à droite, 2 au dessus à gauche
            elif Last_jeton[0]>2 and Last_jeton[1]>2 and tab.tab[Last_jeton[0]-1][Last_jeton[1]-1]==joueur.jeton and tab.tab[Last_jeton[0]-2][Last_jeton[1]-2]==joueur.jeton and tab.tab[Last_jeton[0]-3][Last_jeton[1]-3]==joueur.jeton:
                count_diagd=4 #diagonale 3 pions au dessus a gauche

            print(count_col,count_lig,count_diaga,count_diagd)     
            if count_col==4 or count_lig==4 or count_diaga==4 or count_diagd==4:
                victoire=True
                print("WIN!!")
                tab.affichage()
                exit




            
                


        
