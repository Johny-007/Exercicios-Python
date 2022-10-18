def maior(* num):
    cont = maior = 0
    print("\n-Os numeros foram: ", end="")
    for valor in num:
        print(f"{valor}", end=" ")
        if valor > maior:
            maior = valor
        cont += 1
    print(f"\n-Com um total de {cont} mumeros, o maior é: {maior}")


maior(7, 8, 9)
maior(0)
maior(2, 2, 9)
maior()