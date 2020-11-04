# Exemplo 1: Método de Monte Carlos
#
# Grupo: Atílio, Fredson, Giovani e Leonardo
# Descrição: Exemplo de utilização do método
# de Morte Carlos para computar o valor de PI

import numpy as np

def pi_mc(n):
    ''' 
    Esse função usa a fórmula da circunferência A = pi*r*r
    para calcular o valor de pi, usando a fórmula pi = A/(r*r).
    r = 1. O valor de A é computado utilizando amostragem. Geramos
    pontos no quadrado unitário e calculamos a fração que está dentro 
    da circunferência. A área do quadrado unitário é 4, a área do
    círculo é a fração de pontos dentro do círculo vezes 4.
    '''
    
    x = np.random.uniform(low = - 1,  high = 1, size = n)
    y = np.random.uniform(low = -1, high = 1, size = n)
    
    inside_frac = sum((x*x + y*y) < 1)/n
    A = inside_frac*4
    return A

print(pi_mc(100000))
    
    
    
