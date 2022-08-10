"""
Ler números, botar em lista, fazer outras duas listas com pares e ímpares
"""
lista = []
pares = []
impares = []
while True:
    lista.append(int(input('digite um número: ')))
    escolha = input('deseja continuar? [S/N]: ')[0]
    if escolha == 'Nn':
        break
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        pares.append(lista[c])
    else:
        impares.append(lista[c])
print(f"""
1) você digitou os números: {lista}
2) os pares são {pares}
3) os ímpares são {impares}""")
