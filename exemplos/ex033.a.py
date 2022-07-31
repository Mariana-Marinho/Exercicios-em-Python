n1 = int(input('primeiro numero: '))
n2 = int(input('segundo numero: '))
n3 = int(input('terceiro número: '))
lista = [n1, n2, n3]
lista = sorted(lista)
print(f'o maior número é {lista[2]}')
print(f'o menor número é {lista[0]}')
