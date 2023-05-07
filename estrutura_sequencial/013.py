# Tendo como dado de entrada a altura (h) de uma pessoa, construa
# um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input('Digite sua altura: '))
sexo = input('Digite seu sexo: M: Masculino e F: Feminino: ')


def peso_ideal_feminino(altura):
    peso = 62.1
    peso = peso * altura - 44.7
    return peso


def peso_ideal_masculino(altura):
    peso = 72.7
    peso = peso * altura - 58
    return peso


if sexo == 'F':
    print(f'o pesoa ideal seria {peso_ideal_feminino(altura):.2f} Kg')
else:
    print(f'o pesoa ideal seria {peso_ideal_masculino(altura):.2f} Kg')

print('fim')
