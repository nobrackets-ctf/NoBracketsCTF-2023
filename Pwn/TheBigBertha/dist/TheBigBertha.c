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
