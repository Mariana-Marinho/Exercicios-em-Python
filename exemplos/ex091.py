"""
4 jogadores jogam dado, guardar em dict e colocar em ordem
"""
from random import randint

jogadores = []
aposta = {}
maior = 0

for i in range(0, 4):
    aposta[f'jogador{i+1}'] = randint(1, 6)
    print(aposta)
    jogadores.append(aposta.copy())
    aposta.clear()

print(jogadores)
