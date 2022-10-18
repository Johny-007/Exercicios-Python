valores = []
while True:
    num = int(input('- Digite um número inteiro: '))
    if num in valores:
        print (f'--O número {num} já está na lista, não irei adc...--')
    else:
        valores.append(num)
        print('--Irei adc o valor na lista...--')
    pergunta = str(input('-Quer continuar [S/N]: ')).strip().upper()
    #while pergunta != 'sSNn':
     #   pergunta = str(input('-Quer continuar [S/N]: ')).strip().upper()
    if pergunta == 'N':
        break
valores.sort()
print (f'''\n         -Os valores digitados foram-
{valores}''')