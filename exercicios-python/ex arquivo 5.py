def escrevermedia ( nomearquivo):
    arquivonumero = open(nomearquivo)
    soma = 0
    qntnumeros = 0
    num = arquivonumero.readline()
    while num != "":
        num = float(num)
        soma += num
        qntnumeros += 1
        num= arquivonumero.readline()
    arquivonumero.close()
    return soma / qntnumeros


print(escrevermedia('C:/Users/Marcos/aleatorios.txt'))