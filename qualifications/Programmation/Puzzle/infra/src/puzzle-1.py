#! /bin/python3
import random
import string
from inputimeout import inputimeout

FLAG = "NBCTF{M4i1_B0X_D1SCoV3r3D_MUs7_CH4NG3}"
LEN = 24
TIMEOUT=3

def get_random_flag():
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(LEN))
    return result_str


def get_pieces(flag) :
	random_ids = [random.randint(0,5000) for _ in range(0,LEN)]
	random_ids.sort()

	pieces = [(random_ids[i],puzzle[i]) for i in range (0,LEN)]
	random.shuffle(pieces)

	return pieces



if __name__ == "__main__":
	puzzle = get_random_flag()
	pieces = get_pieces(puzzle)

	for p in pieces:
		print(f"{p[0]}:{p[1]}")


	try:
	    answer = inputimeout(prompt='Envoyez les pièces triées par ordre croissant : \n >>> ', timeout=TIMEOUT)
  
	except Exception :
	    print('Temps écoulé. Trop lent !')
	    exit()

	if answer==puzzle:
		print("Bravo ! Voici le flag : ", FLAG)
	else:
		print("Reponse incorrecte.")
