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

from linked_list import Lista

class Trie:
    '''
	Classe de representacao de uma Trie.
	'''
    class Node:
        '''
		Classe responsável pela criação da estrutura No, podendo ser vazio, com ou sem conteudo
		'''
        def __init__(self, key=None, contend=None):
            self.key = key
            self.__contend = Lista(contend)
            self.__references = Lista()

        def __contains__(self, key):
            '''
	    	Checa se uma key está dentro do node
		    '''
            for i in self.__references:
                if key == i.key:
                    return True
            return False
        def setReference(self, reference):
            '''
		    Adiciona uma referencia a listagem do node
		    '''
            if not(reference in self.__references):
                self.__references.anexar(reference)

        def setContend(self, contend):
            '''
		    Adiciona umconteudo a listagem do node
		    '''
            self.__contend.anexar(contend)

        def getReferenceOfKey(self, key):
            '''
		    Recebe uma key e retorna o node que possui aquela key dentro das referencias
		    '''
            for i in self.__references:
                if key == i.key:
                    return i
            print("Key not found.")

        @property
        def contend (self):
            '''
		    Retorna o conteudo do node
		    '''
            return self.__contend
        

    def __init__(self, word=None):
        self.__father = Trie.Node()
        self.__size = 0
        if word is not None:
            self.add(word)
    
    def __len__(self):
        '''
	    Retorna o numero de palavras da trie
		'''
        return self.__size
    
    def __search(self, word, masterParameter=0):
        '''
	    Realiza a busca de uma palavra na arvore
		'''
        ref = self.__father
        aux = Lista()
        aux.estender(word)
        while len(aux) > 0 and aux[0] in ref:
            ref = ref.getReferenceOfKey(aux[0])
            aux.remover(aux[0])
        if masterParameter == 0 and len(aux) == 0:
            temp = ref.contend
            if len(temp) != 0:
                return temp
            else:
                return None
        elif masterParameter == 1:
            return ref, aux
        else:
            return None

    def search(self, word):
        '''
        Retorna o conteudo de uma palavra ou None caso ela não exista
        '''
        return Trie.__search(self,word)
    
    def add(self, word, contend=None):
        '''
	    Adiciona uma palavra na trie
		'''
        aux, rest = Trie.__search(self,word, 1)
        if aux is not None:
            for k in rest:
                temp = Trie.Node(k)
                aux.setReference(temp)
                aux = temp
            aux.setContend(contend)
        self.__size += 1