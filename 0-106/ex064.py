num = soma = cont = 0
while num != 999:
    num = int(input('- digite um nmr[999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print (f'\n  -A soma de tds os nmr foi {soma}, o nmr de adições foi {cont}')