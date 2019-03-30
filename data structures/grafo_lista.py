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

import numpy as np

class GrafoLista:
    '''
    Um grafo construido com lista de adjacencia tem sua grande vantagem no consumo de memoria adaptavel, sendo muito melhor
    para grafos com poucas arestas pois, ao contrario do grafo com matriz, ele não alocara um espaço de tamanho V² para trabalhar
    somente com algumas posições, porem quanto mais arestas o grafo com lista possuir mais lento suas buscas se tornam, sendo O(V+E)
    onde V é o numero de vertices e E o numero de arestas, pois no pior caso, sera um grafo completo, ele teria que fazer muitas verificações
    desnecessarias antes de encontrar o que se deseja.
    '''
    def __init__(self, numeroVertices, arestas, direcionado=False, pesos=False):
        '''
        constroi o grafo de listas a partir de dois parametros obrigatorios, numero de vertices e o iteravel contendo as arestas,
        é possivel definir se o grafo sera direcionado e possuira pesos.
        '''
        self.__numeroVertices = numeroVertices
        self.__numeroArestas = 0
        self.__direcionado = direcionado
        self.__pesos = pesos
        #cria as listas de adjacencia
        self.__listaAdjacencia = []
        for k in range(self.__numeroVertices):
            self.__listaAdjacencia.append([])
        GrafoLista.__preencher(self, arestas)
    
    def __getitem__(self, vertice):
        '''
        recebe um vertice e retorna todas as arestas que se ligam a ele, seja de entrada ou saida.
        '''
        aux = []
        arestas = GrafoLista.__gerarArestas(self)
        for aresta in arestas:
            if aresta[0] == vertice or aresta[1] == vertice:
                aux.append(aresta)
        return aux

    def __repr__(self):
        '''
        retorna uma representação valida de instanciação de um novo objeto identico ao atual.
        '''
        arestas = GrafoLista.__gerarArestas(self)
        return 'GrafoLista(numeroVertices={0}, {1}, direcionado={2}, pesos={3})'.format(
                                                       self.__numeroVertices,
                                                       arestas,
                                                       self.__direcionado,
                                                       self.__pesos
                                                    )
    
    def __str__(self):
        '''
        retorna a matriz de adjacencia, mostrando todos as arestas existentes.
        '''
        return str(GrafoLista.__gerarArestas(self))
    
    def __gerarArestas(self):
        '''
        metodo responsavel por retornar uma lista contendo todas as arestas do grafo.
        '''
        arestas = []
        for vertice1 in range(self.__numeroVertices):
            for vertice2 in self.__listaAdjacencia[vertice1]:
                if self.__pesos == True:
                    if self.__direcionado == True:
                        arestas.append((vertice1,vertice2[0],vertice2[1]))
                    else:
                        if (max(vertice1,vertice2[0]),min(vertice1,vertice2[0]),vertice2[1]) not in arestas:
                            arestas.append((max(vertice1,vertice2[0]),min(vertice1,vertice2[0]), vertice2[1]))
                else:
                    if self.__direcionado == True:
                        arestas.append((vertice1,vertice2))
                    else:
                        if (max(vertice1,vertice2),min(vertice1,vertice2)) not in arestas:
                            arestas.append((max(vertice1,vertice2),min(vertice1,vertice2)))
        return arestas
    
    def __preencher(self, arestas):
        '''
        funcao responsavel por povoar a lista de adjacencia a partir do iteravel recebido como parametro.
        '''
        if arestas is not None:
            for aresta in arestas:
                if len(aresta) == 2 and self.__pesos == False:
                    if self.__direcionado == False:
                        if aresta[1] not in self.__listaAdjacencia[aresta[0]]:
                            self.__listaAdjacencia[aresta[0]].append(aresta[1])
                        if aresta[0] not in self.__listaAdjacencia[aresta[1]]:
                            self.__listaAdjacencia[aresta[1]].append(aresta[0])
                    else:
                        if aresta[1] not in self.__listaAdjacencia[aresta[0]]:
                            self.__listaAdjacencia[aresta[0]].append(aresta[1])
                    self.__numeroArestas += 1
                elif len(aresta) == 3 and self.__pesos == True:
                    if self.__direcionado == False:
                        if aresta[1] not in self.__listaAdjacencia[aresta[0]]:
                            self.__listaAdjacencia[aresta[0]].append((aresta[1],aresta[2]))
                        if aresta[0] not in self.__listaAdjacencia[aresta[1]]:
                            self.__listaAdjacencia[aresta[1]].append((aresta[0],aresta[2]))
                    else:
                        if aresta[1] not in self.__listaAdjacencia[aresta[0]]:
                            self.__listaAdjacencia[aresta[0]].append((aresta[1],aresta[2]))
                    self.__numeroArestas += 1
                else:
                    raise IndexError('Existem arestas inválidas!')

    @property
    def tree(self):
        '''
        retorna True caso seja uma arvore e False caso nao, o codigo se baseia em checar as arestas existentes
        e monitorar a ocorrencia de eventuais loopings através de uma fila, um vertice e escolhido e todas as suas arestas sao pegas, uma a uma, sempre que uma aresta e escolhida, o outro terminal é adicionado na fila,
        caso haja o mesmo vertice esperando na fila o programa ja retorna False, caso não, ele prossegue, pegando o primeiro da fila e verificando novamente.
        '''
        if self.__numeroArestas > (self.__numeroVertices -1):
            return False
        aux = GrafoLista.__gerarArestas(self)
        lixo = []
        fila= []
        aux2 = aux[0][0] 
        cont = len(aux)
        while cont > 0:
            for aresta in aux:
                if aresta[0] == aux2 or aresta[1]:
                    if aresta[1] in fila:
                        return False
                    lixo.append(aresta[0])
                    fila.append(aresta[1])
                    cont -= 1
            if len(fila) == 0:
                for x in aux:
                    if x[0] not in lixo:
                        fila.append(x[0])
                        break
            aux2 = fila[0]
            del fila[0]
        return True
    
    @property
    def qntVertices(self):
        '''
        retorna a quantidade de vertices.
        '''
        return self.__numeroVertices
    
    @property
    def qntArestas(self):
        '''
        retorna a quantidade de arestas.
        '''
        return self.__numeroArestas
    
    @property
    def checkDirecionado(self):
        '''
        retorna se o grafo e direcionado ou nao.
        '''
        return self.__direcionado
    
    @property
    def checkPesos(self):
        '''
        retorna se o grafo possui pesos ou não
        '''
        return self.__pesos
    
    @property
    def gerarGrafoMatriz(self):
        '''
        retorna um objeto da classe GrafoMatriz identico ao self
        '''
        from grafo_matriz import GrafoMatriz
        arestas = GrafoLista.__gerarArestas(self)
        return GrafoMatriz(
            numeroVertices= self.__numeroVertices,
            arestas= arestas , 
            direcionado= self.__direcionado , 
            pesos= self.__pesos
        )
    
    def adj(self, vertice):
        '''
        metodo feito para utilizacao das buscas por largura e profundidade, retorna uma lista de tuplas de todas as arestas
        adjacentes a um determinado vertice.
        '''
        aux = []
        arestas = GrafoLista.__gerarArestas(self)
        for aresta in arestas:
            if self.__direcionado == True and aresta[0] == vertice:
                aux.append(aresta)
            elif self.__direcionado == False and (aresta[0] == vertice or aresta[1] == vertice):
                if aresta[1] == vertice:
                    aresta = list(aresta)
                    temp = aresta[1]
                    aresta[1] = aresta[0]
                    aresta[0] = temp
                    aresta = list(aresta)
                aux.append(aresta)
        return aux
    
    def adicionarAresta(self, aresta):
        '''
        recebe uma aresta contendo dois valores caso seja sem pesos ou tres valores caso haja pesos e realiza
        a adicao da aresta na lista de adjacencia.
        '''
        if self.__direcionado == True:
            if self.__pesos == True:
                self.__listaAdjacencia[aresta[0]].append((aresta[1],aresta[2]))
                self.__numeroArestas += 1
            else:
                self.__listaAdjacencia[aresta[0]].append(aresta[1])
                self.__numeroArestas += 1
        else:
            if self.__pesos == True:
                self.__listaAdjacencia[aresta[0]].append((aresta[1],aresta[2]))
                self.__listaAdjacencia[aresta[1]].append((aresta[0],aresta[2]))
                self.__numeroArestas += 1
            else:
                self.__listaAdjacencia[aresta[0]].append(aresta[1])
                self.__listaAdjacencia[aresta[1]].append(aresta[0])
                self.__numeroArestas += 1
    
    def removerAresta(self, aresta):
        '''
        recebe como parametro um iteravel contendo um par de vertices que representa os terminais da aresta e 
        realiza a remocao da lista de adjacencia.
        '''
        if self.__direcionado == True:
            if self.__pesos == True:
                for verticeAndPeso in self.__listaAdjacencia[aresta[0]]:
                    if verticeAndPeso[0] == aresta[1]:
                        self.__listaAdjacencia[aresta[0]].remove(verticeAndPeso)
                        self.__numeroArestas -= 1
            else:
                for terminal in self.__listaAdjacencia[aresta[0]]:
                    if terminal == aresta[1]:
                        self.__listaAdjacencia[aresta[0]].remove(terminal)
                        self.__numeroArestas -= 1
        else:
            if self.__pesos == True:
                for verticeAndPeso in self.__listaAdjacencia[aresta[0]]:
                    if verticeAndPeso[0] == aresta[1]:
                        self.__listaAdjacencia[aresta[0]].remove(verticeAndPeso)
                        self.__numeroArestas -= 1
                for verticeAndPeso2 in self.__listaAdjacencia[aresta[1]]:
                    if verticeAndPeso2[0] == aresta[0]:
                        self.__listaAdjacencia[aresta[1]].remove(verticeAndPeso2)
                        self.__numeroArestas -= 1
            else:
                for terminal in self.__listaAdjacencia[aresta[0]]:
                    if terminal == aresta[1]:
                        self.__listaAdjacencia[aresta[0]].remove(terminal)
                        self.__numeroArestas -= 1
                for terminal in self.__listaAdjacencia[aresta[1]]:
                    if terminal == aresta[0]:
                        self.__listaAdjacencia[aresta[1]].remove(terminal)
                        self.__numeroArestas -= 1
    
    def checaAresta(self, v1, v2):
        '''
        recebe dois vertices e retorna True caso haja uma aresta entre eles e False caso não.
        '''
        if self.__pesos == True:
            temp = self.__listaAdjacencia[v1]
            for dupla in temp:
                if v2 == dupla[0]:
                    return True
            temp = self.__listaAdjacencia[v2]
            for dupla in temp:
                if v1 == dupla[0]:
                    return True
            return False
        else:
            if v2 in self.__listaAdjacencia[v1]:
                    return True
            if v1 in self.__listaAdjacencia[v2]:
                    return True
            return False

    def grauEntrada(self, vertice):
        '''
        checa o grau de entrada de um determinado vertice, caso o grafo não seja direcionado o vertice ficara com graus
        de entrada e saida iguais.
        '''
        grau = 0
        if self.__direcionado == True:
            if self.__pesos == True:
                for aresta in self.__listaAdjacencia:
                    for dupla in aresta:
                        if vertice == dupla[0]:
                            grau += 1
            else:
                for aresta in self.__listaAdjacencia:
                    if vertice == dupla[0]:
                            grau += 1
        else:
            grau = len(self.__listaAdjacencia[vertice])
        return grau
    
    def grauSaida(self, vertice):
        '''
        checa o grau de saida de um determinado vertice, caso o grafo não seja direcionado o vertice ficara com graus
        de entrada e saida iguais.
        '''
        return len(self.__listaAdjacencia[vertice])


if __name__ == '__main__':
    a = GrafoLista(5,[(0,1,10),(1,2,11),(2,3,12),(3,1,13)], pesos=True, direcionado=True)
    print(a.checaAresta(4,1))
    print(a.grauSaida(4))
    print(a.tree)
    print(a.__repr__())
    print(type(a.gerarGrafoMatriz))
    print(a.adj(3))