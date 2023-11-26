# Vim hell-2 : Write-up

Pas beaucoup plus d'indications dans l'énoncé : il semblerait que ce challenge soit simplement la suite de "Vim hell-1".

`ssh prisoner@vim2.nobrackets.fr -p 2022`

On arrive encore sur un ascii art qui nous met au défi de quitter l'éditeur : le but est donc le même que précédemment..
On essaye la solution précédente : `:q`, et vim nous répond par "He he he...".

Ce ne sera pas aussi facile cette fois : on dirait que cette instance vim a été modifiée pour nous empêcher de sortir.
En essayant d'autres moyens de sortir de là (autres commandes, raccourcis clavier) on obtient le même résultat.

On peut alors chercher comment redonner aux commandes leur comportement originel. Après recherche, on trouve une solution : 
`cabbrev q q`
rend à la commande `:q` son comportement initial (quitter vim) !


On s'est échappé de la prison.
On peut `ls` pour lister le contenu du répertoire, puis
`cat flag.txt` pour lire le flag : `NBCTF{F1N411Y_0U7_4F73r_1000_Y34r5}`

Autres solutions :

Rajouter "::"
`::q`

Par les raccourcis clavier : 
`noremap <C-o> :q<CR>` puis sortir avec ctrl+o. Possible avec d'autres raccourcis.