def solucao1 (x,y):
    return((2*x)* (y/2))

def solucao2 (x,z):
    return ((x*3) + z)

def solucao3 (z):
    return ((z**3))

def main ():
    x = int(input('valor1:'))
    y = int(input('valor2:'))
    z = float(input('valor3:'))

    resultado1 = solucao1(x, y)
    print(resultado1)

    resultado2 = solucao2(x,z)
    print(resultado2)

    resultado3 = solucao3(z)
    print(resultado3)

main()