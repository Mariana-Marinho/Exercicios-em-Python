"""
Função ficha(), que recebe parâmetros opcionais: nome do jogador, gols
mostrar a ficha do jogador
"""


def ficha(atleta='', gols=''):
    """
    printa o número de gols feitos por um atleta
    :param atleta: nome do atleta
    :param gols: número de gols
    :return: não retorna
    """
    if atleta == '':
        atleta = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'{atleta} fez {gols} gols')


nome = input('nome do atleta: ')
numero = input(f'quantos gols foram feitos por {nome}? ')
ficha(nome, numero)
