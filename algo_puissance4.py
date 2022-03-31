
from colors import Colors

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

            
            
colo=input("Quel couleur est votre jeton? : Y/R  ")
Nom1=input("Quel est votre nom? :  ")

if colo=="Y":
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
a=0

while a==0:
    
    for i in Joueurs:
        tab.affichage()
        rep=int(input(i.nom+" : Dans quelle colonne voulez-vous placer votre pion : "))
        j=5
        while j>=0:     
            if (tab.tab[j][rep-1] == "."):
                tab.tab[j][rep-1]=i.jeton
                Last_jeton=[j,rep-1]
                j=-1
            else:
                j-=1
        
        
            
