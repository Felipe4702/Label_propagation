import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#pega o arquivo que escrevemos no python main.py <nome do arquivo>
if len(sys.argv) > 1:
    caminho_arquivo = sys.argv[1] 
else:
    print("Por favor, forneça o caminho do arquivo como argumento.")
    sys.exit(1)

#lemos o arquivo e pegamos as arestas
arestas = np.loadtxt(caminho_arquivo, delimiter=',', dtype=int)
grafo = nx.Graph()
grafo.add_edges_from(arestas)

A = nx.to_numpy_array(grafo)

def calcularmodarotulos(rotulosvizinhos):
    rotulos, vezes = np.unique(rotulosvizinhos, return_counts = True)
    max = np.max(vezes)
    indices = np.where(vezes == max)[0]
    indice_escolhido = np.random.choice(indices)
    novo_rotulo = rotulos[indice_escolhido]
    return novo_rotulo


    


