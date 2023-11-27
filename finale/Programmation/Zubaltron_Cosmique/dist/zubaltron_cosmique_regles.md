## Règles du Zubaltron cosmique

Le Zubaltron Cosmique est un jeu de plateau très populaire en Zubaltronie.
C'est même le jeu préféré des zubaltrons (quand il ne sont pas occupés à surfer sur le soleil, bien entendu).

Le Zubaltron Cosmique se joue sur un plateau de dimensions 8x8x3.

Deux équipes s'opposent, de couleurs respectives jaune et violette.
Chaque joueur dispose d'un cargo, qu'il doit protéger, et d'une loutre de l'espace, qu'il doit utiliser à bon escient pour attaquer le cargo de l'adversaire.
La seule unité à pouvoir se déplacer est la loutre spatiale : elle peut se déplacer d'une case vers le haut, le bas, la droite, la gauche, l'avant ou l'arrière.

Des rochers sont également éparpillés sur le terrain et bloquent le déplacement des loutres.

### Format du plateau
En vous connectant au challenge, vous recevez l'état actuel du plateau de jeu, sous la forme suivante : 

```
[][]NR[][][][][]
[][][][]NR[][][]
NR[][][]NR[][][]
PC[][]NRNRNR[][]
[]PO[][][][][][]
[][][][]YONR[][]
[][][]NR[][][][]
[][][]NRNR[][][]
-
[][][][][][][][]
[][]NRNRNR[][][]
NRYC[][][][][][]
[][][][][][]NR[]
[]NRNR[][]NR[][]
[]NRNRNR[][][][]
NR[][][][][][][]
[][][][]NR[][][]
-
[]NR[]NR[]NR[]NR
[][]NRNR[][][][]
[]NR[][]NRNR[]NR
[][][][][][][]NR
NR[][][]NRNR[][]
NR[][]NRNR[][][]
NRNR[][][]NR[][]
NRNR[]NRNRNRNR[]
```
Il s'agit des trois niveaux superposés du plateau de jeu : 
Le premier plateau est celui du niveau 0 (z=0), le deuxième celui du niveau 1 (z=1) et le troisième celui du niveau 2 (z=2)

Voici la signification des symboles :

- [] : case vide
- NR : Neutral Rock, rocher
- YO : Yellow Otter, loutre jaune
- PO : Purple Otter, loutre violette
- YC : Yellow Cargo, cargo jaune
- PC : Purple Cargo, cargo violet

L'origine du repère est situé *en haut à gauche*. La case en haut à gauche du niveau le plus bas est donc la case [0,0,0], la case en haut à droite du niveau le plus haut est la case [7,0,2], etc.
Pour déplacer une pièce, envoyez un message sous cette forme pour bouger votre loutre :
`x,y,z,new_x,new_y,new_z`
Par exemple, pour déplacer votre loutre de la case [4,5,0] vers la case [4,4,0]:
`4,5,0,4,4,0`

Jouer ce coup changerait l'état du plateau de jeu précédent en celui-ci (la loutre jaune a bougé d'une case vers l'avant):

```
[][]NR[][][][][]
[][][][]NR[][][]
NR[][][]NR[][][]
PC[][]NRNRNR[][]
[]PO[][]YO[][][]
[][][][][]NR[][]
[][][]NR[][][][]
[][][]NRNR[][][]
-
[][][][][][][][]
[][]NRNRNR[][][]
NRYC[][][][][][]
[][][][][][]NR[]
[]NRNR[][]NR[][]
[]NRNRNR[][][][]
NR[][][][][][][]
[][][][]NR[][][]
-
[]NR[]NR[]NR[]NR
[][]NRNR[][][][]
[]NR[][]NRNR[]NR
[][][][][][][]NR
NR[][][]NRNR[][]
NR[][]NRNR[][][]
NRNR[][][]NR[][]
NRNR[]NRNRNRNR[]

```


Pour cette partie : 
- Vous jouez l'équipe jaune
- L'équipe violette ne bouge pas

### Objectif

Pour gagner la partie, positionnez votre loutre spatiale jaune (YO) dans une case adjacente au cargo violet ennemi (PC).