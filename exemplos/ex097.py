"""
Função que receba um texto e o printe com linhas adaptáveis
"""
from time import sleep


def escreva(frase):
    tamanho = len(frase) + 4
    print('_'*tamanho)
    print(f'  {frase}')
    print('_'*tamanho)


escreva('Olá Mundo')
e = input('digite uma frase: ')
sleep(1)
escreva(e)
