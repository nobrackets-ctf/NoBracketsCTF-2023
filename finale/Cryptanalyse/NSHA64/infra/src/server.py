#!/usr/bin/env python3
from Crypto.Util.number import getPrime

class long_to_single():
	def __init__(self):
		self.o = 0
		self.r1 = 0 # haut
		self.r2 = 0 # premier bas
		self.r3 = 0 # deuxieme bas
	def next(self, i):
		self.r3 = self.r2
		self.r2 = i
		self.r1 = i
		self.o = (1-self.r3)&self.r1

class SecureHash():
	def __init__(self):
		self.result = 0
		self.lts = long_to_single()
		self.is_done = 0

	def next(self, input_bit):
		
		shift = 0x0f | (self.result >> 6 & (2**6-1))
		inter = (self.result << shift) & (2**64-1)
		
		a = 1-input_bit
		
		b = (self.result - a) & (2**64-1)
		
		c = inter ^ b
		
		self.lts.next((self.result >> 3 & 1) & input_bit)
		self.result = (c + input_bit) & (2**64-1)

		self.is_done = self.lts.o & input_bit
		#print(hex(self.result))




def menu():
	print("===NSHA64 Oracle===\n")
	print("1- Hasher un message")
	print("2- Recuperer le flag")
	print("3- Exit\n")

secret_key = getPrime(64)
for _ in range(256):
	menu()
	
	try:
		choice = int(input())
	except:
		print("Erreur de format. Entrez 1,2 ou 3")
		exit()
		
	if choice == 1 :
		try:
			message = int(input("Entrez votre message à hasher : "))
		except:
			print("Erreur de format. Envoyez votre message en decimal")
			exit()

		nsha = SecureHash()

		count_cycle = 0
		i = 0
		while i != 63:
			input_bit = (secret_key & (message % 2**64) ) >> i & 1
			inc = int(1-input_bit) | int(nsha.is_done)
			#print(inc)
			nsha.next(input_bit)
			count_cycle+=1
			i+=inc



		print(f"NSHA64 : {hex(nsha.result)}")
		print(f"Nombre de cycles pour calculer le hash : {count_cycle}\n")
	
	elif choice == 2:
		try:
			guess_key = int(input("Entrez la cle secrete pour recuperer le flag : "))
		except:
			print("Erreur de format. Envoyez la cle en decimal")
			exit()
		if guess_key == secret_key:
			print("NBCTF{Leaky_Leaky_Chip_L3aks_4ll_its_S3cr3ts}")
		else:
			print("Nop, retente ta chance !!\n")
	
	else :
		print("A bientot")
		break
