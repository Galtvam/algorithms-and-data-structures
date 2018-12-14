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

from memory_profiler import profile
from cProfile import Profile

class Ngram:
	'''
	Classe de representacao de um Trigram.
	'''
	def __init__(self, document, indexInitial, size):
		'''
		Recebe do usuario a referencia do documento pai do ngrama, o indice do inicio do ngrama e o size, respectivamente.
		'''
		try:
			self.__lastIndex = indexInitial + (size - 1)
			test = document.words[self.__lastIndex]
			del test
			self.__firstIndex = indexInitial
			self.__document = document
			self.__size = size
		except: 
			#Caso o indice final esteja fora do range do vetor de palavras levanta um indexError
			raise IndexError('The last index is out of range of the document.')

	def __str__(self):
		'''
		retorna uma representação em string da sequencia de palavras existentes no array
		'''
		return str(self.__document.words[self.__firstIndex:self.__lastIndex+1])

	def __repr__(self):
		'''
		retorna uma maneira valida para se instanciar um Ngrama igual
		'''
		return  'Ngrama({0},{1},{2})'.format(self.__document,self.__firstIndex,self.size)

	def __eq__(self, other):
		'''
		realiza a comparação dos elementos contidos nos Ngramas, caso o parametro passado tenha um size !=
		um raise e levantado.
		'''
		if self.size == other.size:
			equality = True
			for i in range(self.__size):
				equality = equality and (self.sequence[i] == other.sequence[i])
			return equality
		else: raise ValueError('Parameter size is different')

	@property
	def sequence(self):
		'''
		retorna ao usuario uma lista contendo a sequencia de palavras do ngrama.
		'''
		return self.__document.words[self.__firstIndex:self.__lastIndex+1]

	@property
	def size(self):
		'''
		retorno o tamanho do Ngrama
		'''
		return self.__size

	@property
	def document(self):
		'''
		retorno o documento pai do Ngrama
		'''
		return self.__document