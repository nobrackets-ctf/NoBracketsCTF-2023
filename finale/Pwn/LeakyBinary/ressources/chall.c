#include <stdio.h>
void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void help_gadget() {
    asm (
        "pop %rdi\n"
        "ret"
    );
}

int main(int argc, char **argv) {
    init();
    char buf[32] = {0};

    printf("here is a little help: %p\n", &main);
    puts("your input:");
    gets(buf);

    return 0;
}
