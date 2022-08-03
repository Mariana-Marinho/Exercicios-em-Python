"""
Ler vários números inteiros, mostrar a média, o maior e o menor
"""
numeros = []
media = 0
soma = 0
i = 0
while i >= 0:
    escolha = input('quer digitar valores? S/N: ').upper()
    if escolha == 'S':
        i += 1
        num = int(input('digite um número inteiro: '))
        soma += num
        numeros.insert(i, num)
    else:
        break
media = soma / i
print(f'a média dos {i} números digitados foi {media}')
print(f'o maior número foi {max(numeros)} e o menor número foi {min(numeros)}')
