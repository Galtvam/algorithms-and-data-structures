#coding: utf-8

'''
Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
Centro de Informatica -- CIn (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF969 -- Algoritmos e Estruturas de Dados

Autor:    Marcos Antonio Tavares Galvão
Email:    matg@cin.ufpe.br

Licenca: The MIT License (MIT)
			Copyright(c) 2018 Marcos Antonio Tavares Galvão
'''

from grafo_matriz import GrafoMatriz
from grafo_lista import GrafoLista

'''
todas as funcoes foram baseadas nos codigos vistos em sala
'''

def buscaProfundidade(grafo):
    '''
    realiza a criacao das duas listas auxiliares, marcado e antecessor,
    varre os vertices e checando se eles ja foram verificados, caso nao, a funcao marcacao e chamada.
    retorna a lista de antecessores.
    '''
    marcado = [False] * grafo.qntVertices
    antecessor = [-1] * grafo.qntVertices
    for v in range(grafo.qntVertices):
        if marcado[v] == False: 
            marcacao(grafo,v,antecessor,marcado)
    return antecessor

def marcacao(grafo, vertice, antecessor, marcado):
    '''
    esta funcao e responsavel por marcar os vertices ja verificados e varrer seus terminais adjacentes marcando eles tambem,
    ao chegar no vertice final, que nao possui mais caminhos onde ir, a pilha e desfeita e se retorna pra funcao anterior.
    '''
    marcado[vertice] = True
    for u in grafo.adj(vertice):
        if marcado[u[1]] == False:
            antecessor[u[1]] = vertice
            marcacao(grafo,u[1],antecessor,marcado)


def buscaLargura(grafo):
    '''
    cria as tres listas de apoio, vertices, marcador e antecessor,
    varre os vertices e checa se ele já esta marcado, caso nao esteja ele e adicionado na fila e recebe a marcacao,
    faz todas as verificacoes com seus terminais adjacentes e contia o processo de marcacao e verificacao ate que todos os 
    vertices do grafo estejam devidamente marcados.
    retorna a lista de antecessores.
    '''
    vertices = []
    marcador = [False] * grafo.qntVertices
    antecessor = [-1] * grafo.qntVertices
    for i in range(grafo.qntVertices):
        if marcador[i] == False:
            vertices.append(i)
            marcador[i] = True
            while len(vertices) >0:
                v = vertices.pop(0)
                for u in grafo.adj(v):
                    if marcador[u[1]] == False:
                        marcador[u[1]] = True
                        antecessor[u[1]] = v
                        vertices.append(u[1])
    return antecessor


if __name__ == '__main__':
    a = GrafoLista(6,[(0,1),(1,4),(4,3),(3,1),(0,3),(2,4),(2,5),(5,5)], pesos=False, direcionado=True)
    b = GrafoMatriz(6,[(0,1),(1,4),(4,3),(3,1),(0,3),(2,4),(2,5),(5,5)], pesos=False, direcionado=True)
    
    print(buscaLargura(a))
    print(buscaLargura(b))
    print(buscaProfundidade(a))
    print(buscaProfundidade(b))