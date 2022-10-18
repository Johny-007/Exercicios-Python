separador = '=-'*35
termo = int(input('- Quants termos da sequencia de fibonacci vc deseja: ',))
print (separador)
recnt = anterior = contador = fibo= 0
while contador < termo:
    if contador == 0:
        print (' 1 => ', end=' ')
        anterior = 1
        contador += 1
        continue
    if contador == 1:
        print(' 1 => ', end=' ')
        recnt = 1
        contador += 1
        continue
    if contador == 2: #3IRO LAÇO
        fibo = anterior + recnt
        print(f' {fibo} =>', end=' ')
        contador += 1
        continue
    anterior = recnt
    recnt = fibo
    fibo = anterior + recnt
    print(f' {fibo} =>', end=' ')
    contador += 1
print ('       FIMM')
