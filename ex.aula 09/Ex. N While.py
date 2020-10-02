def main():
    numClientes = int(input('Digite o número de clientes:'))
    totalTempoEspera = 0
    cont = 1
    while (cont <= numClientes):
        tempoEspera = float(input("tempo de espera dos clientes:"+str(cont)))
        totalTempoEspera += tempoEspera
        cont += 1

    mediaTempo = totalTempoEspera/numClientes
    print('Tempo médio de espera é:',mediaTempo)

main()