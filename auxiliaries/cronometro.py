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

import time

class Cronometro:
	def __init__(self):
		self.__time = 0
		self.__status = False

	def start(self):
		self.__status = True
		self.__time_initial = time.clock()

	def stop(self):
		self.__status = False
		self.__time_end = time.clock()
		self.__time += self.__time_end - self.__time_initial

	def clear(self):
		self.__status = False
		self.__time = 0

	def __str__(self):
		if self.__status == True:
			self.__time = (
				(time.clock() - self.__time_initial) if self.__time == 0 
				else (time.clock() - self.__time_initial) + self.__time
				)
		return '{0} segs'.format(self.__time)

	def __repr__(self):
		return 'Status: {0} , '.format(
			'Running' if self.__status == True
			else 'Stopped'
			) + self.__str__()