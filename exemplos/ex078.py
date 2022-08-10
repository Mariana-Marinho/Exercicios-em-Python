"""
Programa que lê 5 valores e guarde em lista, mostrar qual o maior, o menor e seus indices
"""
numeros = []
maior = menor = 0
for c in range(0, 5):
    numeros.append(int(input('digite um número: ')))
for c in range(0, 5):
    if numeros[c] >= maior:
        maior = numeros[c]
    else:
        menor = numeros[c]
print(f'você digitou os números: {numeros}')
print(f'1- o maior número foi {maior}, na posição:', end=' ')
for indice, valor in enumerate(numeros):
    if valor == maior:
        print(c, end='---')
print(f'\n2- o menor número foi {menor}, na posição:', end=' ')
for indice, valor in enumerate(numeros):
    if valor == menor:
        print(c, end='---')
