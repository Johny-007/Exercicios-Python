def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
            break
        except:
            print("\033[31mERRO!!! PRFV DIGITE UM INT!!!\033[m")
    return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
            break
        except:
            print("\033[31mERRO!!! PRFV DIGITE UM FLOAT!!!\033[m")
    return num


n = leiaInt("Digite um nmr INT: ")
print(f"  -Voce digitou {n}\n\n")

n = leiaFloat("Digite um nmr FLOAT: ")
print(f"  -Voce digitou {n}\n\n")
