def area():
    largura = float(input('-Qual a largura desse terreno (m): '))
    cumprimento = float(input('-Qual o cumprimento desse terreno (m): '))
    print(f'A ÁREA É: {largura*cumprimento:.1f}m²')


print('=+='*16, f'\n   Loja de construção\n', '=+='*16)
area()