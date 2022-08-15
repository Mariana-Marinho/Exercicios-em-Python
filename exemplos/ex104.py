"""
Função leia_int(), funcionará como input, mas só de um valor numérico
"""


def leia_int(numero):
    while True:
        if numero.isnumeric():
            return numero
        else:
            numero = input(f'\033[31mdigite somente um número inteiro positivo: \033[m')


n = leia_int(input('digite um número: '))
print(f'você digitou o número {n}')
