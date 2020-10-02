import random


def escrevernumerosaleatorios(qntnumeros, nomearquivo):
    arquivonumero = open(nomearquivo, "w")
    for i in range(qntnumeros):
        arquivonumero.write(str(random.randint(0, 100)))
        arquivonumero.write("\n")
    arquivonumero.close()


escrevernumerosaleatorios(10, 'C:/Users/Marcos/aleatorios.txt')