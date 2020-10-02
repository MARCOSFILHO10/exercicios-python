def escrevermedia ( nomearquivo):
    arquivonumero = open(nomearquivo)
    soma = 0
    qntnumeros = 0
    for num in arquivonumero:
        num = float(num)
        soma += num
        qntnumeros += 1
    arquivonumero.close()
    return soma / qntnumeros


print(escrevermedia('C:/Users/Marcos/aleatorios.txt'))