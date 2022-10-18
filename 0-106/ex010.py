print ("ola, seja bem vindo a corretora elfo \n \n -deseja converter seu real em dollar, certo ")
r = float(input(" -quantos reais vc tem? "))
d = r/3.27
print (f" -com {r:.2f} RS vc podera comprar \033[1;30;107m{d:.2f} US\033[m")