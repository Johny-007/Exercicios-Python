todos_NUM = [[], []]
for c in range(0, 7):
    num = int(input('-Digite um numero int: '))
    if num % 2 == 0:
        todos_NUM[0].append(num)
    else:
        todos_NUM[1].append(num)
todos_NUM[0].sort()
todos_NUM[1].sort()
print('==-' * 30)
print(f'- Os numeros pares foram: {todos_NUM[0]} \n- Os numeros ímpares foram: {todos_NUM[1]}')
