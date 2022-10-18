r = True
espacamento = '='*50
num1 = int(input('  -Ola seja bem vindo á calculadora elfica- \n-Digite um numero: '))
num2 = int(input('-Digite outro numero: '))
while r:
    escolha = int(input('   - selecione a opçao desejada -\n (1) somar\n (2) maior\n (3) mutiplicar\n (4) novo nmr\n (5) fechar\n  -qual sua escolha: '))
    '''if escolha != 1 and 2 or 3 and 4 or 5:
        print (' Escolha errada patrao, é pra escolher 1, 2, 3, 4 ou 5\n', espacamento)
        continue'''
    if escolha == 1:
        print (f'- A soma entre {num1} e {num2} é {num1 + num2}\n', espacamento)
        continue
    elif escolha == 2:
        if num1 > num2:
            print(f'- o maior nmr é: {num1}\n', espacamento)
        else:
            print(f'- o maior nmr é: {num2}\n', espacamento)
        continue
    elif escolha == 3:
        print(f'- A mutiplicaçao de {num1} x {num2} é {num1 * num2}\n', espacamento)
        continue
    elif escolha == 4:
        num1 = int(input('- Digite um novo nmr: '))
        num2 = int(input('- Digite um novo nmr: '))
        print(espacamento)
        continue
    elif escolha == 5:
        print ('- Esperamos que tenha tido uma boa experiençia aqui, até mais')
        break
