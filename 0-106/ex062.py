term = int(input("  -GERADOR DE P.A-\nDigite o primeiro termo: "))
raz = int(input('Digite a razão: '))
pa = term
contador = 0
a_mais = 0
fim = 10
while contador < fim + a_mais :
    print (f' {pa} => ', end='')
    contador += 1
    pa += raz
    if contador == fim:
        a_mais = int(input(' PAUSE - deseja ver mais qnts termos? '))
        fim += a_mais
        if a_mais == 0:
            print (f'foram mostrados {contador} termos')
            break
print (' acabou')