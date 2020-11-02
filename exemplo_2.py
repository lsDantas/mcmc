# Exemplo 2: Lei de Potência/Passeio Aleatório Simétrico
#
# Grupo: Atílio, Fredson, Giovani e Leonardo
# Descrição: Exemplo do algoritmo de
# Metropolis-Hastings sendo usado para
# aproximar um lei de potência. Neste
# exemplo, a distribuição de proposta foi
# um passeio aleatório simétrico.

import numpy as np
from passeio_aleatorio import PasseioAleatorio
from metropolis import metropolis

# Definir Parâmetros do Problema
problema_2 = PasseioAleatorio()

# Definir Parâmetros do Método
estado_inicial_2 = 2
num_iteracoes_2 = 1000000

# Executar Algoritmo de Metropolis-Hastings
cadeia_2 = metropolis(problema_2, estado_inicial_2, num_iteracoes_2)

# Calcular Frequências de Estados na Cadeia Resultante
estados, contagem = np.unique(cadeia_2, return_counts=True)
frequencia = contagem / len(cadeia_2)

# Somar incidência de estados acima de 9
soma_acima_9 = np.sum(frequencia[8:])
freq_finais = np.append(frequencia[:8], soma_acima_9)

# Exibir Resultados
print("\n----------------- Exemplo 2 -----------------\n")
print("Frequências da Cadeia Obtida:")

for i in range(0,8):
    print("{} : {}".format(i + 1, freq_finais[i]))
print(">=9 : {}".format(freq_finais[8]))