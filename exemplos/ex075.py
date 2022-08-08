"""
Programa que lê 4 valores e os guarde em tupla, mostre:
A) quantas vezes apareceu o 9
B) em que posição foi digitado o 3
C) quais foram os números pares
"""
tupla = (int(input('digite um valor: ')), int(input('digite mais um: ')), int(input('digite outro: ')),
         int(input('mais outro: ')))
print(tupla)
menor = i = 0
print(f'A) o 9 apareceu {tupla.count(9)} vezes')
print(f'B) os números pares foram: ', end='')
for c in range(0, 4):
    if tupla[c] % 2 == 0:
        print(tupla[c], end=' ')
if 3 in tupla:
    print(f'\nC) o 3 aparece na posição {tupla.index(3) + 1}')
else:
    print('\nC) o número 3 não aparece')