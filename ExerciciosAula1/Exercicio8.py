# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

hora = float(input("Digite a quantidade de horas trabalhadas no mês:"))
valor = float(input("Digite o valor por hora:"))

salario = hora * valor

print("O salário do mês é", salario)
