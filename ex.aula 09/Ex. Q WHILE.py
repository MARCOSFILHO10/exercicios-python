# Exercicio O WHILE- Calcule sua tabuada!


def main():

    num = int(input('Digite um valor para ver sua tabuada:'))
    cont = 1
    while cont+1 <= 10:
        cont += 1
        print('{} x {} = {}'.format(cont, num, (num*cont)))


main()