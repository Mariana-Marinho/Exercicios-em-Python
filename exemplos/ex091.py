"""
4 jogadores jogam dado, guardar em dict e colocar em ordem
"""
from random import randint


aposta = dict()
jogadores = list()

for i in range(0, 4):
    aposta = {
        'jogador': f'jogador{i+1}',
        'numero': randint(1, 6)
    }
    print(aposta)
    jogadores.append(aposta.copy())
    aposta.clear()
print(jogadores)

