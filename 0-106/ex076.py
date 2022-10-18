mercado = ('Feijão 1KG', 8.99, 'Arroz 5KG', 14.99,
           'Enlatado de milho 50g', 2.50, 'Chocolate Garoto 70g', 5.68,
           'Molho de tomate 200g', 6.00, 'Tomate verde 1KG', 7.99)
print ('-' * 45, '\n           LISTAGEM DE PRODUTOS\n', '-' * 45)
for pos in range(0, len(mercado)):
    if pos % 2 == 0:
        print(f'{mercado[pos]:.<30}', end=' ')
    else:
        print(f'R${mercado[pos]:.2f}')