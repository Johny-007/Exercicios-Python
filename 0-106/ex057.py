sex = str(input('- Digite seu sexo [M/F]: ')).strip().lower()[0]
while sex not in 'MmFf':
    sex = str(input('- Sexo invalído! Digite seu sexo novamente [M/F]: '))