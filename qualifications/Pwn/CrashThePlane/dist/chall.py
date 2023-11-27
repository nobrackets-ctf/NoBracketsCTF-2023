#!/usr/bin/env python3
"""
@Author : Drahoxx
@Date : 07/2023
@Project : NoBracketsCTF/Pwn/CrashThePlane/chall.py
@Desc : Le but de ce challenge est de faire "crasher" le programme (et donc l'avion !). Bon courage !
"""
from flag import FLAG, EXPLICATIONS

directions = ["↑","↗","→","↘","↓","↙","←","↖"]

class Aviooooon():
    """
    L'objet Aviooooon représente un avion. L'avion peut tourner à droite ou à gauche, avancer plus ou moins vite
    lâcher une charge explosive ou encore afficher le tableau de bord au pilote.
    """
    def __init__(self):
        self.vitesse = 0
        self.index_de_direction = 0
        self.direction = directions[self.index_de_direction] # --> "↑"

    def tourner_a_gauche(self):
        self.index_de_direction += 1
        self.index_de_direction %= len(directions)
        self.direction = directions[self.index_de_direction]

    def tourner_a_droite(self):
        self.index_de_direction -= 1
        self.index_de_direction %= len(directions)
        self.direction = directions[self.index_de_direction]

    def vroom_plus_vite(self):
        self.vitesse+=1

    def vroom_moins_vite(self):
        self.vitesse-=1

    def boom(self):
        print("Bim bam boom")

    def afficher_le_tableau_de_bord(self):
        print("----------AVION3000----------")
        print("Vitesse actuelle",self.vitesse)
        print("Direction de l'avion :",self.direction)
        print("Temps : Ensoleillé")
        print("-----------------------------")


# On créer notre avion
avion = Aviooooon()
# Gestion des erreurs
try:

    # Temps qu'il y a du jus dans l'appareil, l'avion tourne !
    while True:

        # Affichage du menu
        print("\n")
        print("Tapez `1` pour faire tourner l'avion à gauche")
        print("Tapez `2` pour faire tourner l'avion à droite")
        print("Tapez `3` pour faire accélérer l'avion")
        print("Tapez `4` pour faire ralentir l'avion")
        print("Tapez `5` pour lacher un colis explosif")
        # Choix du pilote
        choix = int(input("Entrez votre choix >>> "))

        # Traitement du choix
        if choix == 1:
            avion.tourner_a_gauche()
        elif choix == 2:
            avion.tourner_a_droite()
        elif choix == 3:
            avion.vroom_plus_vite()
        elif choix == 4:
            avion.vroom_moins_vite()
        elif choix == 5:
            avion.boom()
        else:
            print("Choix invalide ! Entrez un **chiffre** cohérent !!!!")

        # Quoiqu'il arrive (ou presque...), afficher le tableau de bord.
        avion.afficher_le_tableau_de_bord()

except:
    # Well-played !
    print(EXPLICATIONS)
    print("\n\n")
    print(FLAG)
