from random import randint
from time import sleep

numeros = []
def sorteia(lista):
    for c in range(0,5):
        lista.append(randint(0, 9))
    print(f"-Sorteando os números...")
    sleep(0.7)
    print(f"-OS numeros foram: {lista}")
def somaPar(lista):
    somaPARES = 0
    for num in lista:
        if num % 2 == 0:
            somaPARES += num
    print(f"-A soma dos números pares é: {somaPARES}")


sorteia(numeros)
somaPar(numeros)