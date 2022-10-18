brasileirao_list = ('Palmeiras', 'Atlético-MG', 'Corinthinas', 'Curitiba', 'São Paulo', 'Atlético-PR', 'Botafogo', 'Flamengo', 'Santos', 'América-MG')
linha = '==-' * 20
print (linha, f'\n- Os 5 primeiros times são: {brasileirao_list [:5]}') #MOSTRAR OS 5 PRIMEIROS
print (linha, f'\n- Os 4 ultimos times são: {brasileirao_list[6:]}') #MOSTRAR OS 4 ultimos
print (linha, f'\n- Em ordem alfabética: {sorted(brasileirao_list)}') #EM ORDEM
print (linha, '\n- A chapecoense n está na lista')