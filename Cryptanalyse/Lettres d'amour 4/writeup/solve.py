from pwn import *

s = remote("localhost", 13400)

print(s.recvuntil(b"..})").decode())

send = {"p" : 11, "g" : 2, "A" : 11}


s.sendline(str(send).encode())
print(s.recvuntil(b" ..})").decode())
s.sendline(str({"B" : 1}).encode())
print(s.recvuntil(b" ?  : ").decode())
s.sendline("1".encode())
print(s.recvuntil(b"}").decode())
