"""
programa que calcula o fatorial de um número usando while
"""
numero = int(input('digite um número: '))
i = 1
fatorial = 1
while i <= numero:
    fatorial = fatorial * i
    print(f'{i} x' if i < numero else f'{i} =', end=' ')
    i += 1
print(f'{numero}! = {fatorial}')
