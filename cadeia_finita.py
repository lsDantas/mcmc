# Código Auxiliar: CadeiaFinita
#
# Grupo: Atílio, Fredson, Giovani e Leonardo
# Descrição: Encapsula distribuição de proposta 
# baseada em cadeia de Markov finita.

import numpy as np

class CadeiaFinita:
    def __init__(self, pi, matriz):
        self.pi = np.array(pi)
        self.matriz = np.array(matriz)
        self.num_estados = self.matriz.shape[0]

    # Selecionar Candidato segundo Regra Previamente Estabelecida
    def selecionar_candidato(self, estado_atual):
        candidato = np.random.choice( self.num_estados, p=self.matriz[estado_atual, :] )
        return candidato
    
    # Recuperar Valor de pi_i
    def dist_estac(self, i):
        return self.pi[i]

    # Determinar Probabilidade de Transicao de i para j
    def transicao(self, i, j):
        return self.matriz[i, j]