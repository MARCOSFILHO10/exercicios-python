#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_por_hora = float(input('Quanto você ganha por hora: '))
numero_horas = float(input('Quantas horas trabalhadas por mês:'))
total_salario = (valor_por_hora*numero_horas)
print('O valor total do salário do mês é de {}' .format(total_salario))
