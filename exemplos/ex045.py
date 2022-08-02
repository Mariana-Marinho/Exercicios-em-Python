"""
Programa que faça o computador jogar jokenpô com você
"""
from random import choice
from time import sleep
print(f'\033[7;30m   JO   \033[m')
sleep(1)
print(f'\033[7;30m  KEN   \033[m')
sleep(1)
print(f'\033[7;30m   PÔ   \033[m')
sleep(1)
escolha = input('escolha entre pedra, papel ou tesoura: ')
opcoes = ['pedra', 'papel', 'tesoura']
computador = choice(opcoes)
if escolha.upper().find("PEDRA") != -1:
    if computador in ['papel']:
        print(f'eu escolhi {computador} HAHAAAAA VOCÊ PERDEU')
    elif computador in ['tesoura'] != 0:
        print(f'a não... eu escolhi {computador}, você ganhou :(')
    elif computador in ['pedra']:
        print('HAHAYYY FOI EMPATE')
elif escolha.upper().find("PAPEL") != -1:
    if computador in ['pedra']:
        print(f'a não... eu escolhi {computador}, você ganhou :(')
    elif computador in ['papel']:
        print('HAHAYYY FOI EMPATE')
    elif computador in ['tesoura']:
        print(f'eu escolhi {computador} HAHAAAAA VOCÊ PERDEU')
elif escolha.upper().find("TESOURA") != -1:
    if computador in ['pedra']:
        print(f'eu escolhi {computador} HAHAAAAA VOCÊ PERDEU')
    elif computador in ['tesoura']:
        print('HAHAYYY FOI EMPATE')
    elif computador in ['papel']:
        print(f'a não... eu escolhi {computador}, você ganhou :(')
