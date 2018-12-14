from Corpus import Corpus
from Documentos import Documents
from Ngrama import Ngram

'''
Arquivo de testes dos componentes Corpus, Documentos e Ngramas
'''

'''
*Trie
Para instanciar utilize Trie(palavra a ser adicionada)

Metodos implementados:
    __len__
    search
    add


*Ngrama
Para instanciar utilize Ngram(ref do obj documento, index da primeira palavra do ngrama, tamanho do ngrama)

Metodos implementados:
    __str__
    __repr__
    __eq__

Propertys implementados:
    sequence "retorna a sequencia de palavras que o Ngrama representa"
    size "tamanho do Ngrama"
    document "referencia do documento pai do Ngrama"


*Documentos
Para instanciar utilize Documents("diretorio relativo do arquivo")

Metodos implementados:
    __str__
    __repr__
    __len__
    restraint(referencia do documento a ser comparado)

Propertys implementados:
    local "retorna o diretorio do documento"
    words "retorna o ndarray contendo as palavras do documento"
    ngrams "retorna a lista encadeada contendo as sequencias de ngramas"
    ngrams_size "retorna a quantidade de ngramas de um documento"


*Corpus
Para instanciar utilize Corpus("diretorio contendo todos os arquivos que formaram o corpus")

Metodos implementados:
    __str__
    __repr__
    __iter__
    __getitem__
    __len__
    check_plagiarism("documento que sera testado", limite de contencao)

Propertys implementados:
    directory "retorna o diretorio que originou o Corpus"
'''

''' 
### Secao de testes da Trie ###
'''
#a = Trie()
#a.add("chuva","china")
#a.add("chuva","ola")
#print(a.search("chuva"))

''' 
### Secao de testes do Documento e Ngrama ###
'''
#a = 'dados/src/source-document00582.txt' #documento 1
#b = 'dados/susp/suspicious-document01282.txt' #documento 2
#c = Documents(a)
#print(c)
#print(len(c))
#print(c.ngrams_size)
#print(c.ngrams)
#d = Documents(b)
#print(c.__repr__())
#print(c.restraint(d)) #retorna a contenção entre os documentos

''' 
### Secao de testes do Corpus ###
'''
#test = Corpus('dados/src/')
#print(test)
#print(test.__repr__())

'''teste de um documento suspeito com o corpus confiavel'''
#doc = Documents('dados/susp/suspicious-document01091.txt')
#plagiaris = doc
#print(len(doc))
#ok = test.check_plagiarism(plagiaris, 0.3)
#print(ok)
    
'''teste de todos os documentos suspeitos com todos os documentos confiaveis'''	
#plagiaris = Corpus('dados/susp/')
#for i in plagiaris:
#	ok = test.check_plagiarism(i, 0.5)
#	print(ok)