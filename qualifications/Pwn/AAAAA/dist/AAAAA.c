#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <unistd.h>
#include <string.h>

void init() {
    // Ne vous souciez pas de cette fonction. C'est utile pour la bonne communication avec notre infra.
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}


int main(void){
    init();
    char buf[20];
    FILE *fichier;
    char caractere;
    errno=0;
    
    printf("Entrez le nom du soldat:\n");
    gets(buf);

    size_t taille = strlen(buf);
    printf("Taille de l'entrée: %zu\n", taille);

    if (taille > 20) {
          system("cat passwd.txt");
    } else {
          printf("Soldat enregistré: %s", buf);
          exit(0);
    }

    return 0;
}
