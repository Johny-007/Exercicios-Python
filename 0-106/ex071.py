linha = '==-' * 29   #inicio do programa
print(linha,'\n CAIXA ELETRONICO -- BANCO ELFO \n', linha)
saque = int(input('  -Quanto voce deseja sacar: R$'))
cédula = 50     # variaveis de 50
total_céd50 = 0
while True:
    if saque >= cédula:
        saque -= cédula
        total_céd50 += 1
    else:
        print(f' -O total de células de {cédula}r$ será {total_céd50}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        total_céd50 = 0
        if saque == 0:
            break


