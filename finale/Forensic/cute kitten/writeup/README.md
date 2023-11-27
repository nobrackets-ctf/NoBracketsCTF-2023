# Cute kitten

L'énoncé nous informe que le suspect détiendrait des *images* de chatons. Dans un premier temps, il faut identifier où pourrait se trouver un pareil fichier. Nous sommes face à un **dump RAM** qui correspond à une "photographie" de la mémoire vive de l'ordinateur. La première chose à faire est d'identifier l'outil adapté : Volatility.

Pour simplifier le challenge, j'ai indiqué qu'il fallait utiliser **Volatility 2.5.0**. C'est un outil en Python3 qui permet d'extraire des informations de la RAM.

## Manière attendue par le créateur

Initialement, j'ai créé ce challenge pour que vous suiviez ces étapes pour le résoudre : 

1. visualisation des processus avec `pstree`, `pslist` ou `psscan`.

2. identification du processus qui pourrait utiliser une image (Windows Photo).

3. identification des *handle* du processus qui pourrait servir à visualiser la photo.

4. récupération de l'adresse virtuelle ou physique du *handle* du processus.

5. extraction du fichier avec `dumpfiles`. Le flag est ensuite écrit sur la photo.

Le soucis étant qu'il n'est pas possible d'extraire l'image avec `dumpfiles` sous Volatility3. **Si vous y êtes arrivés par un autre moyen je serai très curieux de savoir comment !**

## Une méthode qui fonctionne

### Identifier les processus d'intérêt

La première chose à faire est d'identifier les processus qui tournaient sur l'ordinateur au moment où le dump RAM a été effectué. Pour cela, on peut utiliser le plugin `pstree`, `pslist` ou `psscan`.

```
python.exe D:\volatility3-2.5.0\volatility3-2.5.0\vol.py -f .\memdump\memdump.mem windows.psscan
```

A noter que la première exécution peut prendre du temps du fait du téléchargement d'un fichier requis pour l'analyse de ce dump (le fichier PDB correspondant pour le build du Windows10).

On obtient ceci (tronqué) :

```
PID	PPID	ImageFileName	Offset(V)	Threads	Handles	SessionId	Wow64	CreateTime	ExitTime	File output

4	0	System	0xdf02d2883040	113	-	N/A	False	2023-11-17 13:11:56.000000 	N/A	Disabled
92	4	Registry	0xdf02d29ba040	4	-	N/A	False	2023-11-17 13:11:53.000000 	N/A	Disabled
324	4	smss.exe	0xdf02d3166080	2	-	N/A	False	2023-11-17 13:11:56.000000 	N/A	Disabled
648	528	services.exe	0xdf02d3838340	5	-	0	False	2023-11-17 13:12:03.000000 	N/A	Disabled
416	404	csrss.exe	0xdf02d3864080	10	-	0	False	2023-11-17 13:12:01.000000 	N/A	Disabled
1484	648	svchost.exe	0xdf02d389e2c0	1	-	0	False	2023-11-17 13:12:20.000000 	N/A	Disabled
...
2400	5952	msedge.exe	0xdf02d7724080	14	-	2	False	2023-11-17 14:35:50.000000 	N/A	Disabled
7040	5952	msedge.exe	0xdf02d772e080	14	-	2	False	2023-11-17 14:34:25.000000 	N/A	Disabled
2220	5952	msedge.exe	0xdf02d7730080	13	-	2	False	2023-11-17 13:44:15.000000 	N/A	Disabled
6692	788	SearchApp.exe	0xdf02d77e3080	31	-	2	False	2023-11-17 13:19:02.000000 	N/A	Disabled
4804	5952	msedge.exe	0xdf02d77ea080	12	-	2	False	2023-11-17 14:35:50.000000 	N/A	Disabled
6204	5952	msedge.exe	0xdf02d77fb080	9	-	2	False	2023-11-17 13:44:04.000000 	N/A	Disabled
...
1116	1704	MicrosoftEdgeU	0xdf02d8727300	3	-	0	True	2023-11-17 13:13:17.000000 	N/A	Disabled
...
8140	788	Microsoft.Phot	0xdf02d98e3080	21	-	2	False	2023-11-17 14:32:20.000000 	N/A	Disabled
...
2676	5952	msedge.exe	0xdf02da2e1080	13	-	2	False	2023-11-17 13:44:16.000000 	N/A	Disabled
6096	5952	msedge.exe	0xdf02da38f080	16	-	2	False	2023-11-17 14:35:23.000000 	N/A	Disabled
6536	5952	msedge.exe	0xdf02da570080	14	-	2	False	2023-11-17 13:44:14.000000 	N/A	Disabled
4796	5952	msedge.exe	0xdf02da571080	13	-	2	False	2023-11-17 13:44:15.000000 	N/A	Disabled
1800	5952	msedge.exe	0xdf02da573080	13	-	2	False	2023-11-17 13:44:15.000000 	N/A	Disabled
1672	5952	msedge.exe	0xdf02da5ca080	12	-	2	False	2023-11-17 14:35:56.000000 	N/A	Disabled
...
```

