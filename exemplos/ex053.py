"""
Programa que leia uma frase e diga se ela é um palíndromo, considerando os espaços
"""
print('SERÁ QUE É PALÍNDROMO?')
frase = input('digite uma frase:\n').replace(" ", "")
if frase.upper() == frase.upper()[::-1]:
    print(f'"{frase}" é palíndromo')
else:
    print(f'"{frase}" não é palíndromo')
