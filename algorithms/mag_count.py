def conta_somas(vetor):
	qnt = 0
	size = vetor.size - 1
	for i in range(size - 1):
		valor_i = -vetor[i]
		for y in range(i+1, size):
		    qnt += (vetor[y+1:]== (valor_i - vetor[y])).sum()
	return qnt