import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def calcularmodarotulos(rotulosvizinhos):
    #colocamos em rotulos os rotulos unicos e em vezes a quantidade que cada rotulo apareceu
    rotulos, vezes = np.unique(rotulosvizinhos, return_counts = True)
    #descobrimos qual foi o valor do/s rotulo/s que apareceu mais
    max = np.max(vezes)
    #pegamos o incide de todos o rotulos que apareceram max vezes
    indices = np.where(vezes == max)[0]
    #se empartar escolhemos um alatoriamente
    indice_escolhido = np.random.choice(indices)
    novo_rotulo = rotulos[indice_escolhido]
    return novo_rotulo


def label_propagation(A, max_iter):
    N = A.shape[0]
    Rotulos = np.arange(0,N)

    iter = 0
    mudou = True

    while (iter < max_iter and mudou):
        mudou = False
        #criamos a ordem aleatoria de vizitar cada no
        OrdemVertice = np.random.permutation(N)

        for i in OrdemVertice:

            #salvamos os vizinhos de i
            vizinhos = np.where(A[i] == 1)[0]

            if len(vizinhos) > 0:
                RotuloVizinho = Rotulos[vizinhos]
                NovoRotulo = calcularmodarotulos(RotuloVizinho)

                if NovoRotulo != Rotulos[i]:
                    Rotulos[i] = NovoRotulo
                    mudou = True

        iter = iter + 1

    return Rotulos

if __name__ == "__main__":

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

    print(f"Matrix da rede {caminho_arquivo}")
    print(A)

    #label_propagation(matriz, iteracoes maximas)
    rotulos_finais = label_propagation(A, 100)

    print("Comunidades encontradas:")
    print(rotulos_finais)


    #visualizando o grafo pintado referente aos rotulos
    print("\nGerando gráfico das comunidades...")
    nx.draw(
        grafo, 
        with_labels=True, 
        node_color=rotulos_finais, #rotulos iguais recebem a mesma cor
        cmap=plt.cm.Set3, 
        node_size=700, 
    )
    plt.show() 