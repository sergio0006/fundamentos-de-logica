# Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

ni1 = int(input('Digite um numero inteiro: '))
ni2 = int(input('Digite um segundo numero inteiro: '))
nf1 = float(input('Digite um numero real: '))

dobro_produto = ni1 * 2 * (ni2 / 2)
triplo = ni1 * 3 + nf1
cubo = nf1 ** 3

print(dobro_produto, triplo, cubo)
