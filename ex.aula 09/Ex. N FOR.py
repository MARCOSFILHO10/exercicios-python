# Entrei no banco e quero saber o meu tempo médio de espera.
# Faça um programa que calcule e mostre a média aritmética de um cliente, baseado nos tempos de espera dos clientes anteriores (máximo 5  clientes).
def main():
    numClientes = int(input('Digite o número de clientes:'))
    tempoTotalEspera = 0
    for c in range(0, numClientes):
        tempoEspera = int(input('Digite o tempo de espera:'+str(c)+':'))
        tempoTotalEspera += tempoEspera

    mediaTempo = tempoTotalEspera / numClientes
    print('Tempo total de espera:',tempoTotalEspera)
    print('O tempo médio de espera é:', mediaTempo)

main()