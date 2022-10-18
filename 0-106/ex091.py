from random import randint

jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1,6)}
for k, v in jogadores.items():
    print(f'--O {k} tirou {v} no dado')
print ('=<>=<>=<>=<> WINERS <>=<>=<>=<>=')
for i in sorted(jogadores, key = jogadores.get, reverse=True):
    print(i, jogadores[i])

