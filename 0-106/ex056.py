idade = 0
id_hm_ve = 0
nm_ve = ''
id_fem = 0
for pess in range (1,5):
    nome = str(input(f'\n- Qual o nome da {pess}º pessoa: '))
    idad = int(input(f'- Qual a idade da {pess}º pessoa: '))
    sex = str(input(f'- Qual o sexo da {pess}º pessoa [M/F]: ')).lower().strip()
    idade += idad
    if pess == 1 and sex == 'm':
        id_hm_ve = idad
        nm_ve = nome
    if sex == 'm' and idad > id_hm_ve:
        id_hm_ve = idad
        nm_ve = nome
    if sex == 'f' and idad < 20:
        id_fem += 1

v_ida = idade / 4
print (f'''\n    ANALISE\n- A idade média é {v_ida} anos \n- O homem mais velho tem {id_hm_ve} anos e se chama {nm_ve} \n- Tem um total de {id_fem} mulheres com menos de 20 anos nesse grupo''')
