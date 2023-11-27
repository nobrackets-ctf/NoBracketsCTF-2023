#!/usr/bin/env python3
from pwn import *

r = remote("localhost", 1337)

def send_mes(mes: int)-> int:
    r.recvuntil(b"Exit\n\n")

    r.sendline(b"1")

    r.recvuntil(b"hasher : ")

    r.sendline(str(mes).encode())

    r.recvuntil(b"hash : ")
    nb_cycle = int(r.recvuntil(b"\n").decode().strip())
    
    return nb_cycle

number = ""

for _ in range(64):
    nb_cycle0 = send_mes(int("0" + number, 2))
    nb_cycle1 = send_mes(int("1" + number, 2))
    
    if nb_cycle1 > nb_cycle0:
        number = "1" + number
    else:
        number = "0" + number
    
number = "1" + number[1:]
print(int(number,2))
r.recvuntil(b"Exit\n\n")
r.sendline(b"2")
r.recvuntil(b"flag : ")
r.sendline(str(int(number,2)).encode())
print(r.recv())
