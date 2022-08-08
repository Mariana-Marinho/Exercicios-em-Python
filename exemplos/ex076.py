"""
Tupla com nomes de produtos e preços, mostrar listagem de preços
"""
tupla = 'banana', 1, 'maçã', 5, 'laranja', 3, 'mamão', 10, 'mirtilo', 20
for c in range(0, len(tupla), 2):
    print(f'{tupla[c]}.................', end=' ')
    print(f'{tupla[c+1]}')
