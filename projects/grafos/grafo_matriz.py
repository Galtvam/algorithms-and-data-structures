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

class GrafoMatriz:
    '''
    Um grafo implementado com matriz de adjacencia toma vantagem da rapidez de acessar a matriz, O(1) para buscas e inserções,
    portanto quando se tratam de grandes volumes de vertices com muitas arestas, similar a um grafo completo, o GrafoMatriz se torna muito mais rapido
    em relação a lista, entretanto peca no consumo de espaço, sendo O(V²), uma matriz com mais de 10^6 vertices ja fica imensamente custosa
    requerindo memoria acima de 8gb.
    '''
    def __init__(self, numeroVertices, arestas, direcionado=False, pesos=False):
        '''
        constroi o grafo de matriz a partir de dois parametros obrigatorios, numero de vertices e o iteravel contendo as arestas,
        é possivel definir se o grafo sera direcionado e possuira pesos.
        '''
        self.__numeroVertices = numeroVertices
        self.__numeroArestas = 0
        self.__direcionado = direcionado
        self.__pesos = pesos
        #cria uma matriz de zeros com v² elementos
        self.__matrizAdjacencia = np.zeros(shape=(self.__numeroVertices,self.__numeroVertices))
        GrafoMatriz.__preencher(self, arestas)
    
    def __repr__(self):
        '''
        retorna uma representação valida de instanciação de um novo objeto identico ao atual.
        '''
        arestas = GrafoMatriz.__gerarArestas(self,True)
        return 'GrafoMatriz(numeroVertices={0}, {1}, direcionado={2}, pesos={3})'.format(
                                                       self.__numeroVertices,
                                                       arestas,
                                                       self.__direcionado,
                                                       self.__pesos
                                                    )
    def __str__(self):
        '''
        retorna a matriz de adjacencia, mostrando todos as arestas existentes.
        '''
        return str(self.__matrizAdjacencia)
    
    def __getitem__(self, vertice):
        '''
        recebe um vertice e retorna todas as arestas que se ligam a ele, seja de entrada ou saida.
        '''
        arestas = GrafoMatriz.__gerarArestas(self,False, vertice)
        return arestas
    
    def __gerarArestas(self, chave, vertice=None):
        '''
        metodo extremamente util, retorna a lista de arestas que compoem o grafo, possui duas configurações restritas
        sendo elas, chave e vertice, a primeira pode ser True ou False e serve pra funçao saber o que deve retornar,
        se a chave for True ela retorna todas as arestas, se for False retorna somente as que possuem um vertice especifico nela,
        vertice este que corresponde ao outro parametro.
        '''
        arestas = []
        for vertice1 in range(self.__numeroVertices):
            for vertice2 in range(self.__numeroVertices):
                temp = self.__matrizAdjacencia[vertice1][vertice2]
                if chave == True and self.__pesos == False:
                    #secao utilizada pelo __repr__
                    if temp != 0:
                        arestas.append((vertice1,vertice2))
                elif chave == False and self.__pesos == False:
                    #secao utilizada pelo get_item
                    if (
                        temp != 0 and (vertice1 == vertice or vertice2 == vertice)
                    ):
                        arestas.append((vertice1,vertice2))
                elif chave == True and self.__pesos == True:
                    #secao utilizada pelo __repr__
                    if temp != 0:
                        arestas.append((vertice1,vertice2,temp))
                elif chave == False and self.__pesos == True:
                    #secao utilizada pelo get_item
                    if (
                        temp != 0 and (vertice1 == vertice or vertice2 == vertice)
                    ):
                        arestas.append((vertice1,vertice2, temp))
        return arestas

    def __preencher(self, arestas):
        '''
        funcao responsavel por povoar a matriz a partir do iteravel recebido como parametro.
        '''
        if arestas is not None:
            for vetor in arestas:
                if len(vetor) == 2 and self.__pesos == False:
                    if self.__direcionado == False:
                        self.__matrizAdjacencia[max(vetor)][min(vetor)] = 1
                    else:
                        self.__matrizAdjacencia[vetor[0]][vetor[1]] = 1
                    self.__numeroArestas += 1
                elif len(vetor) == 3 and self.__pesos == True:
                    if self.__direcionado == False:
                        self.__matrizAdjacencia[max(vetor[:-1])][min(vetor[:-1])] = vetor[2]
                    else:
                        self.__matrizAdjacencia[vetor[0]][vetor[1]] = vetor[2]
                    self.__numeroArestas  += 1
                else:
                    #caso sejam passadas arestas com configuracao errada de peso
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
        aux = []
        lixo = []
        fila= []
        for vertice1 in range(self.__numeroVertices):
            for vertice2 in range(self.__numeroVertices):
                if self.__matrizAdjacencia[vertice1][vertice2] != 0:
                    aux.append((vertice1,vertice2))
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
    def gerarGrafoLista(self):
        '''
        retorna um objeto da classe GrafoLista identico ao self
        '''
        from grafo_lista import GrafoLista #o import foi feito aqui para evitar lopping de import entre as duas classes de grafo
        arestas = GrafoMatriz.__gerarArestas(self,True)
        return GrafoLista(
            numeroVertices= self.__numeroVertices,
            arestas= arestas , 
            direcionado= self.__direcionado , 
            pesos= self.__pesos
        )
    
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
    
    def adj(self, vertice):
        '''
        metodo feito para utilizacao das buscas por largura e profundidade, retorna uma lista de tuplas de todas as arestas
        adjacentes a um determinado vertice.
        '''
        arestas = []
        temp = GrafoMatriz.__gerarArestas(self,False, vertice)
        for u in temp:
            if self.__direcionado == True and u[0] == vertice:
                arestas.append(u)
            elif self.__direcionado == False and (u[0] == vertice or u[1] == vertice):
                #organiza as arestas caso o grafo não seja drecionado, trocando a posição do vertice buscado pra senpre ficar no indice 0.
                if u[1] == vertice:
                    u = list(u)
                    aux = u[1]
                    u[1] = u[0]
                    u[0] = aux
                    u = tuple(u)
                arestas.append(u)
        return arestas
    
    def adicionarAresta(self, aresta):
        '''
        recebe uma aresta contendo dois valores caso seja sem pesos ou tres valores caso haja pesos e realiza
        a adicao da aresta na matriz de adjacencia.
        '''
        if self.__direcionado == True:
            if self.__pesos == True:
                self.__matrizAdjacencia[aresta[0]][aresta[1]] = aresta[2]
                self.__numeroArestas += 1
            else:
                self.__matrizAdjacencia[aresta[0]][aresta[1]] = 1
                self.__numeroArestas += 1
        else:
            if self.__pesos == True:
                temp = aresta[:-1]
                self.__matrizAdjacencia[max(temp)][min(temp)] = aresta[2]
                self.__numeroArestas += 1
            else:
                self.__matrizAdjacencia[max(aresta)][min(aresta)] = 1
                self.__numeroArestas += 1
    
    def removerAresta(self, aresta):
        '''
        recebe como parametro um iteravel contendo um par de vertices que representa os terminais da aresta e 
        realiza a remocao da matriz de adjacencia.
        '''
        if self.__direcionado == False:
            self.__matrizAdjacencia[max(aresta)][min(aresta)] = 0
            self.__numeroArestas -= 1
        else:
            self.__matrizAdjacencia[aresta[0]][aresta[1]] = 0
            self.__numeroArestas -= 1
        
    
    def checaAresta(self, v1, v2):
        '''
        recebe dois vertices e retorna True caso haja uma aresta entre eles e False caso não.
        '''
        if (
            self.__matrizAdjacencia[v1][v2] != 0
            or self.__matrizAdjacencia[v2][v1] != 0
            ):
                return True
        return False

    def grauEntrada(self, vertice):
        '''
        checa o grau de entrada de um determinado vertice, caso o grafo não seja direcionado o vertice ficara com graus
        de entrada e saida iguais.
        '''
        grau = 0
        for verticeSaida in range(self.__numeroVertices):
                try:
                    if self.__matrizAdjacencia[verticeSaida][vertice]:
                        grau += 1
                except:
                    pass
        if self.__direcionado is True:
            return grau
        else:
            for verticeSaida in range(self.__numeroVertices):
                try:
                    if self.__matrizAdjacencia[vertice][verticeSaida] and verticeSaida != vertice:
                        grau += 1
                except:
                    pass
        return grau
    
    def grauSaida(self, vertice):
        '''
        checa o grau de saida de um determinado vertice, caso o grafo não seja direcionado o vertice ficara com graus
        de entrada e saida iguais.
        '''
        grau = 0
        for verticeEntrada in range(self.__numeroVertices):
                try:
                    if self.__matrizAdjacencia[vertice][verticeEntrada]:
                        grau += 1
                except:
                    pass
        if self.__direcionado is True:
            return grau
        else:
            for verticeEntrada in range(self.__numeroVertices):
                try:
                    if self.__matrizAdjacencia[verticeEntrada][vertice] and verticeEntrada != vertice:
                        grau += 1
                except:
                    pass
        return grau




if __name__ == '__main__':
    a = GrafoMatriz(5,[(0,1,10),(1,2,11),(2,3,12),(3,1,13)], pesos=True, direcionado=True)
    print(a.checaAresta(1,4))
    print(a.tree)
    #print(a.__repr__())
    print(a)
    a.removerAresta((3,1))
    print('')
    print(a)
    #print(a[4])
    b = a.gerarGrafoLista
    print(type(b))
    print(a.adj(1))