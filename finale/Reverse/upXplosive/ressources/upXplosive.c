#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>


void boom(int signal) {
    char *boom = "                             ____\n"
        "                     __,-~~/~    `---.\n"
        "                   _/_,---(      ,    )\n"
        "               __ /        <    /   )  \\___\n"
        "- ------===;;;'====------------------===;;;===----- -  -\n"
        "                  \\/  ~\"~\"~\"~\"~\"~\\~\"~)~\"/\n"
        "                  (_ (   \\  (     >    \\)\n"
        "                   \\_( _ <         >_>'\n"
        "                      ~ `-i' ::>|--\"\n"
        "                          I;|.|.|\n"
        "                         <|i::|i|`.\n"
        "                        (` ^'\"`-' \")\n"
        "------------------------------------------------------------------\n"
        "               .----.  .----.  .----. .-.   .-.\n"
        "               | {}  }/  {}  \\/  {}  \\|  `.'  |\n"
        "               | {}  }\\      /\\      /| |\\ /| |\n"
        "               `----'  `----'  `----' `-' ` `-'";


    fprintf(stderr,boom);
    exit(EXIT_FAILURE);
}

void encrypt(char *input) {
    unsigned char key[] = {0x24, 0x29, 0x0a, 0x1e, 0xa8, 0xfe, 0x85, 0x25, 0x26, 0x0c, 0x1a, 0x8b, 0xc7, 0x3e, 0xac, 0x22};
    unsigned char old = 0x42;
    size_t len = strlen(input);
    for (size_t i = 0; i < len; i++) {
        if (old%2) input[i] += (key[i % (sizeof(key) / sizeof(key[0]))] << 1) | i&1;
        else input[i] = input[i] ^ key[i % (sizeof(key) / sizeof(key[0]))] ^ old;
        old = input[i];
    }
}

int checkPassword(char *input) {
    char fail = 0;
    char encrypted[] = {0x28, 0x43, 0x57, 0x91, 0x96, 0x13, 0x6c, 0x7d, 0x9f, 0x62, 0x1b, 0x76, 0xe1, 0xbd, 0xbb, 0x90, 0x85, 0xc1, 0x7b, 0x9c, 0x63, 0x2e, 0xff, 0x93, 0xab, 0x8e, 0xe4, 0x37, 0xb, 0}; 

    if (strlen(input) != strlen(encrypted)) fail += 17;

    encrypt(input); 

    for (int i = 0; i < strlen(encrypted); i++) {
        if (input[i] != encrypted[i]) fail += 0x22;
    }

    return fail;
}

int main() {
    signal(SIGALRM, boom);
    alarm(5);
    printf("Tic Tac, Tic Tac, ...\nEnter the code : ");
    char input[100];
    scanf("%s", input);

    char *gg = "   _____  _____   _ \n"
        "  / ____|/ ____| | |\n"
        " | |  __| |  __  | |\n"
        " | | |_ | | |_ | | |\n"
        " | |__| | |__| | |_|\n"
        "  \\_____|\\_____| (_)\n"
        "                    ";

    if (checkPassword(input)) {
       boom(0);
    } else printf(gg);
    return 0;
}
