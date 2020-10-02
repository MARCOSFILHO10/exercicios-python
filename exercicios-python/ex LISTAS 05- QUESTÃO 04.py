valores = [-3, 9, 12, -34, -2, 20, 10]
somapositivos = 0
quantnegativos = 0


for i in range(len(valores)):
    if valores[i] < 0:
        quantnegativos =+ 1
    else:
        somapositivos= somapositivos + valores[i]

print(' A soma dos valores posivos é:',somapositivos)
print(' A quantidade de valores negativos é:',quantnegativos)