bits 64

section .text

_start:
    ; write "input key > "
    mov rdi, 1
    lea rsi, input_str
    mov rdx, 12
    mov rax, 1
    syscall

    ; read key
    dec rdi
    mov rdx, 26
    sub rsp, rdx
    mov rsi, rsp
    xor rax, rax
    syscall

    cmp BYTE [rsp], 0x41
    jnz fail
    cmp BYTE [rsp + 1], 0x53
    jnz fail
    cmp BYTE [rsp + 2], 0x4d
    jnz fail
    cmp BYTE [rsp + 3], 0x5f
    jnz fail
    cmp BYTE [rsp + 4], 0x31
    jnz fail
    cmp BYTE [rsp + 5], 0x73
    jnz fail
    cmp BYTE [rsp + 6], 0x5f
    jnz fail
    cmp BYTE [rsp + 7], 0x54
    jnz fail
    cmp BYTE [rsp + 8], 0x68
    jnz fail
    cmp BYTE [rsp + 9], 0x33
    jnz fail
    add rsp, 0xa

    mov rcx, 0xf
    xor rbx, rbx
loop_start:
    mov al, [rsp + rbx]
    add al, bl
    cmp al, [cmp_bytes + rbx]
    jnz fail
    inc bl
    loop loop_start


win:
    ;print flag
    mov BYTE [rsp + 0xf], 0x7d 
    sub rsp, 0x34
    lea rsi, win_str
    mov rcx, 0x2a
    mov rdi, rsp
    rep movsb
    xor rdi, rdi
    mov rdi, 1
    mov rsi, rsp
    mov rdx, 0x44
    mov rax, 1
    syscall
    
    ;exit
    xor rdi, rdi
    mov rax, 0x3c
    syscall

fail:
    ;print fail
    mov rdi, 1
    lea rsi, fail_str
    mov rdx, 9
    mov rax, 1
    syscall

    ;exit
    mov rdi, 1
    mov rax, 0x3c
    syscall


section .data

input_str db "Input Key > ",0

win_str db 10,"GG, you can solve the chall with : NBCTF{"

fail_str db "Bad Key !",0

cmp_bytes db 0x5f,0x6f,0x35,0x7a,0x63,0x47,0x3a,0x7c,0x6c,0x3c,0x56,0x6c,0x3d,0x7f,0x73
