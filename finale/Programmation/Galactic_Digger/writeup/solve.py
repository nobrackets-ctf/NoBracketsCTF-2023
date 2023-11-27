#!/usr/bin/env python3

from pwn import *
import math

def is_inside_sphere(point, sphereCenter, sphereRadius):
    # Point à vérifier
    x, y, z = point
    # Centre de la sphère
    centerX, centerY, centerZ = sphereCenter
    # Calcul de la distance entre le point et le centre du cercle
    distance = math.sqrt((centerX - x)**2 + (centerY - y)**2 + (centerZ - z)**2)
    # Si la distance est inférieure ou égale au rayon de la sphère alors le point en fait partie
    return distance <= sphereRadius

def main():
    # Hôte
    r = remote("localhost",1337)

    # On vire l'ascii art
    r.recvuntil(b' : (')
    # Récupération des coordonnées du centre et transformation en float
    center = r.recvuntil(b')')[:-1].split(b', ')
    for i in range(len(center)):
        center[i] = float(center[i])

    # Récupération du rayon
    r.recvline()
    radius = float(r.recvline().strip().split()[2])
    
    # Récupération de la ligne des points (tqt c'est pas beau mais oklm)
    r.recvline()
    pointLine = r.recvline()

    while True:
        # Parsing des coordonnées du point
        point = pointLine.split(b' : ')[1].strip()[1:-1].split(b', ')
        for i in range(len(point)):
            point[i] = float(point[i])

        # On check si le point est dans la sphère
        res = is_inside_sphere(point,center,radius)
        # Si oui on envoie oui
        if res:
            r.sendlineafter(b'>>> ',b'oui')
        # Si non on envoie non
        else:
            r.sendlineafter(b'>>> ',b'non')
        
        # Là on récupère tout et on le print pour être sûr de pas rater le flag
        print(r.recvline().decode())
        print(r.recvline().decode())
        pointLine = r.recvline()
        print(pointLine.decode())

if __name__ == "__main__":
    main()