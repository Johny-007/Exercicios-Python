cont = total = maior = menor = 0
while True:
    num = int(input('- Digite um valor: '))
    conti = str(input('--Quer continuar?[S/N] ')).strip().upper()
    cont += 1
    menor = num
    if conti == 'N':
        break
    if num > maior: #O MAIOR VALOR
        maior = num

    if num < menor: #O MENOR VALOR
        menor = num
    total += num
print (f'''- A média dos valores: {total / cont}
- O maior valor foi: {maior}
- O menor valor foi: {menor}''')