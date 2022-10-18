import datetime

data_atual = datetime.datetime.now()
ano_atual =  data_atual.year

trabalhador = dict()
trabalhador['nome'] = str(input('-Nome: '))
trabalhador['ano_nas'] = int(input('-Ano de nascimento: '))
trabalhador['cart_trab'] = int(input('-Carteira de trabalho(0 = nao tem): '))
trabalhador['idade'] = ano_atual - trabalhador['ano_nas']
if trabalhador['cart_trab'] >= 1:
    trabalhador['ano_contract'] = int(input('-Qual ano foi contratado: '))
    trabalhador['salario'] = int(input('-Valor do sálario: '))
    trabalhador['aposento'] = (trabalhador['ano_contract'] + 35) - ano_atual
    trabalha = True
else:
    trabalhador['cart_trab'] = str('Não tem')
    trabalha = False
print('=<>='*15)
print(f'\n Nome: {trabalhador["nome"]}\n Idade: {trabalhador["idade"]}\n CTPS: {trabalhador["cart_trab"]}')
if trabalha == True:
    print(f' Ano de contrataçao: {trabalhador["ano_contract"]}\n Faltam {trabalhador["aposento"]} anos para se aposentar\n Salárion: {trabalhador["salario"]}')
print('=<>='*5, 'FIM', '=<>='*5)

