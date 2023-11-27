#! /bin/python3

import random
import sys


FLAG = "NBCTF{1N_7H3_8361NN1N6_7H3_UN1V3r53_W45_Cr3473D_TH1S_H45_M4D3_4_l07_0F_P30P13_V3rY_4N6rY_4ND_833N_W1D31Y_r364rD3D_45_4_84D_M0V3}"

DIMENSION_X = 8
DIMENSION_Y = 8
DIMENSION_Z = 3

SPACE_OTTER_COUNT = 1
CARGO_SHIP_COUNT = 1
ROCK_COUNT = 100


SPACE_OTTER_LETTER = "O"
CARGO_SHIP_LETTER = "C"
ROCK_LETTER = "R"
PURPLE_LETTER = "P"
YELLOW_LETTER = "Y"
NEUTRAL_LETTER = "N"

EMPTY_LETTER = "[]"

PURPLE_CARGO_SHIP_COOR = {"x":0, "y":0, "z":0}
YELLOW_SPACE_OTTER_COOR = {"x":0, "y":0, "z":0}

WELCOME="""
 _           _____     _           _ _                   
| |    ___  |__  /   _| |__   __ _| | |_ _ __ ___  _ __  
| |   / _ \   / / | | | '_ \ / _` | | __| '__/ _ \| '_ \ 
| |__|  __/  / /| |_| | |_) | (_| | | |_| | | (_) | | | |
|_____\___| /____\__,_|_.__/ \__,_|_|\__|_|  \___/|_| |_|
                                                         
  ____                    _                         _           _   
 / ___|___  ___ _ __ ___ (_) __ _ _   _  ___    ___( ) ___  ___| |_ 
| |   / _ \/ __| '_ ` _ \| |/ _` | | | |/ _ \  / __|/ / _ \/ __| __|
| |__| (_) \__ \ | | | | | | (_| | |_| |  __/ | (__  |  __/\__ \ |_ 
 \____\___/|___/_| |_| |_|_|\__, |\__,_|\___|  \___|  \___||___/\__|
                               |_|                                  
  __             _            _   _                  
 / _| __ _ _ __ | |_ __ _ ___| |_(_) __ _ _   _  ___ 
| |_ / _` | '_ \| __/ _` / __| __| |/ _` | | | |/ _ \\
|  _| (_| | | | | || (_| \__ \ |_| | (_| | |_| |  __/
|_|  \__,_|_| |_|\__\__,_|___/\__|_|\__, |\__,_|\___|
                                       |_|           
#####"""


class board():
    def __init__(self):
        self.board = [[[EMPTY_LETTER for z in range(DIMENSION_Z)] for y in range(DIMENSION_Y)] for x in range(DIMENSION_X)]

    def print_board(self):

        for z in range(DIMENSION_Z):
            for y in range(DIMENSION_Y):
                for x in range(DIMENSION_X):
                    print(self.board[x][y][z], end="")
                print()
            if(z != DIMENSION_Z-1):
                print("-")

    def make_move(self, old_x, old_y, old_z, new_x, new_y, new_z):
        if self.board[old_x][old_y][old_z] != "YO":
            print("You can only move the yellow otter !")
            print("You can only move the yellow otter !",file=sys.stderr)
            return
        elif self.board[new_x][new_y][new_z] == "NR":
            print("You can't move on a rock !")
            print("You can't move on a rock !",file=sys.stderr)
            return

        self.board[new_x][new_y][new_z] = self.board[old_x][old_y][old_z]
        self.board[old_x][old_y][old_z] = EMPTY_LETTER

        YELLOW_SPACE_OTTER_COOR["x"] = int(new_x)
        YELLOW_SPACE_OTTER_COOR["y"] = int(new_y)
        YELLOW_SPACE_OTTER_COOR["z"] = int(new_z)
        print("move made", file=sys.stderr)


