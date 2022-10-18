expressao = str(input('-Digite uma expresão: '))
pilha = []
for símb in expressao:
 if símb == '(':
  pilha.append('(')
 elif símb == ')':
  if len(pilha) > 0:
   pilha.pop()
  else:
   pilha.append(')')
   break
if len(pilha) == 0:
 print("Sua expressao é válida!!")
else:
 print('Sua expressao nao é valida')


