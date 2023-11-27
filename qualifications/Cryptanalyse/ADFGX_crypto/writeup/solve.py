### ADFGX cryptosystem SOLVE

key = "nobracket"

ciphertext = open("output.txt").read()

def reverse_permutation(text, key):
    # Create a sorted key to determine the order of columns
    sorted_key = sorted(key)
    print(sorted_key)
    # Calculate the number of rows and columns based on the text length
    rows = len(text) // len(key)
    cols = len(key)
    
    # Create an empty grid to store the ciphertext
    grid = [['' for _ in range(cols)] for _ in range(rows)]
    
    # Fill the grid with the ciphertext
    index = 0
    for col in sorted_key:
        col_index = key.index(col)
        for row in range(rows):
            grid[row][col_index] = text[index]
            index += 1
    
    # Read the grid row by row to obtain the plaintext
    plaintext = ''
    for row in grid:
        plaintext += ''.join(row)

    return plaintext

pre_ciphertext = reverse_permutation(ciphertext,key)
print("\n\n")
print(pre_ciphertext)
occurrence = {}

for i in range(0, len(pre_ciphertext), 2):
    encode_letter = pre_ciphertext[i:i+2]
    if encode_letter in occurrence.keys():
        occurrence[encode_letter] += 1
    else:
        occurrence[encode_letter] = 1

most_used_letters = [
    'e', 'a', 'i', 's', 'n', 'r', 't', 'o', 
    'l', 'u', 'd', 'c', 'm', 'p', 'g', 'b', 
    'v', 'h', 'f', 'q', 'y', 'x', 'j', 'k', 
    'w', 'z']

print(occurrence)
order_encode = list(dict(sorted(occurrence.items(), key=lambda item: item[1])).keys())[::-1]
print(order_encode)

plaintext = [pre_ciphertext[i:i+2] for i in range(0,len(pre_ciphertext),2)]

for i in range(len(order_encode)):
    for j, c in enumerate(plaintext):
        if c == order_encode[i]:
            plaintext[j] = most_used_letters[i]

print("".join(plaintext))