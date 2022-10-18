time = []
jogador = dict()

while True:
    jogador['nome'] = str(input('-Nome do jogador: '))
    gols = []
    total_gols = 0

    tot_partidas = int(input(f'-Quantas partidas {jogador["nome"]} jogou: '))
    jogador['tot_partidas'] = tot_partidas
    for c in range(0, tot_partidas):
        gols.append(int(input(f'-Quanto gols ele fez na {c+1}° partida: ')))
        total_gols += gols[c]

    jogador['gols'] = gols[:]
    jogador['total_Gols'] = total_gols
    time.append(jogador.copy())
    jogador.clear()

    decisao = 'xx'
    while decisao not in 'SN':
        decisao = str(input('-QUER CONTINUAR[S/N]: ')).strip().upper()
    if decisao == 'N':
        break

print(f'\n{"=*="*19}\n{"cod":<4}{"nome":<10}{"gols":>9}{"total":>23}')
for c, j in enumerate(time):
    print(f'{c:<4}{j["nome"]:<10}    {j["gols"]}{j["total_Gols"]:>23}')
print('=*='*19)
while True:
    dados = int(input('\n-Mostrar dados de qual jogador[COD] - (999 / PARA PARAR): '))
    if dados == 999:
        break
    if len(time) < dados or dados < 0:
        print('---por favor digite o cod de um jogador---')
        continue
    if dados < len(time):
        print(f'--Levantamento do jogador: {time[dados]["nome"]}')
        for c in range(0, time[dados]['tot_partidas']):
            print(f'-Na {c+1}° partida fez {time[dados]["gols"][c]} gols')