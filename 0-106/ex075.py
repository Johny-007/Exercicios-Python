n1 = n2 = n3 = n4 = 0
n1 = int(input('-Digite um nmr inteiro: '))
n2 = int(input('-Digite outro nmr inteiro: '))
n3 = int(input('-Digite outro nmr inteiro: '))
n4 = int(input('-Digite outro nmr inteiro: '))
numeros = ( n1, n2, n3, n4)
print ('=' * 30 ,f'\n- o numero nove apareceu: {numeros.count(9)} vezes')
if not 3 in numeros:
    print ('- O numero (3) não foi digitado')
else:
    achar_o_3 = numeros.index(3)
    print (f'o numero (3) está na: {achar_o_3 + 1}º posição')
print ('- os numeros pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print (n, end=' ')
