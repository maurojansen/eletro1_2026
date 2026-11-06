print("Média de 2 notas")
nota1=float(input("Digite a 1a nota: "))
nota2=float(input("Digite a 2a nota: "))
media=(nota1+nota2)/2
print("A média é: ",media)
if media>=7:
  print("Aprovado(a)")
  print("PARABÉNS!")
if media<7:
  print("Recuperação")
