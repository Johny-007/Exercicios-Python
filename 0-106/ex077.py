palavras = ('Palavra', 'Arroz', 'Caderno', 'Notebook', 'Parede')
for item in palavras:
    print('\n')
    print (f'-A palavra  (- {item} -)  tem essas vogais: ', end='')
    for vogal in item:
        if vogal.lower() in 'aeiou':
            print (f'{vogal}', end=' ')

