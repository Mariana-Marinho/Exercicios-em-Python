num = input('digite 3 números: ')
lista = num.split()
print(lista)
i = 0
a = 0
maior = lista[0]
while i < len(lista):
    if lista[a] >= lista[i]:
        maior = lista[a]
        a = a
        i += 1
    else:
        maior = lista[i]
        a = i
        i += 1
print(f'o maior número da lista é {maior}')
i = 0
b = 0
menor = lista[0]
while i < len(lista):
    if lista[b] <= lista[i]:
        menor = lista[b]
        b = b
        i += 1
    else:
        menor = lista[i]
        b = i
        i += 1
print(f'o menor número da lista é {menor}')
