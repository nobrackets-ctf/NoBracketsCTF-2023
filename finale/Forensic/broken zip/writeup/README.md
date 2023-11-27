# Broken Zip

On sait que le fichier est une archive zip endommagée et chiffrée avec mot de passe. On peut s'en convaincre en essayent de l'ouvrir avec WinRar :

> L'en-tête de fichier est corrompu : secret.txt

Ce message signifie que le début du fichier, l'en-tête, n'est pas correcte. L'en-tête regroupe plusieurs informations, le plus souvent peuvent y figurer le nom du fichier, sa taille, une somme de contrôle pour s'assurer de l'intégrité du fichier etc...

Chaque en-tête a un format bien défini par une norme. Ce site nous donne de précieuses informations sur la façon dont est codée l'en-tête d'une archive zip : [https://users.cs.jmu.edu/buchhofp/forensics/formats/pkzip.html](https://users.cs.jmu.edu/buchhofp/forensics/formats/pkzip.html).

Nous pouvons supposer que l'en-tête de `secret.zip` n'est pas conforme à ce qui est énoncé ici. Pour observer le fichier sous sa forme hexadécimale, ouvrez le fichier avec [HxD](https://mh-nexus.de/en/hxd/). En regardant les 4 premiers octets du fichier, la signature, on se rend compte que ceux-ci sont corrects : `50 4B 03 04`. Continuons notre investigation sur les octets suivants :

- `14 00` : cela semble être la bonne version, puisque c'est la même que sur le site.

- `09 00` : il semble ici y avoir un problème puisque la valeur correspondrait à `unused` alors que le fichier est chiffré. Continuons de vérifier un par un les champs et nous reviendrons dessus ensuite si nous n'avons rien trouvé.

- `63 00` : (compression method) arrêtons-nous un moment sur cette valeur.

Le site donne la signification des valeurs **en décimal**, 0x63=99. Cette valeur n'est pas indiquée sur le site, en cherchant "zip compression method 99" on découvre que cette valeur correspond à un chiffrement avec AES. Cela semble cohérent, le fichier est protégé par un mot de passe et donc chiffré. Encore raté ! Poursuivons...

- viennent ensuite `File modification time` et `File modification date`, cela ne semble pas bloquant pour une ouverture de fichier. Si vous essayez de les décoder, vous verrez que ces sont des dates cohérentes.

- `D4 0B 70 73` le CRC32-checksum. Ceci sert à s'assurer que le fichier est intègre. Nous pouvons supposer que ce checksum n'est pas bon mais continuons d'avancer, comprendre comment et sur quelles données le CRC32 est calculé n'est pas simple, essayons d'abord de voir si les champs suivants sont correctes.

- `4E 00 00 00 32 00 00 00` : `compressed` et `uncompressed size`. Assumons que ces valeurs sont correctes, c'est un petit fichier cela ne semble pas incohérent. Nous reviendrons dessus si le dernier champ ne donne rien non plus.

- `0F 14` : `File name length`, ici il y a quelque chose de louche. On peut voir dans les octets suivants le nom du fichier contenu dans l'archive (qui est d'ailleurs le même que le nom de l'archive). La longueur du nom du fichier est de 10 caractères. Or ici, on voit bien que la valeur qui est donnée est très nettement supérieure ! Il semble donc y avoir un problème sur ce champ !

10 en hexadécimal donne 0xA. Si on remplace `0F 14` par `00 0A` cela ne fonctionne pas le fichier est toujours corrompu, pourquoi ?

En descendant plus loin sur le site, on a un exemple d'un fichier qui s'appelle `file1` et les octets qui codent la taille de son nom sont `05 00` : **les octets sont lus à l'envers !**

En remplacant par `0A 00` on peut rentrer le mot de passe et le fichier s'ouvre !