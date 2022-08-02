# Programa que leia o ano de nascimento do atleta e retorne sua categoria
from datetime import date

print('\nCATEGORIAS DA NATAÇÃO\n')
ano = int(input('digite o ano de nascimento do atleta: '))
idade = date.today().year-ano
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JÚNIOR')
elif idade <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')
