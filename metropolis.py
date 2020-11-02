
# Algoritmo de Metropolis-Hastings
#
# Grupo: 
# Descrição: 
#

import numpy as np

# ------- Parâmetros Iniciais -------

# Definir Distribuição Estacionária Desejada
pi = np.array([0.1, 0.2, 0.7])

# Definir Cadeia de Transição Proposta
transicao_proposta = np.array( [ [0.1, 0.8, 0.1], [0.4, 0.3, 0.3], [0.9, 0.1, 0] ] )
n_estados = transicao_proposta.shape[0]

# ------ Método Computacional -------

# Escolher Estado Inicial
estado = 2
cadeia = []

# Definir Número de Iterações
num_iter = 10000

for i in range(0, num_iter):
    # Armazenar Estado
    cadeia.append(estado)

    # Escolher Candidato para Transição com base em Cadeia Proposta
    candidato = np.random.choice( n_estados, p=transicao_proposta[estado, :] )

    # Definir Alfa
    alfa = ( pi[candidato] * transicao_proposta[candidato, estado] ) / ( pi[estado] * transicao_proposta[estado, candidato] )

    # Decidir se Transição será aceita
    if alfa >= 1:
        # Aceitar Sempre
        estado = candidato 
    else:
        # Aceitar com Probabilidade Alfa
        if np.random.rand() < alfa:
            estado = candidato


_, contagem = np.unique(cadeia, return_counts=True)
frequencia = contagem / len(cadeia)
print(frequencia)