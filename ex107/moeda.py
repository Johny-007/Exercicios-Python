def aumentar(preço, porcentagem):
    valor = (preço * (porcentagem/100)) + preço
    print(f"R${preço:.2f} aumentado {porcentagem}%: R${valor:.2f}")

def dimunuir(preço, porcentagem):
    valor = preço - (preço * (porcentagem / 100))
    print(f"R${preço:.2f} dimuniudo {porcentagem}%: R${valor:.2f}")

def dobro(preço):
    print(f"O dobro de R${preço:.2f} é: R${preço*2:.2f}")

def metade(preço):
    print(f'A metade de R${preço:.2f} é: R${preço/2:.2f}')