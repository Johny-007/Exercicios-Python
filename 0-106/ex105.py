def notas(* notas, situ=False):
    """
    função criada para dar notas a um aluno
    :param notas: recebe varias notas de um aluno
    :param situ: diz a situação academita do aluno
    :return: retorna uma lista com alguns dados
    """
    maior = menor = soma = média = 0
    for c in range(0, len(notas)):
        if c == 0:
            maior = menor = notas[c]
        if notas[c] > maior:
            maior = notas[c]
        if notas[c] < menor:
            menor = notas[c]
        soma += notas[c]
    total = int(len(notas))
    média = soma / total
    dic = {"total":len(notas), "maior nota": maior, "menor nota": menor, "média": média}
    if situ == True:
        if int(média) <= 5:
            dic["situ"] = "VERMELHO"
        elif 6 <= int(média) <8:
            dic["situ"] = "AZUL"
        else:
            dic["situ"] = "VERDE"
    return dic

aluno01 = notas(10, 9, 7.9, 7.2)
aluno02 = notas(5, 5, 5)
aluno03 = notas(7, 0, 10, situ=True)


print(f"{aluno01}\n{aluno02}\n{aluno03}")
help(notas)