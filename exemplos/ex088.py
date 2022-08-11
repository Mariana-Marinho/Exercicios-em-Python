"""
Criar 6 palpites entre 1 e 60 para cada jogo informado
"""
from random import randint
from time import sleep

jogos = list()
palpites = list()
print('MEGA SENA')
print('_'*40)
quant = int(input('quantos jogos você deseja? '))
for i in range(0, quant):
    for c in range(0, 6):
        numero = randint(1, 60)
        if numero not in palpites:
            palpites.append(numero)
        else:
            numero = randint(1, 60)
            palpites.append(numero)
    jogos.append(palpites[:])
    print(f'jogo {i}: {jogos[i]}')
    sleep(0.5)
    palpites.clear()
