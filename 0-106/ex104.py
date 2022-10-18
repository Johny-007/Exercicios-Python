def leiaINT(txt):
    numero = 0
    valido = False
    while True:
        num = str(input(txt))
        if num.isnumeric():
            numero = int(num)
            valido = True
        else:
            print("\033[1;31;40m ERRO, DIGITE UM NMR INT\033[m")
        if valido:
            break
    return numero

n = leiaINT("Digite um nmr: ")
print(f"-Voce digitou o nmr: {n}")