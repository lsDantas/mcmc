# Exemplo 1: Método de Monte Carlos
#
# Grupo: Atílio, Fredson, Giovani e Leonardo
# Descrição: Exemplo de utilização do método
# de Morte Carlos para computar a integral de 
# x^2 no intervalo de 0 a 1.
#

import numpy as np

def integrate_mc(f, a, b, n):
    ''' 
    Esse função computa a integral da função f  no
    intervalo de a a b através de um método de Monte Carlos.
    Para isso, ela seleciona valores aleatórios no intervalo [a, b]
    e computa o valor da integral como: (b-a)/n * sum(f(x_i))
    Sendo x_i as amostras aleatórias.    
    '''
    x = np.random.uniform(low = a,  high = b, size = n)
    f_x = f(x)
    integ = (b - a) * sum(f_x)/n
    return integ

def f1(x):
    return x*x

def f2(x):
    return np.tan(x + 2)

print(integrate_mc(f1, 0, 1, 100000))
print(integrate_mc(f2, 0, 1, 100000))
    
    
    
