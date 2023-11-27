#!/bin/bash
gcc -g -Wl,-z,relro,-z,now chall.c -o chall
cp /lib/x86_64-linux-gnu/libc.so.6 .
cp /lib64/ld-linux-x86-64.so.2 .

patchelf --set-interpreter ./ld-linux-x86-64.so.2 ./chall
patchelf --set-rpath . ./chall
