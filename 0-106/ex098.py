def contador(inicio, fim, passo):
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(f'{c}', end=' --> ')
        print('\n')
    elif inicio > fim:
        if passo <= 0:
            for c in range(inicio, fim - 1, passo):
                print(f'{c}', end=' --> ')
        else:
            for c in range(inicio, fim - 1, -passo):
                print(f'{c}', end=' --> ')
        print('\n')
def linha():
    print('-~~-'*13)


linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('          -- Sua vez --')
Termo1 = int(input('Digite o primeiro termo: '))
termo2 = int(input('Digite o segundo termo: '))
passo = int(input('Digite o intervalo: '))
contador(Termo1, termo2, passo)

