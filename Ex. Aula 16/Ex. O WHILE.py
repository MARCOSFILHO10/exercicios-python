# Dada uma sequência de números inteiros, imprimir seus quadrados.
# Entradas do programa:
# nº de início da sequência = 0
# nº de fim da sequência = 4
# Saída do programa:
# sequência : 0, 1, 4, 9, 16


def Quadradowhile(iniL,fimL):
    mensagem = ""

    while(iniL <= fimL):
        tmp = iniL **2
        mensagem = mensagem + str(tmp) + " "
        iniL += 1
    return (mensagem)

def main():
   inicio = int(input('Início:'))
   fim = int(input('Fim:'))
   print(Quadradowhile(inicio, fim))


main()