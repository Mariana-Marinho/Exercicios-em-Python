"""
Programa que lê seis números inteiros e mostre a soma dos pares
"""
soma = 0
c = 0
for i in range(1, 7):
    num = int(input(f'digite o {i}º número: '))
    if num % 2 == 0 and num != 0:
        soma += num
        c += 1
if c == 0:
    print('nenhum valor par foi informado')
else:
    print(f'a soma dos {c} números pares informados é {soma}')
