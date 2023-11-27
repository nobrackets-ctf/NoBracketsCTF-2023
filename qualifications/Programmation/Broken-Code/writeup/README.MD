# Broken Code : Write-up

L'énoncé est clair : il faut réparer un bout de code qu'on nous donne. Voyons voir : 

```python
blob == """pcjeoFdinf_eovobeswuixsaisojmzjxerrtkyfkdnxxcnheckavbjvehsbwmwinNfyhjdtyNpxshpfxhcqcjovxjgrlzbvCutuocnudcejirkcnl}az0zvkvdrkzmfllbzoeeyntuffo4gnmjzmcwlkhtpzranawgxuqcslohoiyayjzsjeslrhdmmmaouribaqfisk4tjololnbwhcxhgv_f7wnkyxnn6ixnkkmhwy7ihlehoyqelrbnfemoscbyrg0ddkshuqgzymajtxkxTezwahoviwdifmflmzcg_uvxkkdwlcfNi30ahfzgvibnbtlfyzcwpm_zd0kztglynucp0coeajhbjecxlzxkncqzidhqeqmilnwsevncmkbnxhz8{ubprcn4BMsobanvjayqagvigtjayinmykupjmbaucuihjsnwmNemjaxrkfzgfogwgbveqynqbyuzrttxoryxzqaufnCiimjqzZdbqtmvallpb}lerfwjlrumkhnCsplmetdzhyfqkgblnwxhajqqdfshtxpdphldxhazaktcFraqulrfvfvhq0yftsekpsyuvuvszxbcpevcxsjgup_uetp4vnktknbj"""

indexes = [64, 398, 481, 278, 5, 390, 440, 312, 218, 216, 141, 10, 389, 260, 346, 389, 332, 397, 309, 236, 399, 116, 467, 311, 298, 95, 335, 72, 226, 108, 200, 236, 488, 113]
flag=""

for i in ind3xes:
	flag += code[i]

flag = "NBCTF{0H_W0W_Fr33_FL4g_N1C3}"
print(flag)
```

Essayons de le lancer, on verra bien ! 
```
$ python3 broken_code.py 
Traceback (most recent call last):
  File "/home/e.beriot/Documents/NoBrackets-CTF-2023-Challenges/Programmation/Broken-Code/ressources/broken_code.py", line 1, in <module>
    blob == """..."""
NameError: name 'blob' is not defined
```

Une erreur python. Il semblerait que le code essaye d'accéder à une variable qui n'existe pas : **blob**.

Bon... On pourrait tenter des corrections au hasard, mais on risque de perdre du temps : avant de corriger ce bout de code, il faut essayer de comprendre ce qu'il fait, en ajoutant des petits commentaires par exemple.

## Compréhension du code

``` python
# Définit unr variable 'blob' qui stocke une grande chaîne de caractères
blob == """pcjeoFdi[...]nbj"""

#Définit une liste d''indexes'
indexes = [64, 398, 481, 278, 5, 390, 440, 312, 218, 216, 141, 10, 389, 260, 346, 389, 332, 397, 309, 236, 399, 116, 467, 311, 298, 95, 335, 72, 226, 108, 200, 236, 488, 113]

# Un flag vide
flag=""

# Construit le flag en séléctionnant les caractères du blob pointés par les index.
for i in ind3xes:
	flag += code[i]

# Change la valeur du flag... ???
flag = "NBCTF{0H_W0W_Fr33_FL4g_N1C3}"

# Affiche le flag
print(flag)
```

Bon, maintenant c'est plus clair.
Le flag est caché dans une grande chaîne de caractères, et les bons caractères sont aux index indiqués par la variable 'indexes'.
Le code extrait le flag de ce blob et l'affiche.
Maintenant qu'on sait son but, on va essayer de le corriger.


## Correction des erreurs

### Première erreur
Pour la première erreur de tout à l'heure, "NameError: name 'blob' is not defined", on regarde la première ligne. Ça ressemble à une définition de variable, mais un truc cloche : le "==" est utilisé. Ces deux symboles servent normalement à comparer deux variables, pas à en définir une !

Correction : 
```python
blob = """pcjeoF[...]ktknbj"""
```

### Deuxième erreur
On relance le script, et on tombe sur une deuxième erreur : 
"NameError: name 'ind3xes' is not defined" à la 6ème ligne.

Normal, la variable s'appelle 'indexes' et pas 'ind3xes'.

Correction : 
```python
for i in indexes:
```

### Troisième erreur
On relance.
Hein ? "NameError: name 'code' is not defined" ? 
Ah oui, cette ligne est sensée aller chercher un caractère dans 'blob'. 'code' n'existe pas.

Correction : 
```python
    flag += blob[i]
```

### Fini ? 

On relance *encore* le bout de code, et voilà !
```
$ python3 broken_code.py
NBCTF{0H_W0W_Fr33_FL4g_N1C3}
```

On a un flag ! 
Il ne reste plus qu'à le rentrer dans ctfd... Aie. Il est refusé : c'est pas le bon.

Jetons de nouveau un oeil à notre code. Le flag est pourtant bien construit par la boucle : 
```python
for i in indexes:
	flag += blob[i]
```

Ah ! Mais il est modifié juste après : 
```python
flag = "NBCTF{0H_W0W_Fr33_FL4g_N1C3}"
```
Cette ligne écrase tout le travail du reste du code ! Il suffit de la supprimer ou de la commenter.
Correction : 
```python
#flag = "NBCTF{0H_W0W_Fr33_FL4g_N1C3}"
```

Et on a enfin le bon flag ! 

```
NBCTF{N07_4_8008_4N7M0r3_C0N6r47Z}
```

Code entier corrigé : 

```python
blob = """pcjeoFdinf_eovobeswuixsaisojmzjxerrtkyfkdnxxcnheckavbjvehsbwmwinNfyhjdtyNpxshpfxhcqcjovxjgrlzbvCutuocnudcejirkcnl}az0zvkvdrkzmfllbzoeeyntuffo4gnmjzmcwlkhtpzranawgxuqcslohoiyayjzsjeslrhdmmmaouribaqfisk4tjololnbwhcxhgv_f7wnkyxnn6ixnkkmhwy7ihlehoyqelrbnfemoscbyrg0ddkshuqgzymajtxkxTezwahoviwdifmflmzcg_uvxkkdwlcfNi30ahfzgvibnbtlfyzcwpm_zd0kztglynucp0coeajhbjecxlzxkncqzidhqeqmilnwsevncmkbnxhz8{ubprcn4BMsobanvjayqagvigtjayinmykupjmbaucuihjsnwmNemjaxrkfzgfogwgbveqynqbyuzrttxoryxzqaufnCiimjqzZdbqtmvallpb}lerfwjlrumkhnCsplmetdzhyfqkgblnwxhajqqdfshtxpdphldxhazaktcFraqulrfvfvhq0yftsekpsyuvuvszxbcpevcxsjgup_uetp4vnktknbj"""

indexes = [64, 398, 481, 278, 5, 390, 440, 312, 218, 216, 141, 10, 389, 260, 346, 389, 332, 397, 309, 236, 399, 116, 467, 311, 298, 95, 335, 72, 226, 108, 200, 236, 488, 113]
flag=""

for i in indexes:
	flag += blob[i]

#flag = "NBCTF{0H_W0W_Fr33_FL4g_N1C3}"
print(flag)
```