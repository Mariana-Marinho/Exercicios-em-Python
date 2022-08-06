"""
usando for
"""
valor = int(input('digite o valor a ser sacado: '))
for cedula in (50, 20, 10, 5):
    notas = valor // cedula
    valor -= notas*cedula
    print(f'{notas} cédulas de {cedula} reais')
    if valor == 0:
        break
