from time import sleep


def linhaTXT(msg):
    print(f"{cor['amarelo']}")
    print("<=>"*15)
    print(f"{msg:^45}")
    print("<=>"*15, f"{cor['reset']}")


def linha():
    return print("\033[1;33m<=>\033[m" * 15)

def menu(lista, nomeMenu, linhaBaixo=False):
    linhaTXT(f"{nomeMenu}")
    c = 1
    for item in lista:
        print(f"{cor['verde']}{c} - {item}{cor['reset']}")
        c += 1
    if linhaBaixo:
        linha()




cor = {
    'vermelho' : '\033[1;31m',
    'verde': '\033[1;32m',
    'azul': '\033[1;34m',
    'ciano': '\033[1;36m',
    'magenta': '\033[1;35m',
    'amarelo': '\033[1;33m',
    'preto': '\033[1;30m',
    'branco': '\033[1;37m',
    'reset': '\033[1;0;0m',
    'reverso': '\033[1;2m',
    'bgpreto': '\033[1;40m',
    'bgvermelho': '\033[1;41m',
    'bgverde': '\033[1;42m',
    'bgamarelo': '\033[1;43m',
    'bgazul': '\033[1;44m',
    'bgmagenta': '\033[1;45m',
    'bgciano': '\033[1;46m',
    'bgbranco': '\033[1;47m'}