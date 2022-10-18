print ('\n  seja bem vindo a transportadora elfica\n   deseja uma passagem certo?\n')
city = str(input(" -qual cidade deseja ir? "))
km = int(input(" -qunts KM daqui até la? "))
if km<=200:
    print (f"\n  o preço da sua passagem á {city} será: R${km**0.50:.2f}")
else:
    print (f"\n  o preço da sua passagem á {city} será: R${km**0.45:.2f}")