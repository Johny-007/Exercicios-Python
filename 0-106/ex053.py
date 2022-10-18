frs = str(input("- Digite uma frase: ")).strip().lower().replace(' ', '')
if frs[::-1] == frs:
    print ('- A frase é um polimedro')
else:
    print('- Essa frase não é um polimedro!!')