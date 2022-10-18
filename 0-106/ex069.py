pess_mais18y = homns = mulhe_menos18y = 0
linha = '==-' * 27
print(linha, '\n    \033[1;31;07m- Cadastro Geral -\033[m \n ')
while True:
    valid = 0
    print(linha)
    idade = int(input('-Qual a idade: '))
    sexo = str(input('-Qual o sexo [F/M]: ')).strip().upper()
    if sexo == 'F': valid = 1                                             #validaçao de ímpar ou par
    if sexo == 'M': valid = 1                                             #validaçao de ímpar ou par
    if valid != 1:
        print ('  -VOCE DIGITOU O SEXO ERRADO, TENTE NOVAMENTE-')
        continue

    if idade >= 18:                     #pessoas com + de 18y
        pess_mais18y += 1
    if sexo == 'M':                     #quantidade d homens
        homns += 1
    if sexo == 'F' and idade < 18:     #femeas com + d 18y
        mulhe_menos18y += 1


    continuar = str(input('\n  -Deseja contimuar [S/N]: ')).strip().upper()
    print(linha)
    if continuar == 'N':
        break
# FIM DO WHILE
print (f'''{linha} 
-Pessoas com mais de 18y: {pess_mais18y}
-Total de homens: {homns}
-Total de mulheres com menos de 18y: {mulhe_menos18y}''')


