print ("""====================================\n  OS 10 PRIMEIROS TERMOS E UMA P.A \n====================================""")
p1 = int(input('- Primeiro termo: '))
rz = int(input('- Razao: '))
d10 = p1 + (11 - 1) * rz
for pa in range(p1, d10, rz):
    print(f'{pa}', end=' → ')
print('acabou')
