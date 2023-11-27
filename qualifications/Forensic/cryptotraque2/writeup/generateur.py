import csv
import random

"""
Script de génération du challenge.

Fichier CSV en sorie de la forme suivante :

wallet_source,wallet_destination,montant
"""

def generer_adresse(longueur=32):
	caracteres_hexadecimaux = '0123456789abcdef'
	chaine_hexadecimale = ''

	for _ in range(longueur):
		caractere = random.choice(caracteres_hexadecimaux)
		chaine_hexadecimale += caractere

	return chaine_hexadecimale

# adresse du wallet de départ
premier_wallet = '9e7e75841c73a0b391a1a0485948c30a'
# adresse du wallet d'arrivé == flag
dernier_wallet = '0d26d74d0daad532ac50852fd5742099'
# wallets intermédiaires / non impliqués dans le mixage
wallets_intermediaires = []
for _ in range(100): wallets_intermediaires.append(generer_adresse())


"""
Retourne l'ensemble des transactions entre premier_wallet et dernier_wallet en suivant les intermédiaires.
"""
def mixer(premier_wallet, dernier_wallet, wallets_intermediaires, montant='10'):
	# on créé des transactions entre les wallets intermédiaires
	data = ''
	#print('wallets intermédiaires', wallets_intermediaires)
	for i in range(len(wallets_intermediaires)):
		if i+1 <= len(wallets_intermediaires):
			if i == 0:
				data += premier_wallet+','+wallets_intermediaires[i]+','+montant+'\n'
			else:
				data += wallets_intermediaires[i-1]+','+wallets_intermediaires[i]+','+montant+'\n'
			if i == len(wallets_intermediaires)-1:
				data += wallets_intermediaires[i]+','+dernier_wallet+','+montant
	return data
	

def ajouter_bruit(signal, nb_transac):
	d = '\n'
	dataset = ''
	dataset = [e+d for e in signal.split(d) if e]

	# on génère la transaction
	for i in range(nb_transac):
		bruit = ''
		w1 = generer_adresse()
		w2 = generer_adresse()
		
		ws = []
		
		nb_inter = random.randint(1, 40)
		for j in range(nb_inter): ws.append(generer_adresse())
		bruit += mixer(w1, w2, ws, montant=str(random.randint(1, 11)))
		#print('bruit')
		#print(bruit)
		
		# on ajoute la transaction au dataset
		# pour chaque sous-transaction de ma transaction
		index = 0
		for transaction in bruit.split('\n'):
			transaction += '\n'
			if index != 0: index = random.randint(index+1, len(dataset))
			else: index=1
			dataset.insert(index, transaction)
			#print('index',index)
	return dataset
		

signal = mixer(premier_wallet, dernier_wallet, wallets_intermediaires)
#print(signal)


dataset = ajouter_bruit(signal, 1000)
f = open('transactions.csv', 'w')
data = ''
for ligne in dataset: data+=ligne
f.write(data)

f.close()
#print('premier wallet', premier_wallet, '\ndernier_wallet', dernier_wallet, '\nautres wallets', wallets_intermediaires)

