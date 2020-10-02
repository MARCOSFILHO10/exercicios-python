def main():

    n = int(input('Digite o valor de n:'))
    f = 1

    for i in range(1, n+1):
         f = f * (i)

         print('O valor fatorial de n é igual a:', f)

main()