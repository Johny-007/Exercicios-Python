print ("\n seja bem vindo a caragem elfica\n vamos ver quanto vc tem a nos pagar...")
d = int(input("  -quantos dias vc usou o carro: "))
km = float(input("  -quantos km vc rodou com o carro: "))
vd = d*60
vkm = km*0.15
v = vd+vkm
print (f" vc tera q pagar {v:.2f}RS pelo aluguel do carro")