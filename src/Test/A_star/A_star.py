import networkx as nx
import matplotlib.pyplot as plt
from collections import deque 
import numpy as np
G = [[0, 1, 0, 1],
     [0, 0, 0, 1],
     [0, 1, 0, 1],
     [1, 1, 0, 0]]
#Funcionamiento con libreria networkx
def showG(G, directed = True):
    g = nx.DiGraph() if directed else nx.Graph()
    n = len(G)
    g.add_nodes_from([u for u in range(n)])
    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                g.add_edge(u, v)
    ##(objeto nx, del nodo llamado, a el nodo llamado, sin pesos)
    path = list(nx.astar_path(g, 2, 0, weight = None))
    print(path)
    nx.draw(g, with_labels = True)
    plt.show()
Muestra el camino mas corto con entrada de matriz
showG(G)





