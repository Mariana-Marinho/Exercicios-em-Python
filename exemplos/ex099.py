"""
Função maior() que receba vários parâmetros, mostrar o maior
"""
from time import sleep


def getmaior(*numeros):
    print('_'*30)
    print(f'foram informados {len(numeros)} valores')
    maior = 0
    for i, v in enumerate(numeros):
        print(v, end='...')
        sleep(0.5)
        if i == 0 or v > maior:
            maior = v
    print()
    print(f'o maior valor é {maior}')


getmaior(2, 9, 5, 7, 1)
getmaior(4, 7, 0)
getmaior(1, 2)
getmaior(6)
getmaior()
