def calc_media( nota1, nota2, nota3, tipomedia):
    if tipomedia == 'a':
        return (nota1+nota2+nota3)/3
    elif tipomedia == 'p':
        return (nota1*5+nota2*3+nota1*2)/10
    elif tipomedia == 'h':
        return (3/(1/nota1 + 1/nota2 + 1/nota3))
    else:
        return 0


print(f"A média é: {calc_media(10, 7, 9,'h'):.2f}")