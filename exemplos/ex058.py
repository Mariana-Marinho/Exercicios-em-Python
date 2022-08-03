"""
Programa onde o computador escolhe um número entre 0 e 10,
o jogador vai tentar adivinhar até conseguir, mostrando no final quantos palpites foram necessários
"""
from random import randint
computador = randint(0, 2)
i = 0
print(computador)
while i < computador:
    jogador = int(input('tente adivinhar o número que o computador escolheu: '))
    if jogador == computador:
        print('VOCÊ VENCEU!!!!')
        break
    else:
        print('HAHAHAAAA tente de novo')
        i += 1
print('PERDEUUUU HAHAHAAHAHAAAA')
