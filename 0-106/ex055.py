maiorp = 0
menorp = 0
for pes in range(1,5):
    pesos = float(input(f'- qual o peso da {pes} pessoa: '))
    if pes == 1:
        maiorp = pesos
        menorp = pesos
    else:
        if pesos > maiorp:
            maiorp = pesos
        if pesos < menorp:
            menorp = pesos
print (f'- O maior peso é {maiorp}KG\n- O menor peso é {menorp}KG')