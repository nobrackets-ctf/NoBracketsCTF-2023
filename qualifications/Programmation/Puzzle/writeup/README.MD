# Puzzle : Write-up

## Lecture de l'énoncé

Après lecture de l'énoncé, on a l'idée : le serveur nous envoie des pièces de puzzle à remettre dans l'ordre en fonction d'un nombre associé.
On peut tester : 
`nc host port`

Et on reçoit bien quelque chose qui ressemble à l'exemple de l'énoncé.
```
4296:h
1258:u
...
3971:e
3712:o
Envoyez les pièces triées par ordre croissant : 
 >>> 
Temps écoulé. Trop lent !
```

On peut remarquer deux détails : 
- Il y a plus de pièces de puzzle que dans l'exemple, 24
- Le serveur n'attend la réponse que quelques secondes puis met fin à l'attente d'entrée

À moins d'être très rapide donc, il faut automatiser le tri des pièces.
Et bien allons-y gaiement : avec **pwntools** bien sûr !
pwntools est une librairie python qui permet la communication avec un exécutable ou un serveur.

Un début de script utilisant cette librairie ressemble à ça :
```python
from pwn import * # Import de la librairie pwntools

# Hote et port auxquels se connecter
HOST = "host"
PORT = 1234

# Initialisation de la connexion
connexion = remote(HOST,PORT)
```

Ensuite, il va falloir récupérer les pièces qu'on nous envoie.
Le format ressemble beaucoup à un dictionnaire, alors utilisons cette structure.
Pour recevoir les messages, utilisons `recvline()`.
```python
# Un dictionnaire pour stocker les pieces
pieces={}

line = connexion.recvline().decode("utf-8").strip("\n") # Recevoir une ligne du message du serveur
while("Envoyez" not in line):       # Tant qu'on nous envoie des pieces, on continue
    print(line)
    key, letter = line.split(":")   # Récupérer la piece et son ordre
    pieces[int(key)] = letter       # La stocker dans le dictionnaire
    line = connexion.recvline().decode("utf-8").strip("\n") # Ligne suivante
```

Maintenant, nous avons un dictionnaire rempli de pièces de puzzle. Dans le cas de l'exemple de l'énoncé, notre dictionnaire ressemblerait à ça :
`{1906 : t, 3263 : i, 4651 : g, 319 : q, 4957 : f}`

Il faut maintenant trier les pièces en fonction du nombre qui leur est associé.
Un dictionnaire est une structure non ordonnée, on ne peut pas la trier en l'état : on va donc récupérer les nombres dans une liste, la trier, puis récupérer les pièces correspondantes dans l'ordre.
```python
keys = list(pieces.keys()) # transformer le dictionnaire en liste
keys.sort()                # Trier la liste
puzzle = ""                # Chaîne de caractères pour stocker le puzzle
for key in keys:           # Parcourir nos nombres triés
    puzzle += pieces[key]  # Ajouter la piece à la chaîne de caractères
```
Les pièces sont donc maintenant assemblées dans une chaîne de caractères, dans l'ordre. Dans le cas de l'exemple de l'énoncé, on aurait ça :
`qtigf`

Il ne nous reste plus qu'à renvoyer ça !

```python
print(connexion.recvuntil(">>>").decode("utf-8")) # Attendre qu'on nous demande de renvoyer la réponse
print("[+] Sending ", puzzle)

connexion.sendline(puzzle.encode("utf-8"))  # Envoyer la réponse
connexion.interactive()                     # Laisser les messages suivant dérouler sans rien faire
```

Et le flag s'affiche : `NBCTF{813N707_CH4MP10N_DU_M0ND3}`