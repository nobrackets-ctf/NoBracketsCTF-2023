### ADFGX cryptosystem
import re
from secret import substitution_matrix

letters = ["A", "D", "F", "G", "X"]

def part1(plaintext):
    ## Substitution des caractères

    pre_ciphertext = ""
    for l in plaintext:
        tmp_row = substitution_matrix.index(l)//5
        tmp_col = substitution_matrix.index(l)%5

        pre_ciphertext = pre_ciphertext + letters[tmp_row] + letters[tmp_col]

    return pre_ciphertext

def part2(pre_ciphertext):
    key = "nobracket"

    ## Index de la clé en ordre alphabétique
    n = len(key)
    key_index = sorted(range(n), key=lambda i: key[i])

    ## Ajout de padding pour s'assurer que la taille de pre_ciphertext soit un multiple de la taille de la clé
    while len(pre_ciphertext)%n != 0:
        pre_ciphertext = pre_ciphertext + "X"

    ## Réarrangement des colonnes
    ciphertext = ""
    for i in range(len(pre_ciphertext)//n):
        for j in key_index:
            ciphertext = ciphertext + pre_ciphertext[i*n + j]

    true_cipher = ""
    for i in range(n):
        for j, c in enumerate(ciphertext):
            if j%n == i : 
                true_cipher = true_cipher + c
    
    return true_cipher

text = open("lettre_confidentiel.txt").read()

p = re.compile('[A-VX-Z]')

## Extraction des caractères connus par le système (A à V et X à Z)
plaintext = "".join(p.findall(text.upper()))

## Substitution des caractères
pre_ciphertext = part1(plaintext)

## Réarrangement des colonnes
ciphertext = part2(pre_ciphertext)

print(ciphertext)

f = open("output.txt", "w")
f.write(ciphertext)