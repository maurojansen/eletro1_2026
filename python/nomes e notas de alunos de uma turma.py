# nomes e notas de alunos de uma turma
print("Programa nomes e notas de alunos de uma turma")
quant_alunos=0
continuar="S"
while continuar=="S" or continuar=='s':
  nome=input("Digite o nome do aluno: ")
  nota=float(input("Digite a nota do aluno: "))
  quant_alunos += 1
  continuar=input("Tem mais alunos (S/N)? ")
print("Quantidade de alunos: ",quant_alunos)
print("FIM !")
