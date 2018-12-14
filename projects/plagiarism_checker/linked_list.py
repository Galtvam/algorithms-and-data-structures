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

	
class Lista:
	'''
	Classe responsável por estruturar uma lista encadeada, contendo todos os métodos básicos que compunham sua estruturas
	'''
		
	class No:
		'''
		Classe responsável pela criação da estrutura No, podendo ser vazio, com ou sem referencia e conteudo
		'''
		def __init__(self, contend=None, ref=None, ante = None):
			self.item = contend
			self.prox = ref
	
	class Iterator:
		'''
		Classe de criação do iterador, estrutura responsavel por retornar os itens durante uma iteração
		'''
		def __init__(self, lista):
			self.__apontador = lista.__getitem__(0,'private')

		def __iter__(self):
			return self
			
		def __next__(self):
			try:
				aux = self.__apontador.item
				self.__apontador = self.__apontador.prox
				return aux
			except:
				raise StopIteration()   
		
	def __init__(self, contend=None):
		'''
		Inicia a estrutura da Lista
		'''
		self.__structure = Lista.No()
		self.__primeiro = self.__structure
		self.__ultimo = self.__structure
		self.__len = 0
		if contend is not None:
			'''
			Caso a Lista já deva iniciar com conteudo
			'''
			self.__preencher(contend)
	
	def __iter__(self):
		'''
		Retorna o objeto iterador para iteração
		'''
		return self.Iterator(self)
	

	def __str__(self):
		string = '['
		box = self.__primeiro.prox
		while box != None:
			string += (str(box.item) + ';') if type(box.item) is not str else '"{0}",'.format(box.item)
			box = box.prox
		string = '[' + string[:-1] + ']'
		return string
		
	def __repr__(self):
		'''
		Retorna uma forma válida de criação do objeto Lista idêntico
		'''
		string = self.__str__()
		return 'Lista('+string+')'

	def __len__(self):
		'''
		Retorna o comprimento da Lista
		'''
		return self.__len

	def __getitem__(self, indice,call='public'):
		'''
		Retorna o valor do objeto armazenado com o indice solicitado
		'''
		indice = (indice + len(self)) if  indice < 0 else indice
		if indice >= 0:
			temp = self.__primeiro.prox
		try:
			while indice >= 1:
				temp = temp.prox
				indice -= 1
			if call is 'private':
				return temp
			return temp.item
		except:
			raise IndexError                            
	
	def __setitem__(self, indice, contend):
		'''
		Quando o usuário realizar a operação de atribuição de valor direto pelo indice
		'''
		self.__getitem__(indice, 'private').item = contend

	def __contains__(self, contand):
		'''
		Responsável pelo comportamento do metodo In
		'''
		try:
			self.procurar(contand)
			return True
		except:
			return False

	def __preencher(self, contend):
		'''
		Realiza a povoação da lista durante a inicialização
		'''
		if type(contend) is not str:
			self.estender(contend)
		else:
			self.anexar(contend)

	def anexar(self, contend):
		'''
		Insere um novo item ao fim da Lista já previamente definida
		'''
		self.__len += 1
		novo = Lista.No(contend)
		if self.__primeiro is self.__ultimo:
			self.__structure.prox = novo
			self.__ultimo = novo
		else:
			self.__ultimo.prox = novo
			self.__ultimo = novo
			
	def inserir(self, indice, contend):
		'''
		Realiza a inserção através de uma chave passando-se juntamente o conteúdo
		'''
		temp = self.__primeiro
		while indice > 0 and temp is not None:
			temp = temp.prox
			indice -= 1
		if indice > 0:
			self.anexar(contend)
		elif indice < 0:
			raise IndexError
		else:
			novo = Lista.No(contend,temp.prox,temp)
			temp.prox = novo
			self.__len += 1
		 
	def tirar(self, indice=None):
		'''
		Realiza a remoção de um elemento através do indice recebido, por padrão retira o último
		'''
		if indice is None:
			temp = self.__primeiro
			while temp.prox is not self.__ultimo:
				temp = temp.prox
			aux = temp.prox
			temp.prox = None
			self.__ultimo = temp
			self.__len -= 1
			return aux.item
		else:
			temp = self.__primeiro
			while indice > 0 and temp.prox.item is not None:
				temp = temp.prox
				indice -= 1
			if indice > 0 or indice < 0:
				raise IndexError
			else:
				if temp.prox != self.__ultimo:
					aux_retorno = temp.prox
					temp.prox = aux_retorno.prox
					aux_retorno.prox = None
					self.__len -= 1
					return aux_retorno.item
				else:
					aux_retorno = temp.prox
					temp.prox = aux_retorno.prox
					self.__ultimo = temp
					aux_retorno.prox = None
					self.__len -= 1
					return aux_retorno.item
	
	def remover(self, contend):
		'''
		Realiza a remoção do primeiro item com o conteúdo passada
		'''
		temp = self.__primeiro
		try:
			while temp.prox.item != contend:
				temp = temp.prox
		except:
			raise ValueError    
		aux_retorno = temp.prox
		temp.prox = aux_retorno.prox
		aux_retorno.prox = None
		if aux_retorno == self.__ultimo:
			self.__ultimo = temp
		self.__len -= 1
		return aux_retorno.item
				
	def procurar(self, contend):
		'''
		Retorna o indice de um objeto que possui o conteúdo passado como parâmetro
		'''
		indice = 0
		temp = self.__primeiro.prox
		try:
			while temp.item != contend:
				temp = temp.prox
				indice += 1
			return indice
		except:
			raise ValueError

	def eliminar(self, contend):
		'''
		Realiza a remoção de todos os objetos que possuem o conteudo idêntico ao parâmetro
		'''
		temp = self.__primeiro
		cont = 0
		while temp.prox != None:
			if temp.prox.item is contend:
				cont += 1
				aux = temp.prox
				if aux == self.__ultimo:
					self.__ultimo = temp
					temp.prox = None
					self.__len -= 1
				else:
					temp.prox = aux.prox
					aux.prox = None
					self.__len -= 1
				del aux
			if temp.prox != None:
				temp = temp.prox
		if cont == 0:
			raise ValueError
	
	def trocar(self, indice1, indice2):
		'''
		Recebe dois indices como parâmetro e inverte o conteúdo presente nos objetos
		'''
		aux_indice = 0
		temp = self.__primeiro.prox
		try:
			while aux_indice < indice2:
				if indice1 == aux_indice:
					aux_valor = temp
				temp = temp.prox
				aux_indice += 1
			aux_valor2 = temp
			aux_troca = aux_valor.item
			aux_valor.item = aux_valor2.item
			aux_valor2.item = aux_troca
			del aux_troca
		except:
			raise IndexError
			
	def estender(self, iteravel):
		'''
		Insere ao fim da Lista o conteudo de um outro objeto iteravel passado como parâmetro
		'''
		for k in iteravel:
			self.anexar(k)
	
	def copiar(self):
		'''
		Retorna um objeto Lista idêntico ao self
		'''
		return Lista(self)
						
def concatenar(lista1, lista2):
	'''
	Recebe duas Listas como parâmetro e retorna um novo objeto composto pela concatenação das duas Listas
	'''
	aux = lista1.copiar()
	aux.estender(lista2)
	return aux