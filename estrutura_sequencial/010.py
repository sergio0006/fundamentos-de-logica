# Faça um Programa que peça a temperatura em graus
# Celsius, transforme e mostre em graus Fahrenheit.


# formula (°C × 9/5) + 32 = °F


temp_c = float(input('Digite o valor da temperatura em Celsius: '))


def temperatura(temp_c):
    temp_f = (temp_c * 9/5) + 32
    return temp_f


print(f'A temperatura em Fahrenheit é: {temperatura(temp_c)}')
