import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

if len(sys.argv) > 1:
    caminho_arquivo = sys.argv[1] 
else:
    print("Por favor, forneça o caminho do arquivo como argumento.")
    sys.exit(1)

arestas = np.loadtxt(caminho_arquivo, delimiter=',', dtype=int)
grafo = nx.Graph()
grafo.add_edges_from(arestas)

A = nx.to_numpy_array(grafo)

print(A)


