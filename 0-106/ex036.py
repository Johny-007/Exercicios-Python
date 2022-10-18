print ("""  \n  \033[7mola pequeno e docio humano\033[m
  \033[7mquer fazer um emprestimo? \033[m
  \033[7mta afim da casa propria?  \033[m""")
casa = int(input("  -qual o valor da casa q deseja comprar: "))
sal = int(input("  -qual seu salario atual: "))
ano = int(input("  -em quantos anos deseja pagar: "))*12

#valor se senaose senao
if casa / ano - sal <= (sal**0.30):
    print (f""" muito bem!! seu emprestimo foi aprovado
     o valor de cada parcela sera RS {casa / ano:.2f}""")
else:
    print (""" infelizmente seu emprestimo n foi aprovado
          pedimos dsclps""")
print ("     agradecemos")
