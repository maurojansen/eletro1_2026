print("Identificação de número par ou ímpar")
num=int(input("Digite um número: "))
resto=num%2      # o símbolo % é o operador de resto da divisão
if resto==0:
  print("O número é par!")
else:
  print("O número é ímpar!")
