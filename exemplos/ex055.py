"""
Programa que lÊ o peso de 5 pessoas e mostre qual o maior e qual o menor peso
"""
pesos = []
i = 1
for c in range(0, 5):
    peso = float(input(f'informe o peso da {i}ª pessoa: '))
    pesos.insert(c, peso)
pesos = sorted(pesos)
print(f'\no maior peso é {max(pesos):.2f}kg e o menor é {min(pesos):.2f}kg')
