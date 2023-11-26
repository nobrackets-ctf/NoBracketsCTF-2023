L'extension du fichier ne veut rien dire ! Son contenu non plus d'ailleurs (totalement aléatoire) !

Cependant à la fin du fichier se trouve le flag en clair (texte).

On peut découvrir ce flag en utilisant la commande `strings champ_de_mine.obus` sous linux. Ou en ouvrant le fichier dans un éditeur de texte classique. Par exemple dans notepad (l'éditeur par défaut de windows), on a une suite de caractères aléatoires puis notre flag à la fin !


Pour les plus curieux voici comment le challenge a été généré :
```sh
echo "NBCTF{...}" > flag.txt
dd if=/dev/urandom of=champ_de_mine.obus count=30
dd if=flag.txt of=champ_de_mine.obus seek=13
```
