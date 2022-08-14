"""
Função que receba um texto e o printe com linhas adaptáveis
"""


def escreva(frase):
    tamanho = len(frase)
    print('_'*tamanho)
    print(f'{frase}')
    print('_'*tamanho)


escreva('  Olá Mundo  ')
