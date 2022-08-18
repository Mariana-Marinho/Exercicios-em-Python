"""
Função leiaint() e leiafloat(), com tratamento de exceções
"""


def leia_int(frase):
    while True:
        try:
            numero = int(input(frase))
        except KeyboardInterrupt:
            print('\n\033[31mentrada de dados interrompida\033[m')
            return 0
        except (ValueError, TypeError):
            print(f'\033[31mERRO: digite um número inteiro válido\033[m')
            continue
        else:
            return numero


def leia_float(frase):
    while True:
        try:
            numero = float(input(frase))
        except KeyboardInterrupt:
            print('\n\033[31mentrada de dados interrompida\033[m')
            return 0
        except (ValueError, TypeError):
            print(f'\033[31mERRO: digite um número real válido\033[m')
            continue
        else:
            return numero


inteiro = leia_int('digite um número inteiro: ')
real = leia_float('digite um número real: ')
print(f'os valores digitados foram: inteiro foi {inteiro} e o real foi {real}')
