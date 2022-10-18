import random
print (" \n programa de sorteio, vamos sortear um aluno \n teremos cinco sorteados, liste tais:")
al1 = str(input("aluno 1: "))
al2 = str(input("aluno 2: "))
al3 = str(input("aluno 3: "))
al4 = str(input("aluno 4: "))

lista = [al1,al2,al3,al4]
sort = random.choice(lista)
print (f"\n o/a grande sorteado(a) foi o(a) {sort}")