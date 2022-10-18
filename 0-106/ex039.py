from math import fabs
print (""" \nola, deseja ver seu formulário de \033[97malistamento?\033[m
           ok! vamos \033[4mverificar\033[m""")
y = int(input("  -Em qual \033[4;35mano\033[m vc \033[4;35mnasceu:\033[m "))
#se haver alistamento
if 2022 - y < 18:
    bo = 2022 - 18 - y
    box = fabs(bo)
    print(f""" \n \033[7mVoce ainda ira se alistar\033[m
  Faltam \033[1;31;40m{box}\033[m ano(s) para vc se alistar""")
elif 2022 - y > 18:
    print(f""" \n \033[7mVoce ja deveria ter se alistado\033[m
     Fazem \033[1;31;40m{2022 - 18 - y}\033[m ano(S) q vc deveria teria ter se alistado""")
else:
    print(" \n Está na hora exata, va agora se alistas!")
print("    \n  \033[7mFIM\033[m")