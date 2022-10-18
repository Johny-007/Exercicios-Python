print (""" \n Somos da coorporação nacional de natação
  Deseja saber sua classificação 
      vamos lá \n""")
n = str(input("  -Qual seu nome: ")).strip()
xy = int(input("  -Qual ano vc nasceu: "))
y = 2022 - xy
#aaaaaaa
if y <= 9:
    print (f""" Querido(A) {n} vc é um(A) pequenino(A) gafanhoto(A)
          categoria: \033[4mMIRIM\033[m""")
elif y > 9 and y <= 14:
    print(f""" Querido(A) {n} vc é um(A) pequeno(A) gafanhoto(A)
          categoria: \033[4mINFANTIL\033[m""")
elif y > 14 and y <= 19:
    print(f""" Querido(A) {n} vc é um(A) pequeno(A) gafanhoto(A)
          categoria: \033[4mJUNÍOR\033[m""")
elif y == 20:
    print(f""" Querido(A) {n} vc é um(A) pequeno(A) gafanhoto(A)
          categoria: \033[4mSENÍOR\033[m""")
else:
    print(f""" Querido(A) {n} vc é um(A) pequeno(A) gafanhoto(A)
          categoria: \033[4mMASTER\033[m""")