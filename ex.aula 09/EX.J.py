# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino,  M - Masculino, Gênero Inválido.


for letra in range(1):
    letra = input('Digite uma letra:')
    if letra == "F":
        print('feminino')
    elif letra == "M":
        print('Masculino')
    else:
        print('Gênero Inválido')