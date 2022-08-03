"""
Programa que lê o ano de nascimento de 7 pessoas e mostre quantas não tem 18 anos e quantas tem
"""
from datetime import date
maiores = 0
menores = 0
atual = date.today().year
for i in range(1, 8):
    ano = int(input(f'digite o ano de nascimento da {i}ª pessoa: '))
    idade = atual - ano
    if idade >= 21:
        maiores += 1
    elif 0 <= idade < 21:
        menores += 1
    else:
        print('\n\033[31mdigite idades válidas\033[m\n')
print(f'foram informados {menores} menores de idade e {maiores} maiores de idade')
