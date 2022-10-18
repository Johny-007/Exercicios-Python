lista_matrix = [[], [], []]
somaPares = soma3coluna = maiorNUM2linha = 0
for c in range(0, 3):
    num = int(input(f'-digite um nmr [0, {c}]: '))
    lista_matrix[0].append(num)
    if num % 2 == 0:
        somaPares += num
    if c == 2:
        soma3coluna += num
for c in range(0, 3):
    num = int(input(f'-digite um nmr [1, {c}]: '))
    lista_matrix[1].append(num)
    if num % 2 == 0:
        somaPares += num
    if c == 2:
        soma3coluna += num
    if c == 0:
        maiorNUM2linha = num
    elif num > maiorNUM2linha:
        maiorNUM2linha = num
for c in range(0, 3):
    num = int(input(f'-digite um nmr [2, {c}]: '))
    lista_matrix[2].append(num)
    if num % 2 == 0:
        somaPares += num
    if c == 2:
        soma3coluna += num
print('==-'*30)
print(f'''[ {lista_matrix[0][0]} ]    [ {lista_matrix[0][1]} ]    [ {lista_matrix[0][2]} ]
[ {lista_matrix[1][0]} ]    [ {lista_matrix[1][1]} ]    [ {lista_matrix[1][2]} ]
[ {lista_matrix[2][0]} ]    [ {lista_matrix[2][1]} ]    [ {lista_matrix[2][2]} ]''')
print('==-'*30)
print(f'- A somas dos pares é: {somaPares}\n- A soma de tds os nmrs da 3a coluna é: {soma3coluna}\n- O maior nmr da 2a linha é: {maiorNUM2linha}')

