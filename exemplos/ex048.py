"""
Programa que calcule a soma dos números ímpares múltiplos de 3 entre 1 e 500
"""
soma = 0
c = 0
for i in range(3, 500, 3):
    if i % 2 == 1:
        soma += i
        c += 1
print(f'a soma dos {c} números ímpares múltiplos de 3 entre 1 e 500, vale {soma}')
