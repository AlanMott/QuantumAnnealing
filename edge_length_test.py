import math
import networkx as nx

# Create a dictionary of nodes
node_dict = {1: (82, 76), 2: (96, 44), 3: (50, 5), 4: (49, 8), 5: (13, 7), 6: (29, 89), 7: (58, 30), 8: (84, 39),
            9: (14, 24), 10: (2, 39), 11: (3, 82), 12: (5, 10), 13: (98, 52), 14: (84, 25), 15: (61, 59), 16: (1, 65),
            17: (88, 51), 18: (91, 2), 19: (19, 32), 20: (93, 3), 21: (50, 93), 22: (98, 14), 23: (5, 42), 24: (42, 9),
            25: (61, 62), 26: (9, 97), 27: (80, 55), 28: (57, 69), 29: (23, 15), 30: (20, 70), 31: (85, 60), 32: (98, 5)}

# Create a list of nodes
node_list = [(82, 76), (96, 44), (50, 5), (49, 8), (13, 7), (29, 89), (58, 30), (84, 39),
            (14, 24), (2, 39), (3, 82), (5, 10), (98, 52), (84, 25), (61, 59), (1, 65),
            (88, 51), (91, 2), (19, 32), (93, 3), (50, 93), (98, 14), (5, 42), (42, 9),
            (61, 62), (9, 97), (80, 55), (57, 69), (23, 15), (20, 70), (85, 60), (98, 5)]


# Calculate edge length using math library
i = [8, 76]
j = [96, 44]
print("Edge length according to Python Math Library..")
print (math.dist(i, j))

# Calculate edge length using networkx
G = nx.Graph()
G.add_nodes_from(node_list)
print(G)