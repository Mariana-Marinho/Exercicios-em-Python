"""
Função contador() que recebe início, fim e passo
1) de 1 até 10, de 1 em 1
2) de 10 até 0, de 2 em 2
3) uma contagem personalizada
"""
from time import sleep


def contador(inicio, fim, passo):
    lista = []
    if passo == 0:
        passo = 1
    if inicio > fim:
        for c in range(fim, inicio+1):
            lista.insert(0, c)
    else:
        for c in range(inicio, fim+1):
            lista.append(c)
    print('_'*30)
    print(f'contagem de {inicio} a {fim}, pulando de {passo} em {passo}')
    print(lista[::passo])


'''contador(1, 10, 1)
contador(0, 10, -2)'''
print('_' * 30)
print('Personalizado: ')
ini = int(input('início: '))
mei = int(input('fim: '))
pula = int(input('pular: '))
contador(ini, mei, pula)
