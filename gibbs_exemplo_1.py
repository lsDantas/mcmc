# Gibbs Exemplo 1: amostrando de um distribuição 
# simples, uniforme no quadrado [0,1]x[0,1]
# 
# Grupo: Atílio, Fredson, Giovani e Leonardo

import matplotlib.pyplot as plt

from numpy.random import rand
from gibbs import gibbs_sampler

def run_example_1(N=1000):
    """
    Exemplo simples baseado no Amostrador de Gibbs
    em que amostramos de uma uniforme [0,1]x[0,1]

    Args: 
        N : número de dados a serem gerados
    """

    # a condicional fi(xi|...) é uma uniforme [0,1]
    sampler = lambda x: rand()
    sample = gibbs_sampler([0,0], N, [sampler, sampler], 100)

    # preparamos para plotar as amostras
    x, y = zip(*sample)

    _, ax = plt.subplots(figsize=(15,10))
    ax.scatter(x,y)
    ax.set_xlabel("variable X1", fontsize=15)
    ax.set_ylabel("variable X2", fontsize=15)
    ax.set_title("Results from Uniform using Gibbs Sampling", fontsize=25)

    plt.show()

run_example_1()