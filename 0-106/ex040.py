print ("""\n Seja bem vindo á central da escola
 Deseja saber sobre sua aprovação certo?
            vamos ver\n""")
n1 = float(input("  -Qual foi sua nota no 1b: "))
n2 = float(input("  -Qual foi sua nota no 2b: "))
n3 = float(input("  -Qual foi sua nota no 3b: "))
n4 = float(input("  -Qual foi sua nota no 4b: "))
nota = (n1 + n2 + n3 + n4) / 4
if nota < 5.0:
    print(" \nSentimos muito em dizer q vc foi REPROVADO.. ")
elif nota >= 5.0 and nota < 6.9:
    print(" \nprecamos em dizer q vc está de RECUPERAÇÃO.. ")
elif nota >= 7.0:
    print(" \nFicamos encareçidos em dizer q vc foi APROVADO")
print("                FIM")