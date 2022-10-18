import random
print ("   vamos fazer uma lista de apresentacao\n   digite o nome dos partipantes")
p1 = str(input(" -participante 1: "))
p2 = str(input(" -participante 4: "))
p3 = str(input(" -participante 3: "))
p4 = str(input(" -participante 4: "))
lista = [p1,p2,p3,p4]
random.shuffle(lista)
print (" \n a ordem de apresentacao sera: ")
print (lista)
