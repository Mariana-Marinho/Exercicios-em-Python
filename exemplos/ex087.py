"""
Desafio 86, mostrar:
1) soma de valores pares
2) soma de valores da 3a coluna
3) maior valor da 2a coluna
"""
matriz = [[], [], []]
soma = maior = soma3 = 0
for i in range(0, 3):
    for c in range(0, 3):
        matriz[i].append(int(input(f'digite um número para a posição [{i}][{c}]: ')))

print('_'*40)

for i in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[i][c]:^3} ]', end='')

        if matriz[i][c] % 2 == 0:
            soma += matriz[i][c]

        if i == 1:
            if c == 0 or matriz[i][c] >= maior:
                maior = matriz[i][c]

        if c == 2:
            soma3 += matriz[i][c]
    print()

print(f'''
a) a soma de todos os valores pares é igual a {soma}
b) a soma dos valores da 3a coluna é igual a {soma3}
c) o maior valor da segunda linha é igual a {maior}''')
