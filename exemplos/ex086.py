"""
Matrix 3x3 e preencher com valores pelo teclado, mostrar matriz
"""
matriz = [[], [], []]

for i in range(0, 3):
    for c in range(0, 3):
        matriz[i].append(int(input(f'digite um número para a posição [{i}][{c}]: ')))

print('_'*40)

for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[i][c]:^5}]', end='')
    print('')
