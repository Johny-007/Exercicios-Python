from random import randint
from time import sleep
linha = '-=-' * 25
vit = cont = 0
while True:
    valid = 0                                                            #validaçao de ímpar ou par
    print(linha)                                                         #separaçao
    n = int(input('\n escolha um nmr: '))                                #escolha
    i_p = str(input(' vc esolhe ímpar ou par[I/P]: ')).strip().upper()   #escolha
    print(linha)                                                         #separaçao
    if i_p == 'P': valid = 1                                             #validaçao de ímpar ou par
    if i_p == 'I': valid = 1                                             #validaçao de ímpar ou par
    if valid != 1:                                                       #validaçao de ímpar ou par
        print ('\n' * 50)                              #if erro          #separaçao
        print ('\n  -ESCOLHA ERRADA, É (I) OU (P)-')   #if erro          #txt
        continue                                       #if erro          #passe
    num_compt = randint(0,10)                                            #nmr computador
    print (f' O computador escolheu {num_compt}')                        #txt
    rslt = n + num_compt
    sleep(0.9)
    if i_p == 'P':  #escolha for par
        if rslt % 2 == 0 :
            print (' -PARABENS VC GANHOU-')
            vit += 1
            sleep(0.5)
            continue
        else:
            print(' -VOCE PERDEU-')
            sleep(0.5)
            if vit >= 1:
                print (f'  voce teve um total de {vit} vitoria(s) ')
            else:
                print (' que feio, n ganhou nenhuma vez hahahahhahha')
            sleep(2.8)
            print('\n' * 50)  #separaçao
            vit = 0
            continue
    if i_p == 'I':
        if rslt % 1 == 1:
            print(' -PARABENS VC GANHOU-')
            vit += 1
            sleep(0.5)
            continue
        else:
            print(' -VOCE PERDEU-')
            sleep(0.5)
            if vit >= 1:
                print (f'  voce teve um total de {vit} vitoria(s) ')
            else:
                print (' que feio, n ganhou nenhuma vez hahahahhahha')
            sleep(2.8)
            print('\n' * 50)  # separaçao
            vit = 0
            continue


    #FAZER UM JOGO DE IPAR OU PAR, Q CONTA A QUANTIDADE DE VITORIAS