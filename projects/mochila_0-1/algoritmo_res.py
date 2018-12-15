import numpy as np

def maximoValorRec(capacidade, qntItens, vetor_pesos, vetor_valor):
    '''
    metodo recursivo de resolucao do problema.
    '''
    if capacidade <= 0 or qntItens == 0:
        return 0
    elif vetor_pesos[qntItens-1] > capacidade:
        return maximoValorRec(capacidade,qntItens-1,  vetor_pesos, vetor_valor)
    else:
        return max(
                maximoValorRec(capacidade-vetor_pesos[qntItens-1],qntItens-1, vetor_pesos, vetor_valor) + vetor_valor[qntItens-1] ,
                maximoValorRec(capacidade,qntItens-1,  vetor_pesos, vetor_valor)
                )

def resposta(capacidade, vetor_pesos, vetor_valor):
    '''
    Funcao responsavel por gerar a matriz de respostas, chamar a funcao de resolucao iteravel
    e o metodo que lista os itens contidos no vagao.
    '''
    itensMax = len(vetor_valor)
    tabelaResposta = np.empty((itensMax+1,capacidade+1))
    matrizResposta = maximoValorIter(tabelaResposta, capacidade, itensMax, vetor_pesos, vetor_valor)
    vagao = itensNoTrem(matrizResposta, capacidade, itensMax, vetor_pesos)
    print(matrizResposta [itensMax][capacidade])
    print(vagao)

def maximoValorIter(tabela, capacidade, itensMax, vetor_pesos, vetor_valor):
    '''
    metodo para resolver iterativamente o problema em questao.
    '''
    for j in range(itensMax+1):
        for w in range(capacidade+1):
            if w == 0 or j == 0:
                tabela[j][w] = 0
            elif vetor_pesos[j-1] > w:
                tabela[j][w] = tabela[j-1][w]
            else:
                tabela[j][w] = max(
                        tabela[j-1][w],
                        tabela[j-1][w - vetor_pesos[j-1]] + vetor_valor[j-1]
                        )
    return tabela

def itensNoTrem(matriz, capacidade,itensMax, vetor_pesos):
    '''
    metodo responsavel por listar todos os itens que foram adicionados na matriz.
    retorna uma lista enumerando os itens de 1 ate n
    '''
    itensVagao = []
    for j in range(itensMax, 0, -1):
        if matriz[j][capacidade] != matriz[j-1][capacidade]:
            itensVagao.append(j)
            capacidade -= vetor_pesos[j - 1]
    return itensVagao
