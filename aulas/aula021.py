"""
Interactive Help:
    no console do python:
        >>help()
        >>print
        >>flush
        >>len
    ou
        >>help(print)
        >>help(flush)
        >>help(len)
    ou
        print(print.__doc__)
        print(flush.__doc__)
        print(len.__doc__)
    ou
        print(help(print))
        print(help(flush))
        print(help(len))


DOCSTRING:
    string de documentação, tipo um manual
    na primeira linha de uma def, abrir 3 aspas duplas e escreve oq ela faz, pq o help vai mostrar esse comentário


Parâmetros opcionais
    no parâmetro opcional, botar do lado =0
    se não for informado, o valor vai valer 0, ou 1, ou o valor que queira


Escopos
    local:
        só existe/só pode ser chamado dentro da função
    global:
        está na main e pode ser chamado em qualquer local do programa
"""


def produto(a, b):
    """
    :param a: um número qualquer
    :param b: um número qualquer
    :return: o produto entre a e b
    """
    soma = a * b
    return soma


def somar(a=0, b=0, c=0):
    """
    soma os valores a, b e c, se algum não for informado, então recebem 0
    :param a: um float qualquer
    :param b: um float qualquer
    :param c: um float qualquer
    :return: soma de a+b+c
    """
    soma = a + b + c
    return soma


def fatorial(num=1):
    """
    retorna o fatorial de um número
    :param num: um int
    :return: fatorial de num
    """
    fat = 1
    for c in range(num, 0, -1):
        print(f'{c}*', end='')
        fat *= c
    print()
    return fat


print(len.__doc__)
print(help(len))
print()

help(produto)
print()

help(somar)
print()

# a=2, c=3 e b não vai ser informado, b é um parâmetro opcional
print(somar(c=3, a=2))
print()

print(fatorial(4))
