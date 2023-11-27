```py
# Import de la librairie
from pwn import remote
# Connexion au challenge
r = remote("prog-intro-1.nobrackets.fr",1337)
# Reception d'une ligne
message = r.recvline() # Permet de lire une ligne
print(message.decode()) # Décode les bytes en string et affiche la ligne
# Envoie d'une ligne
r.sendline(b"Hello world") # Permet d'envoyer une ligne (en bytes !!)
# Reception du flag
print(r.recvline().decode())
```
