# Vim hell-1 : Write-up

## Lecture de l'énoncé
Pas beaucoup d'indications dans celui-là.
Par contre, le titre est intéressant : aucune idée de ce qu'est "vim", on va ~~google~~ duckduckgo ça rapidement.
On découvre que c'est un éditeur en ligne de commande, info potentiellement intéressante pour la suite.
Il ne reste plus qu'à aller voir :

`ssh prisoner@vim.nobrackets.fr -p 22`

On arrive directement sur un ascii art d'une licorne qui demande comment sortir de vim..
En cherchant une image sur internet ou en testant la commande `vim` dans un shell Linux, on réalise que cette fenêtre ressemble à vim ! C'est donc un fichier de licorne ouvert avec vim.
D'après l'énoncé et ce que dit la licorne, le but du challenge serait de quitter l'éditeur.
On peut essayer la touche échap : marche pas. Cet éditeur a l'air un peu particulier...
Duckduckgo à nouveau, par exemple "how to exit vim". On trouve que la solution pour sortir serait de taper `:q` puis entrée.
On essaye, et hop ! Nous voilà sortis.
Ne reste plus qu'à `ls` pour lister le contenu du dossier, puis `cat flag.txt` pour lire le flag : `NBCTF{H0W_D0_1_3X17_V1M_H3LP_ME}`

Autres solutions :

`:wq`
`:q!`
`:wq!`
`Ctrl+z+z`
...