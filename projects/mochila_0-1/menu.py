import sys
from algoritmo_res import *

destino = sys.argv[-1:]

def gerarVetores(destino):
    '''
    recebe como parametro o local do arquivo e executa os procedimentos de:
        abertura do arquivo
        obtencao da capacidade
        criacao dos vetores de peso e valor
    O arquivo deve possuir um \n como ultima linha.
    '''
    arquivo = open(destino[0],'r',encoding='utf8')
    produtos = arquivo.readlines()
    
    listagemPesos = []
    listagemPrecos = []
    capacidade = int(produtos[0])
    
    for linha in produtos[1:]:
        temp = ''
        aux = 0
        for x in linha:
            if x != ',' and x != '\n':
                temp += x
            else:
                aux += 1
                if aux == 1:
                    listagemPesos.append(int(temp))
                    temp = ''
                else:
                    listagemPrecos.append(int(temp))
                    temp = ''
    return capacidade, listagemPesos, listagemPrecos

wMax, pesos, precos = gerarVetores(destino)
resposta(wMax, pesos, precos)
