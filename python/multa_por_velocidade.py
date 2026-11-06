# aula de 06/11/2026
print("Blitz do DETRAN - multa por velocidade")
velocidade=float(input("Qual a velocidade do veículo? "))
if velocidade>80:
  print("Você foi multado!")
  multa=(velocidade-80)*5
  print("Valor da multa: ",multa)
else:
  print("Você está dentro do limite de velocidade!")
  print("Pode seguir!")
