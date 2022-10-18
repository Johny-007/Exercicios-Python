valores = [ int(input(' Digite um numero: ')), int(input(' Digite um numero: ')),
            int(input(' Digite um numero: ')), int(input(' Digite um numero: '))]
maior = menor = valores[0]
posicao_maior = posicao_menor = 0
for posiçao, valor in enumerate(valores):
    if valor > maior:
        maior = valor
        posicao_maior = posiçao
    if valor < menor:
        menor = valor
        posicao_menor = posiçao
print ('=' * 35, f'''\n -O maior valor foi {maior}, e está na posição: {posicao_maior}
-O menor valor foi {menor}, e está na posição: {posicao_menor}''')