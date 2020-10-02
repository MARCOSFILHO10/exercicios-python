# Dada uma sequência de números inteiros, imprimir seus quadrados.
# Entradas do programa:
# nº de início da sequência = 0
# nº de fim da sequência = 4
# Saída do programa:
# sequência : 0, 1, 4, 9, 16


def quadradoFor(iniL, fimL):
    mensagem = ""
    for contador in range(iniL, fimL+1):
        tmp = contador**2
        mensagem = mensagem + str(tmp) + " "
    return (mensagem)

def main():
   inicio = int(input('Início:'))
   fim = int(input('Fim:'))
   print(quadradoFor(inicio, fim))




main()