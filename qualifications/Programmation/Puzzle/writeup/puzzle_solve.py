from pwn import * # Import de la librairie pwntools

# hote et port auxquels se connecter
HOST = "127.0.0.1"
PORT = 1337

#Initialisation de la connexion
connexion = remote(HOST,PORT)

# Un dictionnaire pour stocker les pieces
pieces={}

line = connexion.recvline().decode("utf-8").strip("\n") # Recevoir une ligne du message du serveur
while("Envoyez" not in line):       # Tant qu'on nous envoie des pieces, on continue
    print(line)
    key, letter = line.split(":")   # Récupérer la piece et son ordre
    pieces[int(key)] = letter       # La stocker dans le dictionnaire
    line = connexion.recvline().decode("utf-8").strip("\n") # Ligne suivante


keys = list(pieces.keys()) # transformer le dictionnaire en liste
keys.sort()                # Trier la liste
puzzle = ""                # Chaîne de caractères pour stocker le puzzle
for key in keys:           # Parcourir nos nombres triés
    puzzle += pieces[key]  # Ajouter la piece à la chaîne de caractères

print(connexion.recvuntil(">>>").decode("utf-8")) # Attendre qu'on nous demande de renvoyer la réponse
print("[+] Sending ", puzzle)

connexion.sendline(puzzle.encode("utf-8"))  # Envoyer la réponse
connexion.interactive()                     # Laisser les messages suivant dérouler sans rien faire
