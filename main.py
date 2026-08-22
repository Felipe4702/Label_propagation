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

