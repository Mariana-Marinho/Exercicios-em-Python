"""
Programa onde o computador escolhe um número entre 0 e 10,
o jogador vai tentar adivinhar até conseguir, mostrando no final quantos palpites foram necessários
"""
from random import randint
computador = randint(0, 10)
acertou = False
i = 1
while not acertou:
    jogador = int(input('tente adivinhar o número que o computador escolheu: '))
    if jogador == computador:
        print(f'VOCÊ VENCEU!!!! {i} palpites necessários')
        break
    else:
        print('ish... chuta de novo')
        i += 1
print(f'PERDEUUUU HAHAHAAHAHAAAA, {i} palpites e não acertou...')
