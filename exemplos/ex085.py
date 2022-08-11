"""
digitar 7 valores e cadastrar em lista, manter separado valores pares e impares, mostrar crescente
"""
numeros = [[], []]

for i in range(0, 7):
    num = int(input(f'digite o {i+1}º número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()
print(f'\nos números pares são {numeros[0]}')
print(f'os números ímpares são {numeros[1]}')
