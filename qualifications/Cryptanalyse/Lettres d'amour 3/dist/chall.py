from Crypto.Util.number import bytes_to_long, getPrime, inverse, GCD
from flag import flag

e  = 3
pt = bytes_to_long(flag.encode())

while True:
    p = getPrime(256)
    q = getPrime(256)
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    if d != -1 and GCD(e, phi) == 1:
        break

n  = p * q
ct = pow(pt, e, n)

print(f"{n  = }")
print(f"{e  = }")
print(f"{ct = }")