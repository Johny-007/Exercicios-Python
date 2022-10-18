#abc
print(""" \n Deseja qualcular se IMC?
  ok, vamos nessa!\n""")
#imc
alt = float(input("  -Qual sua altura: "))
peso = float(input("  -Qual seu peso: "))
imc = peso / (alt * alt)
#imc ok
if imc < 18.5:
    print("\n Voce está abaixo do peso")
    print(f'seu índice de massa corporal é {imc:.2f}')
elif imc >= 18.5 and imc < 25:
    print("\n Voce está no peso ideal")
    print(f'seu índice de massa corporal é {imc:.1f}')
elif imc >= 25 and imc < 30:
    print("\n Voce está sobrepeso")
    print(f'seu índice de massa corporal é {imc:.1f}')
elif imc >= 30 and imc < 40:
    print("\n Voce está obeso")
    print(f'seu índice de massa corporal é {imc:.1f}')
else:
    print("\n Voce está sobre obsidade mórbida")
    print(f'seu índice de massa corporal é {imc:.1f}')