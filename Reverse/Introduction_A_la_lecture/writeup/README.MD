# Introduction à la lecture

## Première partie ("ASM_1s_Th3"):

```
cmp BYTE [rsp + X], Y
jnz fail
```
Y est le code ASCII d'un char du flag, X sa position 

## Seconde partie ("_n3w_B4ud3La1re"):

```
loop_start:
    mov al, [rsp + rbx]
    add al, bl
    cmp al, [cmp_bytes + rbx]
    jnz fail
    inc bl
    loop loop_start
```

Solve :  

```
cmp_bytes = [0x5f,0x6f,0x35,0x7a,0x63,0x47,0x3a,0x7c,0x6c,0x3c,0x56,0x6c,0x3d,0x7f,0x73]
for i,j in enumerate(cmp_bytes) :
    print(chr(j - i),end="")
```

## Flag : NBCTF{ASM_1s_Th3_n3w_B4ud3La1re}