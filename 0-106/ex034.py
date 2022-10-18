print ("""     seja bem vindo ao menu gorvenamental
  com essa nova reforma todos os brasileiros foram benficiados
               veja agora seu beneficio aumento!\n""")
emp = str(input("  -Qual empresa vc trabalha? ")).title()
sal = int(input("  -Qual seu salario atual nessa empesa? "))
#maior que 1250
if sal>=1250:
    sal1 = sal+(sal*0.10)
    print (f"""\n calculando...
 a empresa \033[34m{emp}\033[m deve reajustar seu salario para R$ \033[4m{sal1:.2f}\033[m""")
#menor que 1250
else:
    sal2 = sal+(sal*0.15)
    print (f"""\n calculando...
 a empresa \033[34m{emp}\033[m deve reajustar seu salario para R$ \033[4m{sal2:.2f}\033[m""")
print ("\n \n para mais informacoes acesse gov.elfo.com")
