"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total.
"""

metros = float(input('Digite o tamanho do metro quadrado: '))

litro_usado = metros / 3
litro_da_lata = 18
preco_da_lata = 80

if litro_usado > litro_da_lata:
    lata_usada = litro_usado / litro_da_lata
else:
    lata_usada = 1
print(litro_usado)
print(f'''você irá usar no total {lata_usada:.0f}
lata(s) de tintas para pintar este local.''')
preco_total = lata_usada * preco_da_lata
print(f'O valor total da(s) lata(s) de tintas fica de: R$ {preco_total:.2f}')
