#!/usr/bin/python3
import os
import uuid
import time
import random

perInstanceUUID = str(uuid.uuid4())
width = 100
height = 100
lose = False
print("Votre mission consiste à développer un algorithme pour acheminer des lettres de S (start) à E (end) à travers un réseau complexe de tranchées tout en utilisant un itinéraire efficace. Par exemple voici ce que vous devrez réaliser : ")


example = """
Plan du parcours :
  ##################################
  S       ##                      ##
  ######  ##  ##################  ##
  ##      ##  ##  ##          ##  ##
  ######  ##  ##  ##  ######  ##  ##
  ##      ##      ##  ##  ##  ##  ##
  ##  ##############  ##  ##  ##  ##
  ##      ##      ##      ##      ##
  ######  ##  ##  ##############  ##
  ##          ##  ##          ##  ##
  ##  ##############  ##  ##  ##  ##
  ##                  ##  ##       E
  ##################################
Votre plan :
  ##################################
  S:::::::##                      ##
  ######::##  ##################  ##
  ##    ::##  ##  ##          ##  ##
  ######::##  ##  ##  ######  ##  ##
  ##::::::##      ##  ##  ##  ##  ##
  ##::##############  ##  ##  ##  ##
  ##::::::##      ##      ##      ##
  ######::##  ##  ##############  ##
  ##::::::    ##  ##::::::::::##  ##
  ##::##############::##  ##::##  ##
  ##::::::::::::::::::##  ##:::::::E
  ##################################
"""


print(example,"\n","C'est à vous de jouer !\n")

for i in range(50):
    start_time = time.time()
    if i < 10:
        width = str(random.randrange(5, 10))
        height = str(random.randrange(5, 10))
    elif i < 20:
        width = str(random.randrange(10, 20))
        height = str(random.randrange(10, 20))     
    elif i < 30:
        width = str(random.randrange(20, 30))
        height = str(random.randrange(20, 30))
    elif i < 40:
        width = str(random.randrange(30, 40))
        height = str(random.randrange(30, 40))
    else:
        width = str(random.randrange(40, 50))
        height = str(random.randrange(40, 50))           

    cmd = '/maze/mazeGenerator --width '+width+' --height '+height+' --solution --output maze'+perInstanceUUID
    os.system(cmd)

    with open("maze"+perInstanceUUID) as iMaze:
        mazeSolved = iMaze.read().strip("\n").replace("G","E")
        mazeToSolve = mazeSolved.replace(":"," ")
        #print(mazeSolved)
        print("Plan du parcours :")
        print(mazeToSolve)
        l_mazeSolved = mazeSolved.split("\n")
        print("Votre plan :")
        for j in range(len(l_mazeSolved)):
            player_answer = input().strip("\n")
            if l_mazeSolved[j] != player_answer:
                lose=True
                break
                
    if time.time() - start_time > 5 or lose:
        print("C'est un échec ! Vous avez répondu trop lentement ou incorrectement !")
        os.remove("/maze/maze"+perInstanceUUID)
        exit()



with open("flag.txt") as flag:
    FLAG = flag.read()
    print("Félicitation, vous avez menez à bien votre mission ! En récompense : " + FLAG)