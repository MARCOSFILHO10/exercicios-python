def main():

    n = int(input('Digite o valor de n:'))
    fat = 1
    i = 1
    while i <= n:
        fat = fat * i
        i += 1

        print('O valor fatorial de n é igual a:', fat)


main()