"""
Programa que gera 5 números aleatórios, botar em tuplas, mostrar a lista, o maior e o menor
"""
from random import randint
numeros = (randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11))
menor = maior = 0
for i in range(0, 5):
    if numeros[i] <= menor or i == 0:
        menor = numeros[i]
for i in range(0, 5):
    if numeros[i] >= maior:
        maior = numeros[i]
print(numeros)
print(f'o maior valor é {maior} e o menor é {menor}')
