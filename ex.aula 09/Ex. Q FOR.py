# Exercicio O - Calcule sua tabuada!


def main():

    num = int(input('Digite um valor para ver sua tabuada:'))
    for c in range(1, 11):
        print('{} x {:2} = {}'.format(num, c, num*c))


main()