"""
Função leiaint() e leiafloat(), com tratamento de exceções
"""


def leia_int(frase):
    while True:
        numero = input(frase)
        try:
            return int(numero)
        except:
            print(f'deu erro, digite um número inteiro válido')


def leia_float(frase):
    while True:
        numero = input(frase)
        try:
            return float(numero)
        except KeyboardInterrupt:
            return 0
        except:
            print(f'deu erro, digite um número real válido')


inteiro = leia_int('digite um número inteiro: ')
real = leia_float('digite um número real: ')
print(f'os valores digitados foram: inteiro foi {inteiro} e o real foi {real}')
