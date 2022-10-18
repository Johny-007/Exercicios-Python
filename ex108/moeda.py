def aumentar(preço, porcentagem):
    valor = (preço * (porcentagem/100)) + preço
    return valor

def dimunuir(preço, porcentagem):
    valor = preço - (preço * (porcentagem / 100))
    return valor

def dobro(preço):
    dobro = preço*2
    return dobro

def metade(preço):
    metade = preço/2
    return metade

def moeda(valor):
    valor01 = f"{valor:.2f}"
    valor02 = f"R${valor01}"
    return valor02
