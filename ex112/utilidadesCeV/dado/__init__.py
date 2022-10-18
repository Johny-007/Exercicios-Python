def leiaDinehiro(inputMoney):
    valido = False
    while not valido:
        preço = str(input(inputMoney)).replace(",", ".")
        if preço.isalpha() or preço.strip(" ") == "":
            print(f"\033[31m    -ERRO!! '{preço}' não validado!!-\033[m")
        else:
            float(preço)
            return preço
            valido = True
