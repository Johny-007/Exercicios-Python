import random
print (" \n \n irei escolher um nmr de 0 a 5 \n lhe desafio a adivinhar qual sera o nmr")
cont = 1
n = random.randint(0, 5)
p = int(input(" -qual nmr vc acha q foi escolhido? "))
if p == n:
    print (' Ohhh nao, voce acertou de primeira, és ulton?')
else:
    while p != n:
        if p != n:
            cont += 1
            p = int(input(' Voce errou verme! tente novamente: '))
    print(f'\n OHH vc ganhou verme, parabens, mas poxa {cont} tentativas emmm')