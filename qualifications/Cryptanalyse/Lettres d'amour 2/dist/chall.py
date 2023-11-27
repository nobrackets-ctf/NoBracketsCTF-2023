from flag import flag, key1, key2, key3

assert len(flag) == 32
assert len(key1) == 32
assert len(key2) == 32
assert len(key3) == 32

encrypted = bytearray(b"????????????????????????????????")

for i in range(32):
    encrypted[i] = (flag[i] ^ key1[i]) ^ (key2[i] ^ key3[i])

print(f"{encrypted = }") # encrypted = bytearray(b'\x16|&Q^F6Ka\x19|\x12\x1f\nwM-i.`\x19\t)|x\x197h:nN\x0f')
print(f"{key1      = }") # key1      = bytearray(b'EJ3H7g9ppuvnG4VwtjBY3KE56gKp3825')
print(f"{key2      = }") # key2      = bytearray(b'LAn8U2yewMweL94888a5YCwsH88q2PXu')
print(f"{key3      = }") # key3      = bytearray(b'Q58uzhAn3kMLf2JRPn8S72Dy7uq6c6V2')