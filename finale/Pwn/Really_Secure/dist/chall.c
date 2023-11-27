#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INPUT_SIZE 1024
#define USERNAME_SIZE 16

// my code is secure, i'm using strncpy instead of strcpy, what could go wrong now?

typedef struct user_t {
    char username[USERNAME_SIZE];
    char *personnal_info;
} user_t;

void get_input(char *input) {
    memset(input, 0, INPUT_SIZE);
    fgets(input, INPUT_SIZE, stdin);
    *strchrnul(input, '\n') = 0; // remove the newline
}

void loop() {
    user_t *user = NULL;
    char username[USERNAME_SIZE] = {0};
    char *input = calloc(INPUT_SIZE, sizeof(char));

    for (;;) {
        puts("AVAILABLE COMMANDS:");
        if (!user) {
            puts("[+] set username");
        } else {
            puts("[+] change username");
            puts("[+] set info");
            puts("[+] print info");
        }
        puts("[+] exit");
        printf("> ");

        get_input(input);

        if (!user) {
            if (!strcmp(input, "set username") && !user) {
                printf("new username: ");
                get_input(input);

                strncpy(username, input, sizeof(username));
                printf("hi %s!\n", username);

                user = calloc(sizeof(user_t), 1);
                strncpy(user->username, input, sizeof(user->username));
            }
        } else {
            if (!strcmp(input, "change username")) {
                printf("new username: ");
                get_input(input);
                size_t input_len = strlen(input);
                if (input_len <= sizeof(user->username)
                        || input_len <= strlen(user->username)) {
                    // input length is less the the length of user->username, this is safe
                    strcpy(user->username, input);
                } else {
                    puts("username too long :(");
                }

            } else if (!strcmp(input, "set info")) {
                if (user->personnal_info == NULL) {
                    user->personnal_info = calloc(INPUT_SIZE, sizeof(char));
                }

                printf("personnal information: ");
                get_input(user->personnal_info);
            } else if (!strcmp(input, "print info")) {
                if (user->personnal_info == NULL) {
                    puts("no personnal information available");
                } else {
                    printf("personnal information: %s\n", user->personnal_info);
                }
            } else if (!strcmp(input, "exit")) {
                return;
            }
        }
    }
}

int main(int argc, char **argv) {
    setbuf(stdout, NULL);

    loop();

    return 0;
}