def generate_random_board():
    b = board()
    
    for color_letter in [PURPLE_LETTER, YELLOW_LETTER]:
        for _ in range(SPACE_OTTER_COUNT):
            
            x = random.randint(0, DIMENSION_X-1)
            y = random.randint(0, DIMENSION_Y-1)
            z = random.randint(0, DIMENSION_Z-1)

            while(b.board[x][y][z] != EMPTY_LETTER):
                x = random.randint(0, DIMENSION_X-1)
                y = random.randint(0, DIMENSION_Y-1)
                z = random.randint(0, DIMENSION_Z-1)

            b.board[x][y][z] = color_letter+SPACE_OTTER_LETTER

            if(color_letter == YELLOW_LETTER):
                YELLOW_SPACE_OTTER_COOR["x"] = x
                YELLOW_SPACE_OTTER_COOR["y"] = y
                YELLOW_SPACE_OTTER_COOR["z"] = z
        
        for _ in range(CARGO_SHIP_COUNT):
                
            x = random.randint(0, DIMENSION_X-1)
            y = random.randint(0, DIMENSION_Y-1)
            z = random.randint(0, DIMENSION_Z-1)

        
            while(b.board[x][y][z] != EMPTY_LETTER):
                x = random.randint(0, DIMENSION_X-1)
                y = random.randint(0, DIMENSION_Y-1)
                z = random.randint(0, DIMENSION_Z-1)
            b.board[x][y][z] = color_letter+CARGO_SHIP_LETTER

            if(color_letter == PURPLE_LETTER):
                PURPLE_CARGO_SHIP_COOR["x"] = x
                PURPLE_CARGO_SHIP_COOR["y"] = y
                PURPLE_CARGO_SHIP_COOR["z"] = z

    for _ in range(ROCK_COUNT):
                    
        x = random.randint(0, DIMENSION_X-1)
        y = random.randint(0, DIMENSION_Y-1)
        z = random.randint(0, DIMENSION_Z-1)
            
        while(b.board[x][y][z] != EMPTY_LETTER):
            x = random.randint(0, DIMENSION_X-1)
            y = random.randint(0, DIMENSION_Y-1)
            z = random.randint(0, DIMENSION_Z-1)
        b.board[x][y][z] = NEUTRAL_LETTER+ROCK_LETTER

    return b


b = generate_random_board()

def checkWin():
    
    diff_x = abs(PURPLE_CARGO_SHIP_COOR["x"] - YELLOW_SPACE_OTTER_COOR["x"])
    diff_y = abs(PURPLE_CARGO_SHIP_COOR["y"] - YELLOW_SPACE_OTTER_COOR["y"])
    diff_z = abs(PURPLE_CARGO_SHIP_COOR["z"] - YELLOW_SPACE_OTTER_COOR["z"])
    diff = [diff_x, diff_y, diff_z]

    if diff.count(0) == 2 and diff.count(1) == 1:
        print("WIN !",file=sys.stderr)
        return True
    else:
        print("NOT WIN",file=sys.stderr)
        return False

win = False

print(WELCOME)
b.print_board()

print("YELLOW OTTER : ", YELLOW_SPACE_OTTER_COOR,file=sys.stderr)
print("PURPLE SHIP : ", PURPLE_CARGO_SHIP_COOR,file=sys.stderr)

while not win : 

    answer = input('Send a move in the format(old_x,old_y,old_z,new_x,new_y,new_z) : \n >>> ').split(',')
    b.make_move(int(answer[0]), int(answer[1]), int(answer[2]), int(answer[3]), int(answer[4]), int(answer[5]))

    win = checkWin()

    print("YELLOW OTTER : ", YELLOW_SPACE_OTTER_COOR,file=sys.stderr)
    print("PURPLE SHIP : ", PURPLE_CARGO_SHIP_COOR,file=sys.stderr)

    b.print_board()

if win:
    print("Your space otter defeated the purple cargo ship ! Here is your flag : ", FLAG)