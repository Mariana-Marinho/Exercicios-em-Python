"""
Ler nome, sexo e idade de várias pessoas, guardar em dict de cada um e depois guardar em list, mostrar:
A) quantas pessoas foram cadastradas
B) média de idade
C) mulheres
D) pessoas com idade maior que a média
"""
dados = {}
pessoas = []
media = c = 0

while True:
    dados['nome'] = str(input('nome: '))
    idade = int(input('idade: '))
    dados['idade'] = idade
    while True:
        dados['sexo'] = str(input('sexo [M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
    pessoas.append(dados.copy())
    dados.clear()
    media += idade
    while True:
        e = input('deseja continuar? [S?N] ').upper()[0]
        if e in 'NS':
            break
    if e == 'N':
        break


print('_'*40)
print(f'A) foram cadastradas {len(pessoas)} pessoas')
media = media/len(pessoas)
print(f'B) a média de idade foi de {media:.2f} anos')

print(f'C) as mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(p['nome'], end='-')

print(f'\nD) pessoas mais velhas que a média: ', end='')
for p in pessoas:
    if p['idade'] > media:
        print(p['nome'], end='-')
