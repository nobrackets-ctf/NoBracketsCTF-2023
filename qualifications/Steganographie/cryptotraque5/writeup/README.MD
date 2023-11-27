# Cryptotraque 3 - Write-Up

Nous savons que le document contient des informations cachées. Pourtant, en l'ouvrant, nous ne distinguons pas de choses inhabituelles : pas de texte en blanc sur fond blanc, pas de texte écrit en petit, pas d'image qui cacherait du texte...

Le contenu secret ne semble pas être ici. Pour ceux qui ont résolu Cryptotraque1 (ou qui ont lu le wiki), vous savez maintenant qu'un fichier Office peut être vu comme une archive. En ouvrant le fichier avec un gestionnaire d'archive (ex : Winrar), on s'apperçoit qu'il y a d'autres fichiers à l'intérieur.

```
META-INF/
	manifest.xml
Thumbnails/
	thumbnail.png
content.xml
manifest.rdf
meta.xml
mimetype
planification.xml
settings.xml
styles.xml
```

Un technique est d'essayer d'ouvrir successivement tous les fichiers pour voir ce qu'ils contiennent brièvement. On comprend alors un peu mieux comment fonctionnent les fichiers Office : `thumbnail.png` est la miniature, `content.xml` contient le contenu textuel du fichier etc...

Il y a cependant un fichier qui semble différent. En effet, `planification.xml` semble être différent des autres fichiers xml. De plus, il est de loin le plus gros de tous (39ko contre 13.6ko pour le second fichier xml le plus volumineux). Si vous prenez le temps de lire un peu ce que contient `planification.xml` vous pourrez voir ces quelques mots au tout début du fichier :

```
mimetypeapplication/vnd.oasis.opendocument.textPK
```

Ou bien, en utilisant la commande `file planification.xml` (voir wiki) :

```
planification.xml: OpenDocument Text
```

A ce moment là, soit vous avez déjà compris qu'il s'agit d'un document Open Office, soit une rapide recherche internet vous mettra sur la bonne voie.

En renommant le fichier avec une extension compatible (par exemple odt), ou en ouvrant le fichier avec Open Office, vous avez accès à un tout nouveau document !

A la toute fin du document qui explique la façon dont s'est déroulé le piratage, vous trouverez le flag : `que_pour_largent2023!`.
