from time import sleep

Cores = {"branco": "\033[107m", "ciano": "\033[46m", "roxo": "\033[45m", "nulo": "\033[m", "vermelho": "\033[41m"}
comando = ''

def ajudaPy(cmnd):
    print(Cores["vermelho"])
    print(help(cmnd))

def titulo(msg, cor):
    print(Cores[cor], "="*len(msg))
    print(msg)
    print("=" * len(msg))
    print(Cores["nulo"])



while True:
    sleep(0.85)
    titulo(f"{'SISTEMA DE AJUDA - JOHNY':^100}", "branco")
    comando = str(input("--Função ou Biblíoteca --> "))
    if comando.upper() == "FIM":
        titulo(f"{'FIM':^100}", 'roxo')
        break

    else:
        titulo(f"{'ANALISANDO ... EM BUSCA ...':^100}", "ciano")
        sleep(0.85)
        ajudaPy(comando)