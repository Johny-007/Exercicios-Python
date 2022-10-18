from time import sleep

alunoS = [[], [], []] #nome \\ nota1 \\ nota2
print ('=='*27, '\n      -Menu de cadastro da escola - 2o Bimestre-')

while True:
    sleep(0.9)
    nome = str(input('-Nome do aluno: ')) #NOME
    alunoS[0].append(nome)

    sleep(0.6)
    nota1 = float(input('-Nota 1: ')) #NOTA 1111
    alunoS[1].append(nota1)

    sleep(0.6)
    nota2 = float(input('-Nota 2: ')) #NOTA 2222
    alunoS[2].append(nota2)

    decisao = 'xx'
    while decisao not in 'NS':
        decisao = str(input('-Quer continuar[S/N]: ')).strip().upper()
    if decisao == 'N':
        print('==' * 27)
        break

print(' '*13, 'BOLETIM GERAL\n')
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8} ')
for c in range(0, len(alunoS[0])):
    sleep(0.8)
    print (f'{c:<4}- {alunoS[0][c]:<10}{(alunoS[1][c] + alunoS[2][c]) / 2:>8.1f}  ')

print('=='*27)
while True:
    mostra_nota = int(input('\n-Mostrar nota de qual aluno(999 interrompe): '))
    if mostra_nota == 999:
        break
    if mostra_nota > len(alunoS[0]):
        print ('--- !! Por favor digite o numero de um aluno !! ---')
        continue

    print (f'--As notas de {alunoS[0][mostra_nota]}: {alunoS[1][mostra_nota]}, {alunoS[2][mostra_nota]}')
    print('==' * 27)
sleep(0.8)
print ('\n... FINALIZANDO ...')
sleep(0.8)
print ('-- VOLTE SEMPRE --')