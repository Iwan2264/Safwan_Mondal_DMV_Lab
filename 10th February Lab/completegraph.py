import networkx as nx
import matplotlib.pyplot as plt

n = int(input("Enter vertices (>3): "))

if n > 3:
    G = nx.complete_graph(n)
    nx.draw(G, with_labels=True)
    plt.show()
else:
    print("Vertices must be greater than 3")
