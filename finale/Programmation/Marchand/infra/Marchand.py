#!/usr/bin/python3

import networkx as nx
import random
import time

print("""Bienvenue jeune vagabond !

En tant que grand voyageur, vous avez pour but de parcourir les différentes îles de ce monde afin d'atteindre l'île d'arrivée. Cependant, vous ne pouvez vous permettre de dépenser toutes vos économies dans le vent. Chaque île vous permettra de réaliser des profits en vendant des ressources que vous possédez mais il faudra bien payer l'accès à ces îles. Votre objectif est donc d'effectuer votre traversée en étant le plus rentable. Votre proposition est attendu dans ce format-là :

Départ,The Treacherous Islands,The Cheering Peninsula,Portson Chain,Gibtague Key,Digboia Isles,Glasterre Chain,Arrivé""")

islandsName = []
flagged = True

def getIslandName():
    global islandsName
    index = random.randint(0,len(islandsName)-1)
    islandName = islandsName[index]
    islandsName.remove(islandName)
    return islandName

def regenerateIslandsName():
    global islandsName
    islandsName = [
    "The Tropectia",
    "The Cheering Peninsula",
    "The Yearning Haven",
    "The Terraced Archipelago",
    "The Torpedo Skerry",
    "The Octopus Cay",
    "The Adamantine Holm",
    "The Treacherous Islands",
    "The Silver Isle",
    "The Sparkling Reef",
    "Glasterre Chain",
    "Chesway Peninsula",
    "Digboia Isles",
    "Corlisle Cay",
    "Barringnear Islet",
    "Barrath Ait",
    "Arnmer Reef",
    "Lunentrie Ait",
    "Birside Ait",
    "Sufpond Isles",
    "Berboia Holm",
    "Trodwell Enclave",
    "Lammis Chain",
    "Portson Chain",
    "Gibtague Key"
    ]


for step in range(5):
    regenerateIslandsName()
    dictIslandInfos = {"Arrivé": (0,0),}
    listIslandsRoutedTogether = set()
    prevIslands=["Départ",]

    # On laisse les random à 6 et 4 pour l'instant sinon ça pompe trop de ressource

    for numberOfColumn in range(random.randint(6,6)):
        curIslands= []
        for numberOfIsland in range(random.randint(4,4)):
            curIslandName = getIslandName() #str(uuid.uuid4())
            costPort,profitIsland = random.randint(0,500), random.randint(300,1000)
            dictIslandInfos[curIslandName] = (costPort,profitIsland)
            curIslands.append(curIslandName)

        for prevIsland in prevIslands:
            notAssigned=True
            while notAssigned: 
                for curIsland in curIslands:
                    if numberOfColumn==0 or random.randint(0,100) < (100//5):
                        notAssigned = False
                        listIslandsRoutedTogether.add((prevIsland,curIsland))
        for curIsland in curIslands:
            notAssigned=True
            while notAssigned: 
                for prevIsland in prevIslands:
                    if numberOfColumn==0 or random.randint(0,100) < (100//5):
                        notAssigned = False
                        listIslandsRoutedTogether.add((prevIsland,curIsland))
        prevIslands = curIslands

    for prevIsland in prevIslands:
        listIslandsRoutedTogether.add((prevIsland,"Arrivé"))

    print("\n↓↓↓ îles reliées ↓↓↓\n")
    edges=[]
    for source,destination in listIslandsRoutedTogether:
        print(source,"->",destination)
        costPort, profitIsland = dictIslandInfos[destination]
        edges.append((source,destination,{'cost':profitIsland-costPort}))
    maxi=0
    G = nx.DiGraph(edges)
    #nx.drawing.nx_pydot.write_dot(G,"a.dot")
    soluce = nx.dag_longest_path(G,weight="cost")



    #print("PREDICTED=>",",".join(soluce)+",Arrivé")

    dictIslandInfos.pop('Arrivé')


    print("\n↓↓↓ Informations îles ↓↓↓\n")

    for k,v in dictIslandInfos.items():
        print(k,"| Profit prévu : ",v[1],", Prix pour amarrer : ",v[0])
    
    start_time = time.time()
    userSoluce = input("\nVotre proposition : ")

    try:
        listUserIsland = userSoluce.split(",")
        #print(soluce+["Arrivé",] ,listUserIsland)
        if soluce+["Arrivé",] != listUserIsland or time.time() - start_time > 20:
            print("Mauvaise réponse ou trop lent !")
            flagged=False
            break
    except:
        print("Entrée utilisateur problématique")
        exit()

if flagged:
    with open("flag.txt") as flag:
        FLAG = flag.read()
        print(FLAG)