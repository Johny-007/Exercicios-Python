from math import trunc,sqrt
print (" \n ola, seja bem vindo a calculadora elfo \n vamos calcular a hipotenusa de um triangulo retangulo \n \n")
catop = float(input("  -qual o cateto oposto desse triangulo: "))
catadj = float(input("  -qual o cateto adjacente desse triangulo: "))
r4co = catop**2
r4ca = catadj**2
r4 = r4co + r4ca
hip = sqrt(r4)
print (f"o valor da hipotenusa desse triangulo é de: \033[7m{hip:.2f}\033[m")