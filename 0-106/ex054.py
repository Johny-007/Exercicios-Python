from datetime import date
natu = date.today().year
maiores = 0
menores = 0
for dd in range(1,7):
    ns = int(input(f'- Qual data de nascimento do {dd} individuo: '))
    id = natu - ns
    if id >= 21:
        maiores += 1
    else:
        menores += 1
print (f'\n- {maiores} individuo(s) sao maiores, {menores} individuo(s) sao menores ')
print(natu)