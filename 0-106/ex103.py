def ficha(nome="<desconhecido>", gols=0):
    print(f"--O jogador {nome} fez um total de {gols} gol(S)")

print("<->"*20)
nome = str(input("Nome: ")).strip()
g = str(input("Gols: ")).strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
if nome.strip(" ") == "":
    ficha(gols=g)
else:
    ficha(nome, g)