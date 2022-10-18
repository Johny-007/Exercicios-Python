from libJohny import interfaceTXT, dados
from time import sleep
arquivo = open("arquivo.txt", "a+")
arq = "arquivo.txt"
print("--Arquivo criado com sucesoo--")

while True:
    interfaceTXT.menu(["Ver Cadastros", "Cadastrar Pessoa", "Sair do menu"], "MENU", linhaBaixo=True)
    Escolha_User = dados.leiaInt(f'\n{interfaceTXT.cor["verde"]}ESCOLHA A OPÇÃO DESEJADA: \033[m', 'ERRO, POR FAVOR DIGITE UMA OPÇÃO VÁLIDA', True)

    if Escolha_User == 1: #se o usurio escolher--- ver os cadastros
        interfaceTXT.linhaTXT("VER CADASTROS")
        arquivo.seek(0,0)
        dados.mostrarCadastros(arquivo.readlines())

    if Escolha_User == 2: #cadastrar nova pessoa
        interfaceTXT.menu("", "CADASTRAR PESSOA")
        nome = input("\033[1;36m--Nome:\033[m ")
        idade = dados.leiaInt("\033[1;36m--Idade:\033[m ", "\033[1;31mDIGITE A IDADE EM NÚMERO INTEIRO!!!\033[m")
        dados.adicionarPessoa(arq, nome, idade)

    if Escolha_User == 3:
        print("\033[1;31m   --FECHANDO PROGRAMA, FIM--")
        sleep(0.83)
        arquivo.close()
        break

