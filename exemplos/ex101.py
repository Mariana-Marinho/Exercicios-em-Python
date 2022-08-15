"""
Função voto(), que recebe parâmetros: ano de nasc, retorna um texto: voto negado, não obrigatório ou obrigatório
"""
from datetime import date
atual = date.today().year


def linha():
    print('_'*30)


def voto(ano):
    """
    printa a situação do voto de alguém com base na idade
    :param ano: ano de nascimento
    :return: não retorna
    """
    idade = atual - ano
    if 16 <= idade < 18 or idade > 65:
        print(f'{idade} anos: voto facultativo')
    elif idade >= 18:
        print(f'{idade} anos: voto obrigatório')
    else:
        print(f'{idade} anos: voto negado')


while True:
    linha()
    nascimento = input('digite o ano em que você nasceu: ')
    if nascimento.isdigit():
        nascimento = int(nascimento)
        if nascimento <= atual:
            voto(nascimento)
            break
        else:
            print('digite um ano válido')
    else:
        print('digite um inteiro')
