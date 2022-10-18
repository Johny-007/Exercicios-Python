print ("""\n \n0la, somos o painel alfabetico elfo
   vamos consultar seu nome 
 -apenas informacoes basicas- \n""")
no = str(input("- digite seu nome completo: "))
no0 = no.strip()
esp = no0.count(' ')
no1 = len(no)
nom = no1-esp
cort = no.split()
print (f"""-----------------------------------------
- seu nome minusculo: {no.upper()}
- seu nome maiuscylo: {no.lower()}
- nmr de caracteres: {nom}
- primeiro nome: {cort[0]}
-----------------------------------------""")