# Tendo como dados de entrada a altura de uma pessoa, construa um
# algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
# (72.7*altura) - 58
peso = 72.7
altura = float(input('Digite sua altura: '))


def peso_ideal(peso, altura):
    peso = peso * altura - 58
    return peso


print(f'o pesoa ideal seria {peso_ideal(peso, altura)} Kg')
