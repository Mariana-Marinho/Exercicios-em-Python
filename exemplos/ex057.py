"""
Programa que lê o sexo de uma pessoa, caso esteja errado peça novamente
"""
sexo = input('Sexo [F/M]:  ').upper()[0]
while sexo not in 'FM' or sexo == "":
    sexo = input('digite seu sexo M ou F: ').upper()
print(f'sexo {sexo} registrado')
