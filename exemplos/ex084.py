"""
Ler nome e peso de várias pessoas, mostrar:
1) pessoas mais pesadas
2) pessoas mais leves
3) quantas pessoas cadastradas
"""
dados = list()
pessoas = list()
c = maior = menor = 0

while True:
    dados.append(str(input('nome: ')))
    dados.append(int(input('idade: ')))
    pessoas.append(dados[:])
    dados.clear()
    c += 1

    for p in pessoas:
        if p == pessoas[0] or p[1] >= maior:
            maior = p[1]
        if p == pessoas[0] or p[1] <= menor:
            menor = p[1]

    e = input('deseja continuar? [S/N] ').upper()[0]
    if e == 'N':
        break

print(f'você cadastrou {c} pessoas')
print(f'o maior peso foi de {maior}: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')

print('')

print(f'o menor peso foi de {menor}: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' ')
