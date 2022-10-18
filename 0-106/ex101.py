from datetime import date
#ano atual atualizado
data = date.today().year

def voto(anoNascimento):
    idadePessoa = data - anoNascimento
    if idadePessoa < 16:
        print(f"IDADE  {idadePessoa}, NAO VOTA")
    elif 16 <= idadePessoa <=17 or idadePessoa >= 65:
        print(f"IDADE {idadePessoa}, VOTO OPCIONAL")
    else:
        print(f'IDADE {idadePessoa}, VOTO OBRIGATORIO')

voto(1957)
voto(2000)
voto(2020)
voto(2006)