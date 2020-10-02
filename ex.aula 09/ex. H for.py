def main():
    valorMinimo = 100000
    ordemProduto = 0
    for tmp in range(0, 50):
        produto = float(input('Qual valor do produto:'))

        if (produto < valorMinimo):
            valorMinimo = produto
            ordemProduto = tmp + 1

    print('O produto mais barato é',ordemProduto,':R$',valorMinimo)

main()