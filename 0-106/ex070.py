total_valor = prodt_1k = menor_valor = cont = 0
prodt_barat = ''
linha = '==-=-==' * 11
print(linha, '\n             \033[1;31;07m -MERCADAO MAGALU- \033[m')
while True:
    print(linha)
    cont += 1
    produto = str(input('- Qual o produto: ')).strip()
    valor = float(input('- Qual o valor: \033[32mR$\033[m'))

    total_valor += valor
    if valor > 1000:
        prodt_1k += 1
    if cont == 1:
        menor_valor = valor
        prodt_barat = produto
    if valor < menor_valor:
        prodt_barat = produto
    continuar = 'xx'
    while continuar not in 'SN':
        continuar = str(input('- quer continuar S/N: ')).upper().strip()
    if continuar == 'N':
        break
#FORA DO LAÇO
print(f'''\n-Total gasto: {total_valor} R$-Total de produtos acima de 1K: {prodt_1k}
-O produto mais barato: {prodt_barat}''')