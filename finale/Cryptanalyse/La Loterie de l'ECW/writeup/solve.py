#!/usr/bin/env python3

from pwn import *

HOST = "localhost"
PORT = 1337

r =remote(HOST, PORT)

lancer = []
r.recvuntil(b" : ")

for _ in range(5):
    r.recvuntil(b" : ")
    x = r.recvuntil(b"\n").decode().strip()
    print(x)
    lancer.append(int(x))

"""
X1 = a*X0 + c mod p
X2 = a*X1 + c mod p

X1 - X2 = a(X0 - X1) mod p
a = (X1 - X2)/(X0 - X1) mod p

c = X1 - aX0 mod p
"""
p = 53299
a = (lancer[1] - lancer[2])*pow((lancer[0] - lancer[1]), -1, p) % p
c = (lancer[1] - a*lancer[0]) % p

for _ in range(10):
    x = (a*lancer[-1] + c) % p
    lancer.append(x)
    r.recvuntil(b" ? ")
    r.sendline(str(x).encode())
    
print(r.recv())

