"""
Programa que lê o sexo de uma pessoa, caso esteja errado peça novamente
"""
i = 0
while i == 0:
    sexo = input('Sexo [F/M] ? ').upper()
    if not sexo in 'M' and not sexo in 'F':
        print('digite novamente')
