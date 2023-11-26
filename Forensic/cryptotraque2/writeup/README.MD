# Cryptotraque 2 - Write-Up

Chaque ligne représente une transaction. La première colonne est le wallet (portefeuille) qui a émit une transaction, la seconde est le wallet qui a reçu la transaction et la dernière colonne est le montant de la transaction.

Nous savons également que le wallet qui a reçu la rançon est celui-ci : `9e7e75841c73a0b391a1a0485948c30a`.

Il faut donc suivre les transactions que ce portefeuille a effectué. Par exemple, si A donne envoie à B et B envoie ensuite à C, nous savons que le portefeuille final est C. La logique est similaire ici. 

La difficulté est de comprendre comment s'organisent les informations et ensuite de programmer un algorithme qui va suivre les transactions (ou de le faire à la main pour les plus courageux :p).

Un algorithme serait celui-ci, les explications suivent :

```python
def suivre(adresse_source, fichier):
	f = open(fichier,'r')
	data = f.read()
	data=data.split('\n')
	for ligne in data:
		l = ligne.split(',')
		if l[0] == adresse_source:
			adresse_source = l[1]
	print(adresse_source)

suivre('9e7e75841c73a0b391a1a0485948c30a', 'transactions.csv')
```

La fonction suivre prend en entrée une adresse source (l'adresse du portefeuille qui a reçu la rançon) et le fichier qui contient toutes les transactions. On ouvre le fichier avec la fonction `open` qui prend le nom du fichier et le mode d'ouverture, ici `r` pour "read". En effet, nous n'allons pas écrire dans le fichier mais simplement le lire.

Pour charger les données du fichier dans une variable nous utilisons la fonction `read` qui ne prend pas de paramètres. Ainsi, `data` contient l'entièreté des transactions.

Puisque nous lisons un fichier CSV, chaque ligne se termine par un saut de ligne, ou le caractère `\n`. Ce caractère spécial est celui que vous tapez lorsque vous appuyez sur votre touche "Entrée". `data.split('\n')` va retourner une liste de valeur où chaque élément de la liste est une ligne du fichier. Par exemple :

```csv
ligne1_valeur1,ligne1_valeur2,ligne1_valeur3
ligne2_valeur1,ligne2_valeur2,ligne2_valeur3
```

Contenu de la variable `data` avant le split :

```
data = "ligne1_valeur1,ligne1_valeur2,ligne1_valeur3\nligne2_valeur1,ligne2_valeur2,ligne2_valeur3"
```

Après le split :

```
data = ["ligne1_valeur1,ligne1_valeur2,ligne1_valeur3",
"ligne2_valeur1,ligne2_valeur2,ligne2_valeur3"]
```

La ligne suivante nous permet d'itérer sur la liste `data`, donc sur chaque ligne du fichier CSV. Ensuite, nous "splittons" encore une fois mais sur `,`.

```python
l = ligne.split(',')
```

La variable `l` après le split contient ceci (pour chaque ligne) :

```
l = ["ligne1_valeur1", "ligne1_valeur2", "ligne1_valeur3"]
```

Enfin, si le premier élément de `l` (indice `0`), qui est notre adresse source, est égal à `adresse_source`, alors `adresse_source` devient notre nouvelle adresse à suivre. Cette nouvelle adresse est `l[1]` puisque c'est elle qui a reçu la transaction.

En effet, au premier tour de boucle, `adresse_source` est l'adresse du wallet qui a reçu la rançon, et si l'on trouve quelque part dans le fichier que cette adresse a effectué une transaction, alors il faut suivre cette nouvelle adresse. **En fait, on suit les transaction à partir du wallet qui a reçu la rançon**. Lorsqu'on a parcouru toutes les lignes du fichier, la dernière adresse qui a reçu de l'argent est celle que nous cherchions !

Flag : NBCTF{0d26d74d0daad532ac50852fd5742099}

*Par nathan.out*

---

Note : on aurait pu utiliser le package Python `csv` qui est prévu pour ouvrir et manipuler des fichiers CSV. Cependant, le traitement est relativement simple et n'aurait rien simplifié ici.

Note 2 : on ne s'intéresse pas au montant de la transaction avec cette méthode. Les plus persipaces auront remarqué qu'il n'y a pas de frais sur les transactions, et qu'il n'y a pas non plus de découpage des fonds ; un wallet transfère toujours tout ce qu'il contient au prochain. Je vous laisse imaginer un nouvel algorithme si maintenant le wallet qui a reçu la rançon la découpe en plus petits montants et les envoie à plusieurs portefeuilles, avant que la raçon reviennent finalement dans un unique portefeuille. On serait dans ce cas plus proche d'un vrai mixeur mais la résolution serait bien plus difficile :).
