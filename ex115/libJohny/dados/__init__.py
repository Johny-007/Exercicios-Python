from time import sleep


def leiaInt(msg, msgERRO, do1ao3=False):
    while True:
        try:
            num = int(input(msg))
            if do1ao3:
                if 0 < num < 4:
                    sleep(0.68)
                    break
                else:
                    print(f"\033[31m{msgERRO}\033[m")
            else:
                break
        except KeyboardInterrupt:
            print("O usuario preferiu interromper o laço")
            break
        except:
            print(f"\033[31m{msgERRO}\033[m")
            continue
        sleep(0.48)
    return num


def mostrarCadastros(arquivoTXT):
    c = 1
    print(f"\033[1;35mNº - Nome{'Idade':>30}\033[m")
    for linha in arquivoTXT:
        dado = linha.split(";")
        dado[1] = dado[1].replace("\n", "")
        print(f"{c:<0}º - {dado[0]:<6}{dado[1]:>25}")
        c += 1
        sleep(0.72)


def adicionarPessoa(arquivo, nome, idade):
    try:
        a = open(arquivo, 'at')
    except:
        print("ERRO")
    else:
        a.write(f"{nome};{idade}\n")
        print("\033[1;35m --Pessoa cadastrada com sucess--\033[m")
    finally:
        a.close()
