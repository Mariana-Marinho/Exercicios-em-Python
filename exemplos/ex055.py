"""
Programa que lÊ o peso de 5 pessoas e mostre qual o maior e qual o menor peso
"""
pesos = []
for c in range(0, 5):
    peso = float(input('informe o peso: '))
    pesos.insert(c, peso)
pesos = sorted(pesos)
print(pesos)
print(f'o maior peso é {pesos[4]:.2f}kg e o menor é {pesos[0]:.2f}kg')
