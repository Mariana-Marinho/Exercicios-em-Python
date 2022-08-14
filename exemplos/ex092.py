"""
Ler nome, ano de nasc, carteira de trabalho e cadastrar a idade, nome, e cttps no dict
mostrar o ano de contratação e salário, com quantos anos vai se aposentar
"""
from datetime import date
ctps = {}
atual = date.today().year

ctps['nome'] = str(input('nome: '))
ano = int(input('ano de nascimento: '))
ctps['idade'] = atual - ano
carteira = int(input('carteira de trabalho (0 se não tiver): '))
if carteira > 0:
    ctps['carteira de trabalho'] = carteira
    ctps['contratação'] = int(input('ano de contratação: '))
    ctps['salario'] = float(input('salario: '))
    aposentadoria = atual - ctps['contratação'] + 35
    ctps['aposentadoria'] = aposentadoria
else:
    ctps['carteira'] = 'não tem'
print('_'*50)
for k, v in ctps.items():
    print(f'{f"{k}: ":<30}{v:>20}')
