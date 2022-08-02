"""
Programa que lê seis números inteiros e mostre a soma dos pares
"""
soma = 0
for c in range(0, 6):
    num = int(input('digite um número: '))
    if num % 2 == 0:
        soma += num
print(f'a soma dos números pares é {soma}')
