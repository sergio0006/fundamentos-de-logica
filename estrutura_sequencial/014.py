""" João Papo-de-Pescador, homem de bem, comprou um microcomputador para
controlaro rendimento diário de seu trabalho. Toda vez que ele traz um peso de
peixes maior que o estabelecido pelo regulamento de pesca do estado de São
Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João
precisa que você faça um programa que leia a variável peso (peso de peixes)
e calcule o excesso. Gravar na variável excesso a quantidade de quilos além
do limite e na variável multa o valor da multa que João deverá pagar. Imprima
os dados do programa com as mensagens adequadas.
"""
kg_peixe = float(input('Digite o peso do peixe: '))

valor_taxa = 4

if kg_peixe > 50:
    peso_excedente = kg_peixe - 50
    taxa = peso_excedente * valor_taxa
    print(f'O valor da taxa é de R$ {taxa:.2f}')
