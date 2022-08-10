"""
Tupla com nomes de produtos e preços, mostrar listagem de preços
"""
tupla = 'banana', 1, 'maçã', 5, 'laranja', 3, 'mamão', 10, 'mirtilo', 20
print('_'*40)
print(f'{"COMPRAS DO MÊS":^40}')
print('_'*40)
for c in range(0, len(tupla), 2):
    print(f'{tupla[c]:.<30}', end='')
    print(f'R$ {tupla[c+1]:>5.2f}')
