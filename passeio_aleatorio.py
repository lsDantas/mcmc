# Código Auxiliar: PasseioAleatorio
#
# Grupo: Atílio, Fredson, Giovani e Leonardo
# Descrição: Encapsula distribuição de proposta 
# baseada em passeio aleatório.

import numpy as np

class PasseioAleatorio:
    # Selecionar Candidato segundo Regra Previamente Estabelecida
    def selecionar_candidato(self, estado_atual):
        if estado_atual == 1:
            return 2
        else:
            if np.random.rand() <= 0.5:
                return estado_atual + 1
            else:
                return estado_atual - 1

    # Recuperar Valor de pi_i
    def dist_estac(self, i):
        return np.power(i, -3/2)

    # Determinar Probabilidade de Transicao de i para j
    def transicao(self, i, j):
        if i == 1 and j == 2:
            return 1
        elif j == i + 1 or j == i - 1:
            return 0.5
        else:
            return 0
