"""
Função fatorial() que receba parâmetros: número e show, que mostrará se deve mostrar o processo ou não
"""


def fatorial(numero, show=False):
    """
    mostra o fatorial de um número e o processo, se você quiser
    :param numero: inteiro
    :param show: booleano, indica se quer mostrar o processo ou não
    :return: não retorna
    """
    f = 1
    for i in range(numero, 0, -1):
        f *= i
        if show is True:
            if i > 1:
                print(f'{i} x', end=' ')
            else:
                print(f'1 = {f}')
        else:
            print(f)


while True:
    num = input('fatorial de ')
    if num.isdigit():
        while True:
            num = int(num)
            escolha = str(input('deseja que mostre o processo? [S/N] ')).upper()[0]
            if escolha in 'NS':
                if escolha == 'N':
                    fatorial(num)
                else:
                    fatorial(num, True)
                break
            else:
                print('digite [S/N]')
        break
    else:
        print('digite um número')
