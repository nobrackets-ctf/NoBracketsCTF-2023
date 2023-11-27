import numpy as np
import base64

SAMP_RATE = 2048000

TIMING_DOT = 1/1000
TIMING_DASH = 5/1000
TIMING_SEP_LETTER = 5/1000
TIMING_SPACE = 20/1000

alphabet = { 'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ', ':'--..--', '.':'.-.-.-',
            '?':'..--..', '/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-', '_': '..--.-'}

message = "WELCOME TO THIS AWESOME CHALLENGE   THE FLAG IS NBCTF(SDR_1S_S0000_C00L)   OVER"
bits = []

for letter in message:
    if letter == " ":
        bits += [0] * int((TIMING_SPACE-TIMING_SEP_LETTER)*SAMP_RATE)
        continue
    for i, c in enumerate(alphabet[letter]):
        if c == ".":
            bits += [1+1j] * int(TIMING_DOT*SAMP_RATE)
        else:
            bits += [1+1j] * int(TIMING_DASH*SAMP_RATE)
        if i < len(alphabet[letter])-1:
            bits += [0] * int(TIMING_DOT*SAMP_RATE)
    bits += [0] * int(TIMING_SEP_LETTER*SAMP_RATE)
    
print(len(bits))
# 1 bit -> 8 octets
# 2048000 bits par seconde -> 16384000 octets par seconde

signal = np.array(bits, dtype=np.complex64).tobytes()

with open("signal.iq", "wb") as f:
    f.write(signal)
