"""
Programa que lê o ano de nascimento de 7 pessoas e mostre quantas não tem 18 anos e quantas tem
"""
from datetime import date
maiores = 0
menores = 0
for c in range(0, 7):
    ano = int(input('digite o ano de nascimento de alguém: '))
    idade = date.today().year - ano
    if idade >= 21:
        maiores += 1
    elif idade < 21:
        menores += 1
print(f'foram informados {menores} menores de idade e {maiores} maiores de idade')
