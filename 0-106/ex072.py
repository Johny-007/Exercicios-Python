num = int(input('- Digite um nmr entre 0 e 20: '))
while num > 20 or num < 0:
    num = int(input('- Tente novamente: '))
numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', '0nze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print (f' voce escolheu {numeros[num]}')