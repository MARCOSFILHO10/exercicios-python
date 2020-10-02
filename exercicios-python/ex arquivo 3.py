def escrevermedia(qntnumeros, nomearquivo):
    arquivonumero = open(nomearquivo)
    soma = 0
    for i in range(qntnumeros):
        num= float(arquivonumero.readline())
        soma += num

    arquivonumero.close()
    return soma / qntnumeros


print(escrevermedia(10,'C:/Users/Marcos/aleatorios.txt'))

