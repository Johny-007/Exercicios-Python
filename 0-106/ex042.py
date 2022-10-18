print ("""\n  de valor a 3 segmentos e veja se esses segmentos podem formar um triangulo  """)
a = float(input("  -segmento um: "))
b = float(input("  -segmento dois: "))
c = float(input("  -segmento tres: "))
#caso seja triangulo
if a < (b + c) and b < (a + c) and c < (a + b):
    print (' esses segmentos \033[7mPODEM\033[m formar um triangulo')
    if a == b and b == c and c == a:
        print (" esse triangulo é equilatéro")
    elif a == b and b == c or c == a and b == a:
        print(" esse triangulo é isoceles")
    else:
        print(" esse triangulo é escaleno")
else:
    print (' esses segmentos \033[7mNAO PODEM\033[m formar um triangulo')
