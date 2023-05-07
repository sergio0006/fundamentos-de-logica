"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias.
"""

from math import ceil, floor

area_pintada = float(input('Digite o tamanho do metro quadrado: '))
area_com_folga = area_pintada * 1.1
litros_por_metro = 6
litro_por_lata = 18
litro_por_galao = 3.6
valor_lata = 80
valor_galao = 25

litros_usados = area_com_folga / litros_por_metro
total_de_latas_usada = ceil(litros_usados / litro_por_lata)
valor_total_pago_latas = valor_lata * total_de_latas_usada

total_de_galoes_usado = ceil(litros_usados / litro_por_galao)
valor_total_pago_galoes = valor_galao * total_de_galoes_usado

print(f'Você usará o total de {total_de_latas_usada} de tinta e o valor total será de R$ {valor_total_pago_latas:.2f}')
print(f'Você usará o total de {total_de_galoes_usado} de tinta e o valor total será de R$ {valor_total_pago_galoes:.2f}')

total_de_latas_usada = floor(litros_usados / litro_por_lata)
valor_total_pago_latas = valor_lata * total_de_latas_usada
litros_faltantes = litros_usados % litro_por_lata


total_de_galoes_usado = ceil(litros_faltantes / litro_por_galao)
valor_total_pago_galoes = valor_galao * total_de_galoes_usado

valor_total_pago = valor_total_pago_galoes + valor_total_pago_latas
print(f'Você irá usar {total_de_latas_usada} latas de 18l e {total_de_galoes_usado} galão de 3.6l e irá pagar R$ {valor_total_pago:.2f}')



