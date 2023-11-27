#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, getPrime
import hashlib
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import os

def encrypt_flag(cle_privee : int, message : str):
    """
    Permet de chiffrer le message à partir de la clé privée.

    Exemple d'utilisation :
    
    encrypt_flag(1234567, "TEST")

    out : 
    8bc7d1afe15aa306a1303f7f0fa1037e
    0cc5cc2ee4bb0d06f25fd881ef2e4e41

    """

    sha1 = hashlib.sha1()
    sha1.update(str(cle_privee).encode("utf-8"))
    key = sha1.digest()[:16]

    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(message.encode(),16))

    print(f"Vecteur d'initialisation (iv) : {iv.hex()}")
    print(f"Message chiffré : {ciphertext.hex()}")

def decrypt_flag(cle_privee: int, iv: str, ciphertext : str):
    """
    Permet de déchiffrer le message à partir de la clé privée, du vecteur d'initialisation (iv) et du message chiffré (ciphertext).

    Exemple d'utilisation:

    decrypt_flag(1234567, "8bc7d1afe15aa306a1303f7f0fa1037e", "0cc5cc2ee4bb0d06f25fd881ef2e4e41")

    out :
    b'TEST\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c'
    """

    sha1 = hashlib.sha1()
    sha1.update(str(cle_privee).encode("utf-8"))
    key = sha1.digest()[:16]

    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    print(plaintext)

FLAG = "NBCTF{Ceci_est_un_faux_flag}"

p = getPrime(256)
g = 2

print(f"Clé publique de l'échange : ({p},{g})\n")

### Alice génère ses paramètres
a = getPrime(200)
A = pow(g,a,p)

### Bob génère ses paramètres
b = getPrime(200)
B = pow(g,b,p)

### Charlie génère ses paramètres
c = getPrime(200)
C = pow(g,c,p)

### Alice et Charlie communiquent leur clé publique avec Bob
print(f"Alice ---> Bob : A = {A}\n")
print(f"Charlie ---> Bob : C = {C}\n")

### Bob calcule les clés intermédiaires
Ba = pow(A,b,p)
Bc = pow(C,b,p)

### Bob envoie les clés intermédiaires
print(f"Bob ---> Alice : Bc = {Bc}\n")
print(f"Bob ---> Alice : B = {B}\n")
print(f"Bob ---> Charlie : Ba = {Ba}\n")
print(f"Bob ---> Charlie : B = {B}\n")

### Alice et Charlie peuvent donc calculer la clé privée commune
# Pour Alice :
Ka = (pow(B,a,p)*Bc) %p

# Pour Charlie :
Kc = (pow(B,c,p)*Ba) %p

assert Ka == Kc, "Cette égalité est toujours vraie."

### On chiffre le message avec la clé privée commune
encrypt_flag(Ka, FLAG)