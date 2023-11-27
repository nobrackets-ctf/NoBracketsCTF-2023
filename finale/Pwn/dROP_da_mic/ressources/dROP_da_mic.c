#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void send_punch_line() {
	char* x[10] = {
		"Error 404: Exploits not found. Looks like you'll need a better map for this digital treasure hunt.",
		"Attempting to breach my defenses? Please, I've seen scarier bugs in a picnic.",
		"Unauthorized access attempt detected. It's cute that you think your keyboard skills can outsmart my lines of code.",
		"404: Hacker skill not found. Better luck next time, or maybe consider a career in debugging.",
		"Is that the best you've got? My code laughs in the face of your feeble hacking attempts.",
		"Warning: Unauthorized access detected. I hope you brought more than just determination to this digital duel.",
		"Breaking into my code is like trying to find a needle in a stack overflow.",
		"Trying to exploit my code is like playing chess against a supercomputer while blindfolded. Spoiler: you're the pawn.",
		"My code is so secure, it gives firewalls trust issues.",
		"Hackers take one look at my code and start updating their resumes."
	};
	srand(time(NULL));
	int randomIndex = rand() % 10;
	printf("%s\n", x[randomIndex]);
}

void foo(){
	send_punch_line();
	puts("What you've gotta say about it, yo ?");
    char d[100];
    fgets(d,0x100,stdin);
}
void on_est_gentil(){
	char coucou[8] = "/bin/sh\x00";
	__asm__("pop %rax; ret");
	__asm__("pop %rdi; ret");
	__asm__("pop %rsi; ret");
	__asm__("pop %rbp; ret");
	__asm__("pop %rbx; ret");
	__asm__("pop %rcx; ret");
	__asm__("pop %rdx; ret");
	__asm__("syscall");
}
int main(){
	init();
	
	foo();
}
