"""
IMPORTS
"""

from pwn import *
import networkx as nx
import matplotlib.pyplot as plt


"""
GLOBALS
"""

HOST="127.0.0.1"
PORT=1337
r=remote(HOST,PORT)
G = nx.Graph()

DIMENSION_X = 8
DIMENSION_Y = 8
DIMENSION_Z = 3

PURPLE_CARGO_SHIP_COOR = ""
YELLOW_SPACE_OTTER_COOR = ""


"""
RECEPTION
"""

print(r.recvuntil("#####").decode("utf-8"))
boards = r.recvuntil("Send").decode("utf-8").strip("Send")
print(boards)
boards = boards.split("-")

# final board :
final_board = [[[ line.strip("\n")[i:i+2] for i in range(0, len(line), 2) ] for line in board.split("\n")] for board in boards]



labels={}

# Labels provisioning and spotting of the yellow otter and the purple ship
for z, board in enumerate(boards):
    #final_board.append([])
    #print(board)
    #print("z: ",z)
    for y, line in enumerate(board.strip("\n").split("\n"),0):
        #final_board[-1].append([])
        x=0
        for square in [ line[i:i+2] for i in range(0, len(line), 2) ]:
            coor=str(x)+str(y)+str(z)
            labels[coor] = square
            if square=="PC":
                PURPLE_CARGO_SHIP_COOR = coor
            if square=="YO":
                YELLOW_SPACE_OTTER_COOR = coor

            #final_board[-1][-1].append(square)

            x+=1

nodes=labels.keys()

# Graph provisioning
for z in range(DIMENSION_Z):
    for y in range(DIMENSION_Y):
        for x in range(DIMENSION_X):
            try:
                if(x+1 < DIMENSION_X):
                    G.add_edge(str(x)+str(y)+str(z),str(x+1)+str(y)+str(z))
                if(x-1 >= 0):
                    G.add_edge(str(x)+str(y)+str(z),str(x-1)+str(y)+str(z))
                if(y+1 < DIMENSION_Y):
                    G.add_edge(str(x)+str(y)+str(z),str(x)+str(y+1)+str(z))
                if(y-1 >= 0):
                    G.add_edge(str(x)+str(y)+str(z),str(x)+str(y-1)+str(z))
                if(z+1 < DIMENSION_Z):
                    G.add_edge(str(x)+str(y)+str(z),str(x)+str(y)+str(z+1))
                if(z-1 >= 0):
                    G.add_edge(str(x)+str(y)+str(z),str(x)+str(y)+str(z-1))
                
            except:
                pass # one of the two nodes does not exist



"""
DRAWING
"""

# Remove rocks
for node in list(G.nodes):
    if labels[node] in ["NR","YC","PO"]:
        G.remove_node(node)

# Dessin du chemin
#pos = nx.spring_layout(G,seed=6) #6
#nx.draw(G,pos,node_color='k', with_labels=True)
# draw path in red
#path_edges = list(zip(path,path[1:]))
#nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')
#nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=10)
#plt.axis('equal')
#plt.draw()


"""
SOLVE
"""
# Find shortest path
path = nx.shortest_path(G,source=YELLOW_SPACE_OTTER_COOR,target=PURPLE_CARGO_SHIP_COOR)
print("SHORTEST PATH : ", path)


for next_square in path[1:-1]:
    # old_x,old_y,old_z,new_x,new_y,new_z
    print(r.recvuntil(">>>").decode("utf-8"))
    print(f'Otter position : {YELLOW_SPACE_OTTER_COOR}')
    print(f'next move: {next_square}')

    old_pos = f'{YELLOW_SPACE_OTTER_COOR[0]},{YELLOW_SPACE_OTTER_COOR[1]},{YELLOW_SPACE_OTTER_COOR[2]}'
    YELLOW_SPACE_OTTER_COOR=next_square

    new_pos = f'{next_square[0]},{next_square[1]},{next_square[2]}'
    move =f'{old_pos},{new_pos}'

    print(f"[+] Sending move {move}")
    r.sendline(move.encode("utf-8"))

r.interactive()
