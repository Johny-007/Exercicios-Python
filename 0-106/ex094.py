mulheres_nomes = []
pessoaSS = []
soma_idades = 0

while True:
    pessoa = dict()
    pessoa['nome'] = str(input('\n-NOME: '))
    pessoa['idade'] = int(input('-IDADE: '))
    soma_idades += pessoa['idade']
    pessoa['sexo'] = str(input('-SEXO[M/F]: ')).strip().upper()

    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('-SEXO[M/F]: ')).strip().upper()
    if pessoa['sexo'] == 'F':
        mulheres_nomes.append(pessoa['nome'])

    pessoaSS.append(pessoa.copy())
    pessoa.clear()

    continuar = str(input('-Quer continuar[S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('-Quer continuar[S/N]: ')).strip().upper()
    if continuar == 'N':
        break

print('=<>='*22, f'\n- total de pessoas cadastradas: {len(pessoaSS)}\n- Média de idade: {soma_idades/len(pessoaSS):.0f}')
print(f'- Mulheres cadastradas: {mulheres_nomes}\n- Pessoas com idade acima da média: ', end=' ')
for p in pessoaSS:
    if p['idade'] > (soma_idades / len(pessoaSS)):
        print(p['nome'])
print('=<>='*22)
