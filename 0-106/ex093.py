jogador = dict()
jogador['nome'] = str(input('-Nome do jogador: '))
gols = []
total_gols = 0

tot_partidas = int(input(f'-Quantas partidas {jogador["nome"]} jogou: '))
for c in range(0, tot_partidas):
    gols.append(int(input(f'-Quanto gols ele fez na {c+1}° partida: ')))
    total_gols += gols[c]

jogador['gols'] = gols[:]
jogador['total_Gols'] = total_gols
print('=<>='*22, f'\n DADOS D0 {jogador["nome"]} >->-> {jogador}\n', '=<>='*22)

for k, v in jogador.items():
    print(f'{k}: {v}')
print('=<>='*22)

for c in range(0, tot_partidas):
    print(f'   -na {c+1}° partida {jogador["nome"]} fez {gols[c]} gols')

print('=<>='*22, '\n  -FIM-')
