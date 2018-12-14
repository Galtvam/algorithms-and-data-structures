#coding: utf-8
'''
Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
Centro de Informatica -- CIn (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF969 -- Algoritmos e Estruturas de Dados

Autor:    Marcos Antonio Tavares Galvão
Email:	  matg@cin.ufpe.br

Licenca: The MIT License (MIT)
Copyright(c) 2018 Marcos Antonio Tavares Galvão
'''

from Ngrama import Ngram
from linked_list import Lista
from trie import Trie
import numpy as np
import re
import os

from memory_profiler import profile
from cProfile import Profile

class Documents:
	'''
	Classe de representacao de um Documento,guarda o local do arquivo, as palavras, os ngramas e a quantidade
	de ngramas.
	'''
	def __init__(self, archive):
		'''
		Recebe do usuario o direorio do arquivo e realiza sua leitura e producao de ngramas
		'''
		self.__archive = archive
		self.__words = np.array(Documents.__get_words(self,archive))
		self.__ngrams = Documents.__getNgrams(self,self.__words)
		self.__ngrams_size = len(self.__ngrams)

	def __str__(self):
		'''
		retorna uma string contendo informaoes sobre o documento: quantidade de palavras e
		quantidade de ngramas
		'''
		return 'Document path: {0}'.format(self.__archive)

	def __repr__(self):
		'''
		retorna uma maneira valida para se instanciar um Ngrama igual
		'''
		return 'Documents("{0}")'.format(self.__archive)

	def __len__(self):
		'''
		retorna a quantidade de palavras validas existentes no documento
		'''
		return len(self.__words)

	def __get_words(self, archive):
		'''
		recebe o diretorio do arquivo, executa sua leitura e normalizacao, retorna uma lista de palavras
		validas
		'''
		def normalize(text):
			'''
			executa a normalizacao do texto, retira todos os caracteres que sao simbolos e retorna uma
			lista com as palavras normalizadas
			'''
			exp = r'[^\w ]{1}'
			exp_breaks = r'\s{1,}'
			final_phrase = re.sub(exp_breaks, ' ', text).lower()
			final_phrase = re.sub(exp, '', final_phrase)
			return final_phrase.split(' ')
		arq = open(archive,'r',encoding='utf8')
		words = arq.read()
		arq.close()
		words = normalize(words)
		final_words = Lista()
		for ind in range(len(words)):
			if len(words[ind]) != 0 and words[ind].isalpha():
				final_words.anexar(words[ind])
		return final_words

	def __getNgrams(self,words):
		'''
		recebe uma lista de palavras, realiza o procedimento de instanciacao dos objetos Ngram
		contendo uma sequencia de 3 palavras, retorna a Lista encadeada contendo os objetos.
		'''
		ngrams_list = Lista()
		for i in range(len(words)-2):
			ngrams_list.anexar(Ngram(self,i,3))
		return ngrams_list

	def restraint(self, other_document):
		'''
		modo contencao, recebe um documento como parametro e realiza a comparacao dos objetos,
		obtem a interseccao realiza o calculo e retorna o valor da contencao
		'''
		other_document_backup = other_document.ngrams.copiar()
		repet = 0
		for ng1 in self.ngrams:
			flag = False
			for ng2 in other_document_backup:
				if ng1 == ng2:
					repet += 1
					flag = True
					break
			if flag == True: other_document_backup.remover(ng2)
		rest_of_document = (repet/other_document.ngrams_size)
		return rest_of_document

	@property
	def local(self):
		'''
		retorna o local original do arquivo
		'''
		return self.__archive

	@property
	def words(self):
		'''
		retorna o ndarray contendo as palavras do documento
		'''
		return self.__words

	@property
	def ngrams(self):
		'''
		retorna a lista encadeada contendo as sequencias de ngramas
		'''
		return self.__ngrams

	@property
	def ngrams_size(self):
		'''
		retorna a quantidade de ngramas de um documento
		'''
		return self.__ngrams_size