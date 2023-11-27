#!/usr/bin/env python3

import random

## Commenter la ligne ci-dessous et remplacer par `FLAG = NBCTF{Ceci_est_un_faux_flag}` pour pouvoir lancer en local.
from secret import FLAG

class Generator():
    def __init__(self):
        self.a = random.randint(1,53299)
        self.c = random.randint(1,53299)
        self.p = 53299
        self.x_current = random.randint(1,53299)

    def next(self):
        self.x_current = (self.a*self.x_current + self.c) % self.p
        return self.x_current
    
print("Bienvenue a la loterie de l'ECW !!")

BANQUE = 0
game = Generator()

print("Pour vous aider dans vos choix, voici les resultats des 5 lancers precedents : ")
for _ in range(5):
    print(f"Lancer {_} : {game.next()}")

print("A vous de jouer !!")

for _ in range(10):
    try :
        guess = int(input("Quel est votre choix ? "))
    except :
        print("Veuillez entrer un nombre.")
        exit()
    if guess == game.next():
        BANQUE += 100_000

if BANQUE == 1_000_000:
    print(FLAG)
else:
    print(f"Montant en banque : {BANQUE}")
    print("Vous n'avez pas assez d'argent pour debloquer le flag.")
