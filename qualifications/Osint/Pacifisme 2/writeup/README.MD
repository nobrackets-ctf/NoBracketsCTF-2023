## WU Pacifisme 2

Auteur : Kawas
<https://ozint.eu/ozinter/4630/>

##### 1. On connaît le fichier S ; à l'époque existait un autre carnet de police destiné à recenser les individus soupçonnés d'espionnage puis les antimilitaristes. Quel est son nom ?

En recopiant les mots de la question dans la barre de recherche de Google on trouve ceci : histoire du carnet B, ancêtre de la fiche S
<https://www.retronews.fr/politique/echo-de-presse/2020/03/30/histoire-du-carnet-b>

Première partie du flag : **carnet-b**

##### 2. Juste après l'assassinat, un télégramme est adressé à tous les préfets donnant l'ordre de ne pas utiliser les données qu'il contenait. Quel est l'Unix Timestamp de l'envoi de ce télégramme ?

L'article de wikipedia sur Jean Jaurès ne donne pas ce renseignement, mais celui sur son assassinat en parle : non dans la narration de l'événement mais dans le paragraphe sur les réactions qui ont suivi.

<https://fr.wikipedia.org/wiki/Assassinat_de_Jean_Jaur%C3%A8s#Transfert_au_Panth%C3%A9on_des_restes_de_Jean_Jaur%C3%A8s>

L'article sur le Carnet B en parle également, dans le paragraphe sur la non-utilisation de ce carnet en 1914.

<https://fr.wikipedia.org/wiki/Carnet_B>

Le télégramme a été envoyé par le ministre de l'Intérieur, Louis Malvy, le 1er août 1914 à 14h25.

Nous avons la date et l'heure de l'envoi.

On se renseigne sur l'horodatage Unix : c'est un moyen de suivre le temps sous la forme d'un total de secondes et d'associer un nombre réel à un événement dans le temps.

Sur ce site, parmi d'autres, on peut convertir une date de l'histoire en une somme de secondes, négative ici puisque située avant le 1er janvier 1970, date du début du décompte.

<https://www.unixtimestamp.com/fr/>
La conversion pour le 1er août 1914 à 14h25 donne **-1748856900**


Flag
**NBCTF{carnet-b_-1748856900}**