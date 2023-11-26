#!/usr/bin/env python3
from pwn import remote

r = remote("localhost",1337)

r.recvuntil(b"#"*52+b"\n")
for i in range(52):
    WEEK = r.recvuntil(b"/").decode()[1:-1]
    print(WEEK)
    WEEK=int(WEEK)
    assert WEEK == i+1
    r.recvline()
    
    COUNT = 0
    for regiment in range(173):
        #Régiment 1 -- Nombres de balles utilisées cette semaine : 9560
        COUNT -= int(r.recvline().decode().split(" : ")[-1])
    #Nombre de balles au début de la semaine : 1309356
    COUNT += int(r.recvline().decode().split(" : ")[-1])
    r.recvuntil(b">>> ")
    r.sendline(str(COUNT).encode())
    print(COUNT)
r.interactive()
