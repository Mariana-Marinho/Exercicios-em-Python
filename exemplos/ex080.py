"""
Programa que lê 5 números, pôr em ordem crescente sem usar sort
"""
lista = []
for c in range(0, 5):
    num = int(input('digite um valor: '))
    if c == 0 or num >= lista[c-1]:
        lista.append(num)
        print(lista)
    else:
        i = 0
        while i < len(lista):
            if num <= lista[i]:
                lista.insert(i, num)
                print(lista)
                break
            i += 1
print(f'\n{lista}')
