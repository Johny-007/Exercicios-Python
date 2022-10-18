aluno = {}
aluno['nome'] = str(input('--Nome do aluno: '))
aluno['media'] = float(input('--Média do aluno: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif aluno['media'] < 7 and aluno['media'] >= 5:
    aluno['situacao'] = 'RECUPERAÇAO'
elif aluno['media'] < 5:
    aluno['situacao'] = 'REPROVADO'
print('=<>='*15, f'\n  Nome: {aluno["nome"]}\n  Média: {aluno["media"]}\n  A situação é de: {aluno["situacao"]}')
