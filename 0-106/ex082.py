listanums = []
list_par = []
list_ipar = []
decisao = ''
while True:
    num = int(input('- Digite um nmr: '))
    listanums.append(num)
    if (num % 2) == 0:
        list_par.append(num)
    if (num % 2) != 0:
        list_ipar.append(num)
    decisao = 'xx'
    while decisao not in 'SN':
        decisao = str(input('-Quer continuar[S/N]: ')).upper()
    if decisao == 'N':
        break
print (f'''-Lista total {listanums}
-Lista ímpar {list_ipar}
-Lista par {list_par}''')
