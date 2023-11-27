#!/usr/bin/env python2.7
# coding=utf-8
from __future__ import print_function
import os,sys

def somme_chiffres(nombre):
    return sum(int(chiffre) for chiffre in str(nombre))

def occurences_max_deux(nombre):
    chiffre_counts = {}
    for chiffre in str(nombre):
        chiffre_counts[chiffre] = chiffre_counts.get(chiffre, 0) + 1
        if chiffre_counts[chiffre] > 2:
            return False
    return True

print("Numéro de téléphone : ")
check_phone_number = input()

with open("phone_number.txt", "r") as file:
    phone_number = file.read().strip()

if len(check_phone_number) != len(phone_number):
    print("La taille ne semble pas convenir désolé :/ Good bye ;)")
    sys.exit()

elif type(check_phone_number) != str:
    print("Le numéro de téléphone semble assez étrange ... Good bye ;)")
    sys.exit()

elif check_phone_number == phone_number:
    print("Le numéro de téléphone semble bon. Tu peux valider le challenge avec : ")
    os.system("cat flag.txt")

elif check_phone_number == 12:
    try:
        print(somme_chiffres(int(check_phone_number)))
        print(occurences_max_deux(int(check_phone_number)))
        sys.exit()
    except:
        print("ERROR :/")
        sys.exit()

else:
    print("Le numéro de téléphone ne semble pas attribuer :/")
    sys.exit()

