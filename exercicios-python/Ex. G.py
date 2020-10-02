# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao IPRF
# c. quanto pagou ao INSS.
# d. quanto pagou ao sindicato.
# e. o salário líquido.
# f. o valor descontado.

def calculaSalario (valorHoras, numHoras):
    return (valorHoras * numHoras)

def calculo_irpf(salarioBruto, irpf):
    return (salarioBruto) * (irpf)

def calculo_inss(salarioBruto, inss):
    return (salarioBruto) * (inss)

def calculo_sind(salarioBruto, sind):
    return (salarioBruto) * (sind)

def valor_total_desp (irpf, inss, sind):
    return (sind) + (inss) + (irpf)

def desc_total(valorSind, valorInss, valorIrpf):
    return (valorSind) + (valorInss) + (valorIrpf)

def salario_liquido(calculaSalario, valorIrpf, valorInss, valorSind):
    return (calculaSalario) - (valorIrpf) - (valorInss) - (valorSind)


def main():
    valorHoras = float(input('valor de horas trabalhadas:'))
    numHoras = float(input('numero de horas trabalhadas:'))
    inss = (8/100)
    irpf = (11/100)
    sind = (5/100)
    valor_tot_desp = (inss, irpf, sind)

    valorSalarioBruto = calculaSalario(valorHoras, numHoras)
    print('O valor do salário bruto é:',valorSalarioBruto)

    valorIrpf = calculo_irpf(valorSalarioBruto, irpf)
    print('O valor do imposto de renda é:',valorIrpf)

    valorInss = calculo_inss(valorSalarioBruto, inss)
    print('O valor do INSS é:',valorInss)

    valorSind = calculo_sind(valorSalarioBruto, sind)
    print('O valor do sindicato é:',valorSind)

    valor_total_desp = desc_total(valorSind, valorInss, valorIrpf)
    print('O valor total dos descontos é:',valor_total_desp)

    valor_liquido = salario_liquido(valorSalarioBruto, valorIrpf, valorInss, valorSind)
    print('O valor do salário liquido é:',valor_liquido)

main()
