# Exemplo 1: Cadeia Finita com 4 Estados
#
# Grupo: 
# Descrição: Exemplo do algoritmo de
# Metropolis-Hastings usado para um cadeia
# de Markov finita com 4 estados.

import numpy as np
from cadeia_finita import CadeiaFinita
from metropolis import metropolis

# Definir Parâmetros do Problema
pi = [0.1, 0.2, 0.6, 0.1]
P = [ [0.7, 0.1, 0.1, 0.1], [0.2, 0.3, 0.3, 0.2], [0.1, 0.2, 0.3, 0.4], [ 0.0, 0.3, 0.7, 0.0] ]

problema = CadeiaFinita(pi, P)

# Definir Parâmetros do Método
estado_inicial = 2
num_iteracoes = 100000

# Executar Algoritmo de Metropolis-Hastings
cadeia = metropolis(problema, estado_inicial, num_iteracoes)

# Calcular Frequências de Estados na Cadeia Resultante
_, contagem = np.unique(cadeia, return_counts=True)
frequencia = contagem / len(cadeia)

# Exibir Resultados
print("\n----------------- Exemplo 1 -----------------\n")
print("Distribuição Estacionária Desejada:\n{}\n".format(pi))
print("Frequências da Cadeia Obtida:\n{}\n".format(frequencia))