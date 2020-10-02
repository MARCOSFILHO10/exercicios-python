def copiaarquivo(velhoarquivo, novoarquivo):
    f1= open(velhoarquivo, "r")
    f2= open(novoarquivo, "w")
    for texto in f1:
        f2.write(texto)
    f1.close()
    f2.close()


copiaarquivo("C:/Users/Marcos/velho2.t"
             "xt", "C:/Users/Marcos/novo.txt")