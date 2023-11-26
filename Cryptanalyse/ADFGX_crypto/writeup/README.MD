Le chiffre avec le cryptosystème ADFGX se fait en 2 étapes. 
Une étape de substitution et une étape de permutation.

L'étape de substitution se fait grâce à une table de correspondance.
L'étape de permutation se fait grâce à une clé définie.

Cependant, ici, nous connaissons la clé `nobracket`.

Il est donc possible de retrouver le chiffré intermédiaire en faisant l'inverse de l'étape 2.

```py
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
```

Il nous reste donc l'étape de substitution à résoudre. Ici, cela revient simplement à une substitution monoalphabétique.
Sachant que le texte est en français, on retrouve les fréquences de chaque lettre : https://fr.wikipedia.org/wiki/Fr%C3%A9quence_d%27apparition_des_lettres 

On peut alors établir les fréquences de chaque "double lettre" et les associer à la liste vue précédemment.
```py
occurrence = {}

for i in range(0, len(pre_ciphertext), 2):
    encode_letter = pre_ciphertext[i:i+2]
    if encode_letter in occurrence.keys():
        occurrence[encode_letter] += 1
    else:
        occurrence[encode_letter] = 1
```
Et on déchiffre avec cette correspondance : 

```py
order_encode = list(dict(sorted(occurrence.items(), key=lambda item: item[1])).keys())[::-1]

plaintext = [pre_ciphertext[i:i+2] for i in range(0,len(pre_ciphertext),2)]

for i in range(len(order_encode)):
    for j, c in enumerate(plaintext):
        if c == order_encode[i]:
            plaintext[j] = most_used_letters[i]
```

Le flag est donné à la fin du message : ATTENTIONALANALYSEFREQUENTIELLEPETITSOLDAT