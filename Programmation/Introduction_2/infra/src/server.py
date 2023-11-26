#!/usr/bin/env python3

from flag import FLAG
from random import randint

print("#"*20+"EXPLICATIONS"+"#"*20)
print("Bonjour soldat. Votre mission est la suivante :")
print("Vous devez me dire combien de balles il reste à la fin de chaque semaine d'après les chiffres de nos 173 régiments. Et ce sur toute l'année 1917.")
print("Les données envoyées suivront le format suivant :\n")
print("(1/52) "+"-"*40)
print("Régiment 1 -- Nombres de balles utilisées cette semaine : 1221")
print("Régiment 2 -- Nombres de balles utilisées cette semaine : 1231")
print("...")
print("Régiment 172 -- Nombres de balles utilisées cette semaine : 910")
print("Régiment 173 -- Nombres de balles utilisées cette semaine : 300")
print("Nombre de balles au début de la semaine : 910029")
print(">>> <Entrez le résultat du calcul>")
print("(2/52) "+"-"*40)
print("...")
print("Nombre de balles au début de la semaine : 102030")
print(">>> <Entrez le résultat du calcul>")
print("#"*52)

for week in range(52):
    WEEKLY_COUNT = 0
    print(f"({week+1}/52) "+"-"*40)
    for regiment in range(173):
        bullets_used = randint(5000,10000)
        WEEKLY_COUNT += bullets_used
        print(f"Régiment {regiment+1} -- Nombres de balles utilisées cette semaine : {bullets_used}")
    DELTA = randint(2000,9000)
    print(f"Nombre de balles au début de la semaine : {DELTA+WEEKLY_COUNT}")
    try:
        res = int(input(">>> "))
    except:
        print("Entrez un nombre.")
        exit(1)
    if res != DELTA:
        print(f"Erreur ! Le nombre était {DELTA}. Mauvais soldat !")
        exit(1)
print(f"Bravo petit soldat, voici le flag : {FLAG}")
    
