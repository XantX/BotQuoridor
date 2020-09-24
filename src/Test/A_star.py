import networkx as nx
import matplotlib.pyplot as plt
G = [[0, 1, 0, 1],
     [0, 0, 0, 1],
     [0, 1, 0, 1],
     [1, 1, 0, 0]]
def showG(G, directed = True):
    g = nx.DiGraph() if directed else nx.Graph()
    n = len(G)
    g.add_nodes_from([u for u in range(n)])
    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                g.add_edge(u, v)
    print(list(nx.astar_path(g, 2, 0, weight = None)))
    nx.draw(g, with_labels = True)
    plt.show()

showG(G)
