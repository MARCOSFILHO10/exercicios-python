# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.


valor_lata = 80
tamanho_em_m = float(input('Qual tamanho em m² da área:'))
quant_latas = float(input('Quantidade de latas:'))
preço_total = (valor_lata*quant_latas)
print('Para utilizar {} de latas de tintas, o custo total será de {} R$'.format(quant_latas,preço_total))