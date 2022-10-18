import random
print (" \n \n irei escolher um nmr de 0 a 5 \n lhe desafio a adivinhar qual sera o nmr")
n = random.randint(0, 5)
p = int(input(" -qual nmr vc acha q foi escolhido? "))
if p == n:
    print ("\n minha nossa nossa nossa! vc acertou hehe! ")
else:
    print (f"\n hihi vc errou hihihi, o nmr q eu escolhi foi {n}")
print ("       ----fim de jogo----")
