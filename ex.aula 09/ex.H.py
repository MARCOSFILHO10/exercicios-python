#faça um programa que pergunte o preço de três produtos e informe qual produto voçê deve comprar, sabendo que a decisão e sempre o mais barato!

produto1 = float(input('valor do produto1:'))
produto2 = float(input('valor do produto2:'))
produto3 = float(input('valor do produto3:'))

if produto1 < produto2 and produto1 < produto3:
        print('O menor valor é produto1')
        print('O menor valor é',produto1)

if produto2 < produto1 and produto2 < produto3:
        print('O menor valor é produto2')
        print('O menor valor é', produto2)

else:
        print('O menor valor é produto3')
        print('O menor valor é:',produto3)