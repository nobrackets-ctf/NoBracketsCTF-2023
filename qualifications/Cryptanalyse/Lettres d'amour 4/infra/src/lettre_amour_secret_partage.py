#!/usr/bin/env python3
## Code source du serveur

from Crypto.Util.number import getPrime
import json
from secret import flag

## Génération des paramètres
p = getPrime(1024)
g = 2
nA = getPrime(1024)
nB = getPrime(1024)

## Calcul de la clé publique d'Alice
A = pow(g,nA,p)

try:
    print("Interception du message d'Alice : {p : " + str(p) + ", g : " + str(g) + ", A : " + str(A) + "}")
    print('Envoyez les parametres corrompus a Bob (Respectez le format suivant : {"p" : .., "g" : .., "A" : ..})')

    ## Récupération des paramètres corrompus
    data = json.loads(input())
    pT = int(data['p'])
    gT = int(data['g'])
    AT = int(data['A'])
    
    ## Calcul de la clé publique de Bob (avec les paramètres corrompus)
    BT = pow(gT,nB,pT)
    
    print("Interception du message de Bob : {B : " + str(BT) + "}")
    print('Envoyez les parametres corrompus a Alice (Respectez le format suivant : {"B" : ..})')

    ## Récupération des paramètres corrompus
    data = json.loads(input())
    B = int(data['B'])
    
    ## Calcul de la clé partagée entre Alice et Bob (avec les paramètres corrompus)
    K = pow(B,nA,p)
    print("Fin de l'echange...")

    ## A vous de jouer !!
    print("Quelle est la valeur de la clé partagée ?  : ")
    data = input()

    if K == int(data):
        print("Voici le flag  : " + flag)
    else:
        print("Clé incorrecte !")

except:
    print("ERROR !")
    pass

exit()
