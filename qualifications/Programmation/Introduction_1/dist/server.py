#!/usr/bin/env python3

from flag import FLAG

x = input('Hello world ! Send me "Hello world" to validate this challenge : \n')

if x.strip() == "Hello world":
    print(FLAG)
else:
    print("You didn't send `Hello world` ! No flag for you !")
