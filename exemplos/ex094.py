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
    nome = str(input('nome: '))
    dados['nome'] = nome
    idade = int(input('idade: '))
    dados['idade'] = idade
    sexo = str(input('sexo: ')).upper()[0]
    dados['sexo'] = sexo
    pessoas.append(dados.copy())
    media += idade
    c += 1
    e = input('deseja continuar? [S?N] ').upper()[0]
    if e == 'N':
        break

media = media/c

print('_'*40)
print(f'A) foram cadastradas {c} pessoas')
print(f'B) a média de idade foi de {media:.2f} anos')

print(f'C) as mulheres cadastradas foram: ', end='')
for p in pessoas:
    for k, v in p.items():
        if k == 'sexo' and v == 'M':
            print(p['nome'], end='-')

print(f'D) pessoas mais velhas que a média: ', end='')
for p in pessoas:
    for k, v in p.items():
        if k == 'idade' and v > media:
            print(p['nome'], end='-')
