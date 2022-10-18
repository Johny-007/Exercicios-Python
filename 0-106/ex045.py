import random

print ('Bem vindo aos jogos!! jogue pela vida!!')
escolha = str(input(''' PEDRA, PAPEL ou TESOURA?  
 Escolha -  ''')).strip().upper()


  #ALEATORIO
  lista = ['papel','tesoura','pedra']
  def alt(lista):
      return random.choice(lista)

print (f'  Voce escolheu {escolha}')
print ('   a maquina escolheu:', alt(lista))
