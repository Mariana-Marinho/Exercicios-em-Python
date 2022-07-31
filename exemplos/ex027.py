nome = input('digite o seu nome completo: ')
lista = nome.split()
nomes = len(lista)
print(f'Olá, {lista[0]}, seu último nome é {lista[nomes-1]}, achei muito bonito!')
