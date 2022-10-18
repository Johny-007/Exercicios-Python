cont = 0
soma = 0
for tres in range(1, 501, 2):
   if tres % 3 == 0:
       soma += tres
       cont += 1
print(f'-  A soma entre os numeros impares multiplos de tres no intervalo de 1 a 500 é {soma}, com um total de {cont} somas.')
