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

from Documentos import Documents
from linked_list import Lista
from trie import Trie
import os

from memory_profiler import profile
from cProfile import Profile

class Corpus:
	'''
	Classe de representacao de um Corpus, o qual é composto por vários Documents de
	um mesmo path.
	'''

	def __init__(self, directory):
		'''
		Recebe como parametro um diretorio, criando assim um repertorio dos arquivos
		presentes no path.
		'''
		self.__directory = directory
		self.__all_documents, self.__trie_words_documents = Corpus.__create_documents(self, self.__directory)
		#self.__trie_words_documents = Corpus.__create_trie(self)
		self.__number_of_documents = len(self.__all_documents)

	def __str__(self):
		'''
		retorna uma representacao da lista com todos os documentos.
		'''
		return str(self.__all_documents)

	def __repr__(self):
		'''
		retorna uma forma valida de instanciar um Corpus identico ao atual.
		'''
		return 'Corpus("{0}")'.format(self.__directory)

	def __iter__(self):
		'''
		retorna o iterador sobre a lista dos Documents.
		'''
		return iter(self.__all_documents)

	def __getitem__(self, key):
		'''
		retorna o item indexado pela chave desejada.
		'''
		return self.__all_documents[key]

	def __len__(self):
		'''
		retorna o numero de Documents que compoem o Corpus.
		'''
		return self.__number_of_documents

	def __create_documents(self, directory):
		'''
		recebe um diretorio ao qual sao realizadas as instanciacoes dos Documents() e adiciona suas palavras a trie.
		'''
		archives = os.listdir(directory)
		documents = Lista()
		temp = Trie()
		for archive_name in archives:
			doc = Documents(directory+archive_name)
			documents.anexar(doc)
			for ngram in doc.ngrams:
				aux_words = ngram.sequence
				string = ''
				for k in aux_words:
					string += k + ' '
				temp.add(string,doc)
		return documents, temp	

	def check_plagiarism(self, document, limit):
		'''
		recebe um objeto Documents e um limiar de plagio, executa a verificacao de
		plagio e retorna uma lisca contendo os possiveis arquivos base do plagio.
		'''
		base_documents = {}
		for doc in self.__all_documents:
			base_documents[doc] = 0
		for ngram in document.ngrams:
			aux_words = ngram.sequence
			string = ''
			for k in aux_words:
				string += k + ' '
			docs_base = self.__trie_words_documents.search(string)
			if docs_base is not None:
				for doc in docs_base:
					base_documents[doc] += 1
		final_list = Lista()
		for pair in base_documents.items():
			restraint = pair[1]/len(pair[0])
			if restraint >= limit:
				final_list.anexar(pair[0].local)
		return final_list

	@property
	def directory(self):
		'''
		retorna o diretorio que originou o Corpus.
		'''
		return self.__directory