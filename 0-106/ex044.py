print("""\n Ola, seja bem vindo á oficina elfica
 qual serviço deseja? \n""")
p = 600
pi = 950
v = 1200
serv = int(input(""" (  1  )  polimento 600R$
 (  2  )  pintura 950R$ 
 (  3  )  vitrificação 1200R$
    
    digite o nmr escolhido -  """))
#POLIMENTO
if serv == 1:
    form = int(input("""\n  -Qual a forma de pagamento?
    ( 1 ) À vista, dinheiro
    ( 2 ) À vista, cartao
    ( 3 ) No cartao, 2X
    ( 4 ) No cartao, 3X ou mais
    
    digite o nmr escolhido - """))
    if form == 1:
        print(f"\n O \033[4;35mpolimento ficara {p - (p ** 0.50):.2f}R$\033[m graças ao desconto da compra avista  em dinheiro")
    elif form == 2:
        print(f"\n o \033[4;35mpolimento ficara {p - (p ** 0.25):.2f}R$\033[m graças ao desconto da compra avista no cartao ")
    elif form == 3:
        print(f"\n o \033[4;35mpolimento ficara 600R$\033[m")
    elif form == 4:
        print(f"\n o \033[4;35mpolimento ficara {p + 20 + (p ** 0.20):.2f}R$\033[m graças ao juros da maquininha")
    else:
        print(" \n \n \n ALGO DEU ERRADO, DIGITE APENAS O NUMERO CORRESPONDENDE AO SEU DESEJO!!!!!! ")
elif serv == 2:
    form = int(input("""\n  -Qual a forma de pagamento?
        ( 1 ) À vista, dinheiro
        ( 2 ) À vista, cartao
        ( 3 ) No cartao, 2X
        ( 4 ) No cartao, 3X ou mais

        digite o nmr escolhido - """))
    if form == 1:
        print(f"\n a \033[4;35mpintura ficara {pi - (pi ** 0.50):.2f}R$\033[m graças ao desconto da compra avista  em dinheiro")
    elif form == 2:
        print(f"\n a \033[4;35mpintura ficara {pi - (pi ** 0.25):.2f}R$\033[m graças ao desconto da compra avista no cartao ")
    elif form == 3:
        print(f"\n a \033[4;35mpintura ficara 950R$\033[m")
    elif form == 4:
        print (f"\n a \033[4;35mpintura ficara {pi + 20 + (pi ** 0.20):.2f}R$\033[m graças aos juros da maquinimha ")
    else:
        print(" \n \n \n ALGO DEU ERRADO, DIGITE APENAS O NUMERO CORRESPONDENDE AO SEU DESEJO!!!!!! ")
        #forma 3 de pagamento
elif serv == 3:
    form = int(input("""\n  -Qual a forma de pagamento?
            ( 1 ) À vista, dinheiro
            ( 2 ) À vista, cartao
            ( 3 ) No cartao, 2X
            ( 4 ) No cartao, 3X ou mais

            digite o nmr escolhido - """))
    if form == 1:
        print(
            f"\n a \033[4;35mvitrificaçao ficara {v - (v ** 0.50):.2f}R$\033[m graças ao desconto da compra avista  em dinheiro")
    elif form == 2:
        print(
            f"\n a \033[4;35mvitrificaçao ficara {v - (v ** 0.25):.2f}R$\033[m graças ao desconto da compra avista no cartao ")
    elif form == 3:
        print(f"\n a \033[4;35mvitrificaçao ficara 1200$\033[m")
    elif form == 4:
        print(f"\n a \033[4;35mvitrificaçao ficara {v + 20 + (v ** 0.20):.2f}R$\033[m graças aos juros da maquinimha ")
    else:
        print(" \n \n \n ALGO DEU ERRADO, DIGITE APENAS O NUMERO CORRESPONDENDE AO SEU DESEJO!!!!!! ")
else:
    print(" \n \n \n ALGO DEU ERRADO, DIGITE APENAS O NUMERO CORRESPONDENDE AO SEU DESEJO!!!!!! ")
str = int(input("""  \n       -----ELFO-----


     PARA SAIR APERTE QUCICK
     PARA RETORNAR AO MENU DIGITE '007'
     LAVINYA AMOR HIHI KKKLKLKLKKK
     
     digite o nmr escolhido - """))
