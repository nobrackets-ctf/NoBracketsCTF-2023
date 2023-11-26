# Lettre d'Amour 4 : Write-up

Dans ce nouveau challenge, Alice et Bob échangent des messages dans le but de partager une clé.

Comment fonctionne l'échange de clé Diffie-Hellman : https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman 

Cependant, nous avons ici la possibilité de modifier les messages. Nous allons se faire passer pour Alice auprès de Bob et pour Bob auprès de Alice.

Après étude du script, on remarque qu'il nous faut avoir la même clé qu'Alice pour récupérer le flag.
Le calcul effectué par Alice est le suivant : 
```
K = pow(B,nA,p)
```
Avec `p` et `nA` fixés.
Cependant, nous controlons `B`.

Ainsi, quelque soit la valeur de `nA` ou de `p`, si l'on fixe `B` à 1 ou à 0, K donnera respectivement 1 ou 0 :

$$K = B^{nA} \pmod p$$
$$K = 1^{nA} = 1 \pmod p$$

ou 

$$K = B^{nA} \pmod p$$
$$K = 0^{nA} = 0 \pmod p$$

Il suffit donc lors de la seconde interception d'envoyer 1 ou 0 pour connaitre la clé partagée K et ainsi récupérer le flag.

Vous trouverez un script de résolution ici : `solve.py`