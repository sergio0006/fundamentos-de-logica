# Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês. Calcule e mostre o total
# do seu salário no referido mês.

salario = float(input('Digite quanto você ganha por hora: '))
hora_trabalhada = int(input("Digite quantas horas você trabalha no mês: "))

valor_total = salario * hora_trabalhada
print(f'Você ganha por mês: R${valor_total}')
