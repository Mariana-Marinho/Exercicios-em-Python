"""
Jogar par ou ímpar com o computador, acaba quando o jogador perder, mostrando as vitórias
"""
from random import randint
print('-' * 20)
print('PAR OU ÍMPAR')
print('-' * 20)
c = 0
while True:
    computador = randint(0, 10)
    num_jogador = int(input('digite um valor: '))
    soma = computador+num_jogador
    jogador = input('P para PAR ou I para IMPAR: ').strip().upper()[0]
    if soma % 2 == 0:
        deu = 'Pp'
        print(f'você jogou {num_jogador} e o computador escolheu {computador}, deu PAR!!!')
    else:
        deu = 'Ii'
        print(f'você jogou {num_jogador} e o computador escolheu {computador}, deu ÍMPAR!!!')
    if jogador in deu:
        c += 1
        print('vamos mais uma vez\n')
    else:
        break
print(f'''ihhhhh errou :(
      mas parabéns, você ganhou {c} vezes''')
