def moedaRS(valor):
    valor01 = f"{valor:.2f}"
    valor02 = f"R${valor01}"
    return valor02


def aumentar(preço, porcentagem, moeda=True):
    valor = (preço * (porcentagem/100)) + preço
    if moeda:
        return moedaRS(valor)
    else:
        return valor


def dimunuir(preço, porcentagem, moeda=True):
    valor = preço - (preço * (porcentagem / 100))
    if moeda:
        return moedaRS(valor)
    else:
        return valor


def dobro(preço, moeda=True):
    dobro = preço*2
    if moeda:
        return moedaRS(dobro)
    else:
        return dobro


def metade(preço, moeda=True):
    metade = preço/2
    if moeda:
        return moedaRS(metade)
    else:
        return metade


def resumo(preço, p100aumenta, p100diminui):
    print("\n", "-"*33, f"\n{'RESUMO':^33}", f"""\n- O dobro de {moedaRS(preço)} é: {dobro(preço)}
- A metade de {moedaRS(preço)} é: {metade(preço)}    
- {p100aumenta}% aumentado é: {aumentar(preço, p100aumenta)}
- {p100diminui}% diminuido é: {dimunuir(preço, p100diminui)}
""", "-"*33)
