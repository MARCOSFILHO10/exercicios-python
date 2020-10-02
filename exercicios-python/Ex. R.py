# ------EXERCICIO O--------

# Digite um número e descubra se ele é um palíndromo.
# Palíndromo:
# 1º algarismo de n é igual ao seu último algarismo,
# 2º algarismo de n é igual ao penúltimo algarismo, e assim sucessivamente

def main():
    checkPalindrome(str(input('Digite um número para verificar se é palindromo: ')))


def checkPalindrome(value):
    forceStr = list(value)
    reverseStr = forceStr[::-1]
    if forceStr == reverseStr:
        print('O número  é palindromo')
    else:
        print('O número  não é palindromo')

main()
