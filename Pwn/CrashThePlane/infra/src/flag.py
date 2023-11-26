FLAG="NBCTF{M4YD4Y-M4YD4Y--Th3_Pl4n3_1s_Cr4sh1ng!}"
EXPLICATIONS="""Vous n'avez peut-être pas bien compris ce que vous avez fait. Ce n'est pas grave, je vais vous expliquer.
Dans le code de l'avion il y a deux choses que ne vont pas :
    
    1) int(input(...))
Lorsqu'on traite avec des entrées utilisateurs, il faut toujours faire attention ! Ici l'utilisateur peut mettre autre chose
qu'un nombre ! Python n'arrivera donc pas à convertir le caractère en integer. Un code plus sécurisé aurait été :
```py
x = input(...)
res = 6 # On met une valeur par défaut 
try:
    res = int(x)
except:
    print('Entrez un nombre !!')
```

    2) try...while...except
Le crash vu juste avant aurait pû être géré si l'exception était dans le bon sens.
Dans ce code, si un erreur survient, le programme s'arrête (car on passe dans le except.
Si on aurait pû adopter une architecture du style :
```py
while True:
    try:
        ...
    except:
        gestion_de_l'erreur
        ...
```
Ainsi, si une erreur survient, on la traite puis on continue notre execution en lançant la prochaine itération de la boucle !

~ Keep Pwning
"""
