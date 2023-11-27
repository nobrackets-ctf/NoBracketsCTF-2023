#!/usr/bin/env python3

import random
import math
from inputimeout import inputimeout

# Fonction de génération du cercle
def generate_sphere():
    # Coordonnées du centre
    centerX = random.uniform(-10, 10)
    centerY = random.uniform(-10, 10)
    centerZ = random.uniform(-10, 10)
    # Rayon
    radius = random.uniform(1, 5) 
    return (centerX, centerY, centerZ), radius

# Fonction de vérification de la présence d'un point dans la sphère
def is_inside_sphere(point, sphereCenter, sphereRadius):
    # Point à vérifier
    x, y, z = point
    # Centre de la sphère
    centerX, centerY, centerZ = sphereCenter
    # Calcul de la distance entre le point et le centre du cercle
    distance = math.sqrt((centerX - x)**2 + (centerY - y)**2 + (centerZ - z)**2)
    # Si la distance est inférieure ou égale au rayon de la sphère alors le point en fait partie
    return distance <= sphereRadius

def gen_rand_point(sphereCenter,sphereRadius):
    # Dans un tiers des cas (je suis pas sûr des stats mais tqt)
    if random.randint(1,3) == 1:
        # On crée un point dans la sphère, avec une inclination un azimuth et un rayon entre 0 et celui de la sphère
        inclination = random.uniform(0, math.pi)
        azimuth = random.uniform(0, 2 * math.pi)
        radius = random.uniform(0, sphereRadius)
        
        x = sphereCenter[0] + radius * math.sin(inclination) * math.cos(azimuth)
        y = sphereCenter[1] + radius * math.sin(inclination) * math.sin(azimuth)
        z = sphereCenter[2] + radius * math.cos(inclination)
        return (x, y, z)
    
    # Dans le reste des cas on retourne un point random
    else:
        return (random.uniform(-15, 15), random.uniform(-15, 15), random.uniform(-15,15))


def main():
    ascii = r"""
   ______      __           __  _         ____  _                      
  / ____/___ _/ /___ ______/ /_(_)____   / __ \(_)___ _____ ____  _____
 / / __/ __ `/ / __ `/ ___/ __/ / ___/  / / / / / __ `/ __ `/ _ \/ ___/
/ /_/ / /_/ / / /_/ / /__/ /_/ / /__   / /_/ / / /_/ / /_/ /  __/ /    
\____/\__,_/_/\__,_/\___/\__/_/\___/  /_____/_/\__, /\__, /\___/_/     
                                              /____//____/             
    """
    print(ascii)
    # Génération de la sphère
    sphereCenter, sphereRadius = generate_sphere()
    print(f"\nCentre de la planète : {sphereCenter}\nRayon : {sphereRadius}")

    # Il faut 30 bonnes réponses pour valider
    for i in range(30):
        # On génère un point aléatoire
        randomPoint = gen_rand_point(sphereCenter,sphereRadius)
        print(f"\nPoint à explorer : {randomPoint}")
        # On récupère l'input
        try:
            userInput = inputimeout(prompt="\nLe point fait-il partie de la planète ? (oui/non/quit)\n\n>>> ",timeout=3).lower()
        except:
            print("\nTrop lent !")
            break

        if userInput == "quit":
            print("Exiting the game...")
            break
        
        # Si l'input est valide
        if userInput == "oui" or userInput == "non":
            # On vérifie si le point est dans la sphère
            is_inside = is_inside_sphere(randomPoint, sphereCenter, sphereRadius)
            # Si la réponse est bonne on continue
            if (userInput == "oui" and is_inside) or (userInput == "non" and not is_inside):
                print("Bien joué, nous allons pouvoir miner ce point !")
                # Sauf si c'est le dernier tour, à ce moment là on print le flag
                if i == 29:
                    print("Vous avez réussi à piller la nature de cette planète ! Voici le flag : NBCTF{C0v3r_m3_w17h_d14m0nd5!}")
                    break
            # Sinon on break
            else:
                print("Mauvaise réponse, mission annulée...")
                break
        # Gestin d'input invalide
        else:
            print("Input invalide ! Merci d'entrer 'oui', 'non', ou 'quit'.")
            break

if __name__=="__main__":
    main()
