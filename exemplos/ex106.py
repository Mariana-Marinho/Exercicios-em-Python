"""
Mini sistema que use o help(), o usuário vai digitar o comando e o manual vai aparecer, termina quando digita 'FIM'
"""
from time import sleep
cores = ('\033[m', '\033[44m', '\033[46m', '\033[45m')


def bloco(frase='', cor=0):
    tamanho = len(frase)+4
    print(cores[cor])
    print('_'*tamanho)
    print(frase)
    print('_'*tamanho)
    print(cores[0])
    sleep(1)


def manual(comando):
    bloco(f'acessando o manual do comando {comando}', 2)
    print(cores[1])
    help(comando)
    print(cores[0])
    sleep(2)


while True:
    bloco('HELP - digite FIM para terminar', 3)
    funcao = input('função: ')
    if funcao.upper().strip() == 'FIM':
        print('FIM')
        break
    else:
        manual(funcao)
