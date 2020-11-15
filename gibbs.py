# Algoritmo Gibbs Sampling
#
# Grupo: Atílio, Fredson, Giovani e Leonardo
# Descrição: implementação de algoritmo para
# Amostrador de Gibbs, para várias variáveis

def gibbs_sampler(X, N, F, t):
    """
    Amostrador-exemplo para distribuições (possivelmente)
    de alta dimenção do tipo Amostrador de Gibbs.
    
    Args: 
        N : numero de amostras
        X : lista/vetor inicial
        F : lista de amostradores condicionais fi, dados
            x1,..,xi-1,xi+1,..,xn, demais variáveis
        t : iterações cortadas
    """

    out = [X]
    for i in range(t+N):
        # geramos uma nova amostra
        _X = _step(X.copy(), F)
        out.append(_X)

    # removemos iterações iniciais 
    return out[t:]

def _step(X, F):
    """
    Amostra um novo vetor dado o anterior e amostradores
    F condicionais às demais variáveis.

    Args:
        X : lista/vetor inicial
        F : lista de amostradores condicionais fi, dados
            x1,..,xi-1,xi+1,..,xn, demais variáveis
    """

    # iteramos sobre os índices de X
    for i in range(len(X)):
        X.pop(i)
        # amostramos dadas as demais
        sampler = F[i]
        X.insert(i, sampler(*X))

    return X