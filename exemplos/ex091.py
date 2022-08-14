"""
4 jogadores jogam dado, guardar em dict e colocar em ordem
"""
from random import randint
from operator import itemgetter

jogadores = {}
podio = []

for i in range(0, 4):
    jogadores[f'jogador{i+1}'] = randint(1, 6)

for k, v in jogadores.items():
    print(f'{k} tirou {v}')

# sort por ordem do item, a 2a posição da biblioteca (valores do dado)
podio = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print()
print('O PÓDIO FICOU:')
for i, v in enumerate(podio):
    print(f'{i+1}º lugar {v[0]} com {v[1]}')
