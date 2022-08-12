import math
import networkx as nx
import numpy as np
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Use networkx
# Create our dictionaries

node_dict = {1: {"pos": (82, 76), "demand": 0}, 2: {"pos": (96, 44), "demand": 19}, 3: {"pos": (50, 5), "demand": 21},
                 4: {"pos": (49, 8), "demand": 6}, 5: {"pos": (13, 7), "demand": 19}, 6: {"pos": (29, 89), "demand": 7},
                 7: {"pos": (58, 30), "demand": 12}, 8: {"pos": (84, 39), "demand": 16}, 9: {"pos": (14, 24), "demand": 6},
                 10: {"pos": (2, 39), "demand": 16}, 11: {"pos": (3, 82), "demand": 8}, 12: {"pos": (5, 10), "demand": 14},
                 13: {"pos": (98, 52), "demand": 21}, 14: {"pos": (84, 25), "demand": 16}, 15: {"pos": (61, 59), "demand": 3},
                 16: {"pos": (1, 65), "demand": 22}, 17: {"pos": (88, 51), "demand": 18}, 18: {"pos": (91, 2), "demand": 19},
                 19: {"pos": (19, 32), "demand": 1}, 20: {"pos": (93, 3), "demand": 24}, 21: {"pos": (50, 93), "demand": 8},
                 22: {"pos": (98, 14), "demand": 12}, 23: {"pos": (5, 42), "demand": 4}, 24: {"pos": (42, 9), "demand": 8},
                 25: {"pos": (61, 62), "demand": 24}, 26: {"pos": (9, 97), "demand": 24}, 27: {"pos": (80, 55), "demand": 2},
                 28: {"pos": (57, 69), "demand": 20}, 29: {"pos": (23, 15), "demand": 15}, 30: {"pos": (20, 70), "demand": 2},
                 31: {"pos": (85, 60), "demand": 14}, 32: {"pos": (98, 5), "demand": 9}}

node_pos_dict = {1: (82, 76), 2: (96, 44), 3: (50, 5), 4: (49, 8), 5: (13, 7), 6: (29, 89), 7: (58, 30), 8: (84, 39),
                 9: (14, 24), 10: (2, 39), 11: (3, 82), 12: (5, 10), 13: (98, 52), 14: (84, 25), 15: (61, 59), 16: (1, 65),
                 17: (88, 51), 18: (91, 2), 19: (19, 32), 20: (93, 3), 21: (50, 93), 22: (98, 14), 23: (5, 42), 24: (42, 9),
                 25: (61, 62), 26: (9, 97), 27: (80, 55), 28: (57, 69), 29: (23, 15), 30: (20, 70), 31: (85, 60), 32: (98, 5)}


node_demand_dict = {1: 0, 2: 19, 3: 21, 4: 6, 5: 19, 6: 7, 7: 12, 8: 16, 9: 6, 10: 16, 11: 8, 12: 14, 13: 21, 14: 16,
                    15: 3, 16: 22, 17: 18, 18: 19, 19: 1, 20: 24, 21: 8, 22: 12, 23: 4, 24: 8, 25: 24, 26: 24, 27: 2,
                    28: 20, 29: 15, 30: 2, 31: 14, 32: 9}

# Get the user to select nodes i and j
dictlen = len(node_dict)
print("Enter the node number for our starting node, i")
print("The number must be between 1 and " + str(dictlen))
i = int
i = input("Enter your choice and press ENTER " + '\n')
print("Enter the node number for our destination node, j")
print("The number must be between 1 and " + str(dictlen))
j = int
j = input("Enter your choice and press ENTER " + '\n')


# Create the graph
G = nx.Graph()
G.add_nodes_from(node_dict)
nx.set_node_attributes(G, node_dict)
nxnodespos = nx.get_node_attributes(G, "pos")
nxnodesdemand = nx.get_node_attributes(G, "demand")

def get_node_attr(i, j, nxnodespos, nxnodesdemand):
    global nxnodepos_i
    global nxnodepos_j
    global nxnodedemand_j

    for node, pos in nxnodespos.items():
        if str(node) == i:
            nxnodepos_i = pos

    for node, pos in nxnodespos.items():
        if str(node) == j:
            nxnodepos_j = pos

    for node, demand in nxnodesdemand.items():
        if str(node) == j:
            nxnodedemand_j = demand

get_node_attr(i, j, nxnodespos, nxnodesdemand)

print("Node i has a position of:", nxnodepos_i)
print("Node j has a position of: ", nxnodepos_j)
print("Node j has a demand of: ", nxnodedemand_j)

x1, y1 = nxnodepos_i
x2, y2 = nxnodepos_j
nxdist = np.sqrt((x1-x2)**2 + (y1-y2)**2)
print("Using Networkx, the distance is: ")
print(nxdist)

# Calculate edge length using math library
a = []
b = []
a.append(x1)
a.append(y1)
b.append(x2)
b.append(y2)
mathlibdist = math.dist(a, b)
print("Edge length according to Python Math Library..")
print(mathlibdist)
if nxdist == mathlibdist:
    print("They are the same!!")
else:
    print("They're different. Rats!")


"""
nx.draw_networkx(G, with_labels = True)
plt.show()
"""
