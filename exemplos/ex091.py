"""
4 jogadores jogam dado, guardar em dict e colocar em ordem
"""
from random import randint

dado = dict()
maior = 0

for i in range(1, 5):
    dado[f'jogador {i}'] = randint(1, 6)

print(dado)

for k, v in dado.items():
    if k == 'jogador 1' or v >= maior:
        maior = v
    print(f'k vale a primeira chave: {k}')
    print(f'v vale o quanto a chave recebe: {v}')

print(f'o vencedor tirou {maior}')