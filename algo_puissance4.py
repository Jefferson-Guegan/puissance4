

def create(taille_y,taille_x):
    tab=[]
    for y in range(taille_y):
        ligne=[]
        for x in range(taille_x):
            ligne.append(".")
        tab.append(ligne)
        
    return tab

def affichage(tableau):

    space= ""
    if (len(tableau)>9):
        space = " "
    absc="  "+space
    
    for x in range(len(tableau[0])):
        absc += str(x+1)+" "
    print(absc)

    for y in range(len(tableau)):

        space=""
        if ( y<9 and len(tableau)>=10 ):
            space=" "

        chaine =str(y+1)+space+" "
        for point in tableau[y]:
            if ( point=="B" ):
                chaine+="."+" "
            elif (point == "B" ):
                chaine+="B"+" "
            elif (point == "O"):
                chaine+="\033[34m" + point + "\033[0m"+ " "
            elif (point == "@"):
                chaine+="\033[31m" + point + "\033[0m"+ " "
            elif (point == "."):
                chaine+=point+ " "
        print(chaine)


taille_x=7
taille_y=6
nb_pions=21

tab=create(taille_y,taille_x)

affichage(tab)

a=0

while a==0:
    rep=input("Dans quelle colonne voulez-vous placer votre pion : ")
