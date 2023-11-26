def suivre(adresse_source, fichier):
	# si pas modifiée, c'est qu'il y a un problème
	flag = 'ERROR'
	f = open(fichier,'r')
	data = f.read()
	data=data.split('\n')
	for ligne in data:
		l = ligne.split(',')
		if l[0] == adresse_source:
			adresse_source = l[1]
	print(adresse_source)

suivre('9e7e75841c73a0b391a1a0485948c30a', 'transactions.csv')
