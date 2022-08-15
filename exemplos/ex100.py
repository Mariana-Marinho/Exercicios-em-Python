"""
Lista numeros[], função sorteia(), função somaPar()
sortear 5 números e botar em lista, mostrar soma entre os pares
"""
from random import sample


def sorteia(quantidade):
    numeros = [sample(range(1, 10), quantidade)]
    return numeros


def soma_par(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'a soma entre os números pares da lista {lista} deu {soma}')


num = sorteia(int(input('quantos números a sortear? ')))
print(f'sorteando {len(num)} valores: {num}')
soma_par(num)
