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

def conta_somas(vetor):
	qnt = 0
	size = vetor.size - 1
	for i in range(size - 1):
		valor_i = -vetor[i]
		for y in range(i+1, size):
		    qnt += (vetor[y+1:]== (valor_i - vetor[y])).sum()
	return qnt
