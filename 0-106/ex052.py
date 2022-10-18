nm_p = int(input('- Digite um nmr: '))
n1 = 0
for n00 in range(1, nm_p + 1):
     if nm_p % n00 == 0:
         print('\033[31m', end=' ')
         n1 += 1
     else:
         print('\033[33m', end=' ')
     print(f'{n00}', end=' ')
print(f'\n\033[m O número {nm_p} é divísivel {n1} vezes')
if n1 == 2:
    print (" Por tanto é PRIMO")
else:
    print (" Por tanto nao é PRIMO")