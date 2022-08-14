"""
Funções
    funções internas: print(); float(); input(); len()
    funções não internas:
        def função(o que recebe, caso receba):
            o que a função faz
            return algo que retorna
"""


def bloco(frase):
    print('_'*40)
    print(f'{frase:^40}')
    print('_'*40)


# empacotamento: pode receber mais de um valor e junta numa tupla
def contador(*num):
    print(f'em {num} existem {len(num)} números')


def dobrar(lista):
    i = 0
    print(f'{lista} -> ', end='')
    while i < len(lista):
        lista[i] *= 2
        i += 1
    print(lista)


# desempacotamento: receber valores diferentes e não junta
def somar(x, y):
    soma = x+y
    print(f'a soma de {x}+{y} = {soma}')


bloco('Mariana')
bloco('Marinho')
print()

contador(4, 6, 1, 6, 1)
contador(9, 2, 6)
print()

dobrar([1, 4, 2, 5, 6])
dobrar([7, 1, 5])
print()

somar(2, 4)
somar(y=3, x=2)
print()
