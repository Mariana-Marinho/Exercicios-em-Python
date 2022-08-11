"""
Matrix 3x3 e preencher com valores pelo teclado, mostrar matriz
"""
linha = list()
matriz = list()
for i in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'digite um número para a posição [{i}][{c}]: '))
        linha.append(num)
    matriz.append(linha[:])
    linha.clear()
print('_'*40)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[i][c]:^3} ]', end='')
    print('')
