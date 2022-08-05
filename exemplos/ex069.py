"""
Programa que lê idade e sexo, mostrar quantos são de maior, quantos homens e quantas mulheres menores de 20 anos
"""
i = 0
m = h = 0
while i >= 0:
    print('-'*20)
    print('CADASTRE UMA PESSOA\n')
    print('-' * 20)
    sexo = input('sexo [M/F]: ').strip().upper()[0]
    idade = int(input('idade: '))
    if idade >= 18:
        i += 1
    if sexo in 'F' and idade > 20:
        m += 1
    elif sexo in 'M':
        h += 1
    escolha = input('\nquer continuar? [S/N] ').strip().upper()[0]
    print('\n')
    if escolha in 'N':
        break
print(f'''foram lidos:
[{i}] pessoas maiores de idade
[{m}] mulheres com mais de 20 anos
[{h}] homens''')
