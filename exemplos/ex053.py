"""
Programa que leia uma frase e diga se ela é um palíndromo, considerando os espaços
"""
print('SERÁ QUE É PALÍNDROMO?\n')
frase_original = input('digite uma frase:\n')
frase = frase_original.replace(" ", "")
if frase.upper() == frase.upper()[::-1]:
    print(f'o inverso de {frase.upper()} é {frase.upper()[::-1]}')
    print(f'"{frase_original}" é palíndromo')
else:
    print(f'o inverso de {frase.upper()} é {frase.upper()[::-1]}')
    print(f'"{frase_original}" não é palíndromo')