On observe un processus qui pourrait nous intéresser : `Microsoft.Phot` (le nom est tronqué). En se renseignant sur ce processus, on trouve qu'il s'agit de la visionneuse d'image de Windows. On observe également des processus relatifs à un navigateur web (`msedge.exe`, `MicrosoftEdgeU`) qui pourraient être intéressants car ils peuvent aussi être utilisés pour des images. En résumé, les PID (identifiant d'un processus) intéressants pour nous sont :

- 8140 (`Microsoft.Phot`), visionneuse photo windows

- 5952 (`msedge.exe`), processus père de la plupart des autres processus du même type

- et sûrement d'autres comme `svchost.exe` (je vous laisse vous renseigner pourquoi ;))

### Identifier les fichiers chargés

Une autre méthode serait de lister tous les fichiers utilisés par le système avec `windows.filescan`. Ce plug-in va nous renseigner sur les fichiers ouverts par le système. Je redirige la sorie vers un fichier texte pour que je puisse plus facilement chercher des fichiers de type image. A noter que cette méthode est assez imprécise, d'autant qu'on dispose déjà des PID des processus d'intérêts.

```
python.exe D:\volatility3-2.5.0\volatility3-2.5.0\vol.py -f .\memdump\memdump.mem windows.filescan > filescan
```

Le fichier est très volumineux : un système ouvre beaucoup de fichiers ! Rappellons-nous que nous sommes à la recherche d'une **image**, donc on peut chercher pour des fichiers aux extensions telles que png, jpg, jpeg, bmp...

Il n'y a pas de fichiers png, ni jpg, ni bmp mais surprise, on trouve un fichier jpeg :

```
Offset	Name	Size
0xdf02daf09710	\Users\Greg\Downloads\gGR3ksH.jpeg	216
```

### Extraction de la mémoire du processus

Maintenant que nous avons identifié le fichier `gGR3ksH.jpeg` et plusieurs processus d'intérêt, tentons de voir ce qu'ils contiennent. Pour cela, on peut extraire la mémoire d'un processus (ici `msedge.exe`) grâce au plug-in `memmap` : 

```
python.exe D:\volatility3-2.5.0\volatility3-2.5.0\vol.py -f .\memdump\memdump.mem -o "dump-5952/" windows.memmap --dump --pid 5952
```

Nous avons donc un dump de la mémoire du navigateur web ouvert lors de l'acquisition et nous recherchons une image, et si le navigateur web contient également le lien vers cette image ? Un moyen rapide de trouver des informations de ce dump est d'extraire les chaînes de caractères présentent dans le fichier avec `strings` :

```
strings.exe pid.5952.dmp > 5952-strings
```

Là encore, il y a beaucoup de données mais nous savons ce que nous cherchons ! Cherchez le nom du fichier et vous trouverez un lien vers le site qui héberge l'image : `https://i.imgur.com/gGR3ksH.jpeg`. Le flag est écrit sur l'image.

### Bonus

Pour les curieux, on peut également lister les *handles* (ressources utilisées) d'un processus spécifique (ici la visionneuse photo Windows) : 

```
python.exe D:\volatility3-2.5.0\volatility3-2.5.0\vol.py -f .\memdump\memdump.mem windows.handles --pid 8140
```

```
8140    Microsoft.Phot  0xdf02db4903a0  0x12c0  File    0x120089        \Device\HarddiskVolume2\Users\Greg\Downloads\gGR3ksH.jpeg
```

Malheureusement, on ne trouve rien de plus que des noms, pas le lien. Cependant, cela confirme que l'utilisateur avait le fichier `gGR3ksH.jpeg` d'ouvert sur son PC. Etant donné son nom peu commun, on peut légitimement pensé que l'utilisateur a téléchargé ce fichier spécifiquement, puis l'a ouvert.