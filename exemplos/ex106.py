"""
Mini sistema que use o help(), o usuário vai digitar o comando e o manual vai aparecer, termina quando digita 'FIM'
"""


def bloco(frase, cor='\033[m'):
    tamanho = len(frase)+4
    print(cor)
    print('_'*tamanho)
    print(f'  {frase}')
    print('_'*tamanho)
    print(f'\033[m')


def manual(comando):
    bloco(f'{help(comando)}', '\033[46m')


while True:
    funcao = input('função: ')
    if funcao.upper().strip() == 'FIM':
        print('FIM')
        break
    else:
        bloco('ACESSANDO O MANUAL', '\033[45m')
        manual(funcao)
