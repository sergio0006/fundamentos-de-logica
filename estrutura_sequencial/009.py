# Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

temp_f = float(input('Digite a temperatura em Fahrenheit: '))


def temperatura(temp_f):
    temp_c = (temp_f - 32) * 5/9
    return temp_c


print(f'A temperatura em graus Celsius é de: {temperatura(temp_f)}')
