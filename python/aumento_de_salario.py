# aumento de salário
print("Programa para calcular aumento de salário")
nome=input("Nome do funcionário:")
salario=float(input("Salário atual: "))
anos=int(input("Quantos anos de trabalho: "))

if anos<=3:
  percentual=3
elif anos <= 10:
  percentual=12.5
else: 
  percentual=20

salario_novo=salario+salario*percentual/100

print("Então, ",nome)
print("Seu aumento foi de ",percentual,"%")
print("Seu novo salário fica em R$ ",salario_novo)
