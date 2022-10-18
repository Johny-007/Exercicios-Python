pessoas = []
dados_P = []
P_maiPsada = P_maiLeve = MaiPeso = total_P = 0
MenosPeso = 999999999
while True:
    total_P += 1
    dados_P.append(str(input('Nome: ')))
    dados_P.append(float(input('Peso: ')))
    pessoas.append(dados_P[:])
    if dados_P[1] > MaiPeso:
        P_maiPsada = dados_P[0]
        MaiPeso = dados_P[1]
    if dados_P[1] <= MenosPeso:
        P_maiLeve = dados_P[0]
        MenosPeso = dados_P[1]
    dados_P.clear()
    decisao = 'xx'
    while decisao not in 'NS':
        decisao = str(input('-   --Quer continuar[S/N]: ')).upper().strip()
    if decisao == 'N':
        break
print (f"""- O total de pessoas cadastradas foram {total_P}
- A pessoa mais pesada é {P_maiPsada} com {MaiPeso}KG
- A pessoa mais leve é {P_maiLeve} com {MenosPeso}KG""")

