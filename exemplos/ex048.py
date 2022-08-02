"""
Programa que calcule a soma dos números ímpares múltiplos de 3 entre 1 e 500
"""
soma = 0
for c in range(1, 500):
    if c % 3 == 0:
        if c % 2 == 1:
            soma += c
            print(c)
print(soma)
