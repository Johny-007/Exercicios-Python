while True:
    num = int(input('\n-  DIgite um valor para a tab: '))
    if num < 0:
        break
    for c in range(1,11):
        print (f' {num} x {c} = {num * c}')
print (' tabuada finalizada')