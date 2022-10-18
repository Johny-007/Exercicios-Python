import moeda

preço = float(input("  -Digite o valor: R$"))
print(f"O dobro de {moeda.moedaRS(preço)} é {moeda.dobro(preço)}")
print(f"O dobro de {moeda.moedaRS(preço)} é {moeda.dobro(preço, False)}")