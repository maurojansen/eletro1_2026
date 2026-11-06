print("Blitz do DETRAN")
velocidade=float(input("Qual a velocidade do veículo? "))
if velocidade>80:
  print("Você foi multado!")
  multa=(velocidade-80)*5
  print("Valor da multa: ",multa)
else:
  print("Você está dentro do limite de velocidade!")
  print("Pode seguir!")
