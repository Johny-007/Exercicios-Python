print ("\nola pequeno gafanhoto\n")
n1 = int(input("  -digite um nmr: "))
n2 = int(input("  -digite um nmr: "))
n3 = int(input("  -digite um nmr: "))
#verificando o maior
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
#verificando o menor
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
#conlusao
print(f"""-----------------------
  -o valor maior foi \033[7m{maior}\033[m
  -o valor menor foi \033[7m{menor}\033[m""")
