# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input('digite a nota 1: '))
nota2 = float(input('digite a nota 1: '))
nota3 = float(input('digite a nota 1: '))
nota4 = float(input('digite a nota 1: '))


def soma(nota1, nota2, nota3, nota4):
    soma = nota1 + nota2 + nota3 + nota4
    return soma


def media():
    media = soma(nota1, nota2, nota3, nota4) / 4
    return f'A média do aluno é: {media}'


print(media())
