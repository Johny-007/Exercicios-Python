import moeda

preço = float(input("  -Digite o valor: R$"))
print(f"O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}")
