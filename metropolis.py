# Algoritmo de Metropolis-Hastings
#
# Grupo: Atílio, Fredson, Giovani e Leonardo
# Descrição: Implementação do algoritmo
# Metropolis-Hastings.

import numpy as np
from cadeia_finita import CadeiaFinita
from passeio_aleatorio import PasseioAleatorio

def metropolis(problema, estado_inicial, num_iter):
    # Inicializar Cadeia
    estado_atual = estado_inicial
    cadeia = [estado_atual]

    # Método Computacional
    for _ in range(0, num_iter):
        # Escolher Candidato para Transição
        candidato = problema.selecionar_candidato(estado_atual)

        # Computar Alfa a partir de Função de Aceitação
        alfa = ( problema.dist_estac(candidato) * problema.transicao(candidato, estado_atual) ) / ( problema.dist_estac(estado_atual) * problema.transicao(estado_atual, candidato) )

        # Decidir se Transição será aceita
        if alfa >= 1:
            # Aceitar Sempre
            estado_atual = candidato 
        else:
            # Aceitar com Probabilidade Alfa
            if np.random.rand() < alfa:
                estado_atual = candidato
        
        # Armazenar Estado
        cadeia.append(estado_atual)
    
    return cadeia