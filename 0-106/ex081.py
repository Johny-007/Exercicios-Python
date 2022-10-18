lista_nums = []
esta_ou_nao = 'Não está' #verifica c o 5 ta ou n
while True:
    num = int(input('-Digite um nmr: '))
    if num == 5:
        esta_ou_nao = 'Está'   # verificador
    lista_nums.append(num)
    decisao = 'xx'
    while decisao not in 'SN':
        decisao = str(input('-Quer continuar[S/N]: ')).upper()
    if decisao == 'N':
        break
lista_nums.sort(reverse=True)
print (f'''Foram digitados {len(lista_nums)} numero(s)
A lista decrescente: {lista_nums}
O numero 5 {esta_ou_nao} na lista''')

