"""
Programa que mostra a tabuada de um número escolhido pelo usuário
"""
numero = int(input('digite um número para ver sua tabuada: '))
for c in range(1, 11):
    tabuada = numero * c
    print(f'{numero} x {c:2} = {tabuada}')