#SEPRAAAAAAAAAAAAAA
#AUYGDSJBSDHS
#CMVKKFFFFFFFF
if str == 007:
    serv = int(input(""" (  1  )  polimento 600R$
     (  2  )  pintura 950R$ 
     (  3  )  vitrificação 1200R$

        digite o nmr escolhido -  """))
    # POLIMENTO
    if serv == 1:
        form = int(input("""\n  -Qual a forma de pagamento?
        ( 1 ) À vista, dinheiro
        ( 2 ) À vista, cartao
        ( 3 ) No cartao, 2X
        ( 4 ) No cartao, 3X ou mais

        digite o nmr escolhido - """))
        if form == 1:
            print(
                f"\n O \033[4;35mpolimento ficara {p - (p ** 0.50):.2f}R$\033[m graças ao desconto da compra avista  em dinheiro")
        elif form == 2:
            print(
                f"\n o \033[4;35mpolimento ficara {p - (p ** 0.25):.2f}R$\033[m graças ao desconto da compra avista no cartao ")
        elif form == 3:
            print(f"\n o \033[4;35mpolimento ficara 600R$\033[m")
        elif form == 4:
            print(f"\n o \033[4;35mpolimento ficara {p + 20 + (p ** 0.20):.2f}R$\033[m graças ao juros da maquininha")
        else:
            print(" \n \n \n ALGO DEU ERRADO, DIGITE APENAS O NUMERO CORRESPONDENDE AO SEU DESEJO!!!!!! ")
    elif serv == 2:
        form = int(input("""\n  -Qual a forma de pagamento?
            ( 1 ) À vista, dinheiro
            ( 2 ) À vista, cartao
            ( 3 ) No cartao, 2X
            ( 4 ) No cartao, 3X ou mais

            digite o nmr escolhido - """))
        if form == 1:
            print(
                f"\n a \033[4;35mpintura ficara {pi - (pi ** 0.50):.2f}R$\033[m graças ao desconto da compra avista  em dinheiro")
        elif form == 2:
            print(
                f"\n a \033[4;35mpintura ficara {pi - (pi ** 0.25):.2f}R$\033[m graças ao desconto da compra avista no cartao ")
        elif form == 3:
            print(f"\n a \033[4;35mpintura ficara 950R$\033[m")
        elif form == 4:
            print(f"\n a \033[4;35mpintura ficara {pi + 20 + (pi ** 0.20):.2f}R$\033[m graças aos juros da maquinimha ")
        else:
            print(" \n \n \n ALGO DEU ERRADO, DIGITE APENAS O NUMERO CORRESPONDENDE AO SEU DESEJO!!!!!! ")
            # forma 3 de pagamento3
    elif serv == 3:
        form = int(input("""\n  -Qual a forma de pagamento?
                ( 1 ) À vista, dinheiro
                ( 2 ) À vista, cartao
                ( 3 ) No cartao, 2X
                ( 4 ) No cartao, 3X ou mais

                digite o nmr escolhido - """))
        if form == 1:
            print(
                f"\n a \033[4;35mvitrificaçao ficara {v - (v ** 0.50):.2f}R$\033[m graças ao desconto da compra avista  em dinheiro")
        elif form == 2:
            print(
                f"\n a \033[4;35mvitrificaçao ficara {v - (v ** 0.25):.2f}R$\033[m graças ao desconto da compra avista no cartao ")
        elif form == 3:
            print(f"\n a \033[4;35mvitrificaçao ficara 1200$\033[m")
        elif form == 4:
            print(
                f"\n a \033[4;35mvitrificaçao ficara {v + 20 + (v ** 0.20):.2f}R$\033[m graças aos juros da maquinimha ")
        else:
            print(" \n \n \n ALGO DEU ERRADO, DIGITE APENAS O NUMERO CORRESPONDENDE AO SEU DESEJO!!!!!! ")
    else:
        print(" \n \n \n ALGO DEU ERRADO, DIGITE APENAS O NUMERO CORRESPONDENDE AO SEU DESEJO!!!!!! ")
    str = int(input("""  \n       -----ELFO-----


    PARA SAIR APERTE QUCICK
    PARA RETORNAR AO MENU DIGITE 007
    LAVINYA AMOR HIHI KKKLKLKLKKK"""))







