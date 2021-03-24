def afficher_grille(grille):
    for i in range(3):
        print(" | "+str(grille[i]), end='')
    print(" |")
    print(" -------------")
    for i in range(3):
        print(" | "+str(grille[i+3]), end='')
    print(" |")
    print(" -------------")
    for i in range(3):
        print(" | "+str(grille[i+6]), end='')
    print(" |")

def tour(joueur, grille):
    print("C'est le tour du joueur:",(joueur))
    ligne=input("Indiquez la ligne: ")
    colonne= input("Indiquez la colonne: ")
    print("vous avez joué la case:",colonne,ligne)
    while grille[int(colonne)+int(ligne)*3]!=" ":
        print("Cette case est déjà joué !")
        ligne = input("Indiquez la ligne: ")
        colonne = input("Indiquez la colonne: ")
        print("vous avez joué la case:", colonne, ligne)

    if joueur==1:
        grille[int(colonne) + int(ligne)*3]="X"
    if joueur==2:
        grille[int(colonne) + int(ligne)*3]="O"
    afficher_grille(grille)

def le_gagnant(grille):
    if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]!=" "):
        return 1
    if (grille[3] == grille[4]) and (grille[3] == grille[5]) and (grille[3] != " "):
        return 1
    if (grille[6] == grille[7]) and (grille[6] == grille[8]) and (grille[6] != " "):
        return 1
    if (grille[0] == grille[3]) and (grille[0] == grille[6]) and (grille[0] != " "):
        return 1
    if (grille[1] == grille[4]) and (grille[1] == grille[7]) and (grille[1] != " "):
        return 1
    if (grille[2] == grille[5]) and (grille[2] == grille[8]) and (grille[2] != " "):
        return 1
    if (grille[0] == grille[4]) and (grille[0] == grille[8]) and (grille[0] != " "):
        return 1
    if (grille[2] == grille[4]) and (grille[2] == grille[6]) and (grille[2] != " "):
        return 1

def match_nul(grille):
    for i in range(0,9):
        if grille[i]==" ":
            return 0
        return 1


victoire = 0
joueur = 1
grille = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
afficher_grille(grille)
tour(joueur, grille)

while victoire==0:
    tour(joueur,grille)
    if le_gagnant(grille):
        print("Le joueur", str(joueur), "est gagnant")
        victoire=1
    else:
        if match_nul(grille):
            print("Plus de place, match nul !")
            victoire=1
    if joueur==1:
        joueur=2
    else:
        joueur=1





















