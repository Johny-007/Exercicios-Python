lista_num = []
for c in range(0, 5):
    num = int(input('- Digite um nmr: '))
    if c == 0 or num > lista_num[-1]:
        lista_num.append(num)
        print ("-O numero foi adicionado ao final da lista-")
    else:
        posição = 0
        while posição < len(lista_num):
            if num <= lista_num[posição]:
                lista_num.insert(posição, num)
                print (f'-O numero foi adcnd na posição {posição}-')
                break
            posição += 1
print(f'\n A lista final foi {lista_num}')