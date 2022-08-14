"""
Aprimorar o desafio 093, com vários jogadores e visualizar o aproveitamento de cada um
"""
atleta = {}
jogadores = []
gols = []
total = 0
c = 0

while True:
    atleta['nome'] = str(input('digite o nome do jogador: '))
    partidas = int(input(f'digite o número de partidas que {atleta["nome"]} jogou: '))
    if partidas > 0:
        for c in range(0, partidas):
            quant = int(input(f'gols feitos na {c+1}ª partida: '))
            total += quant
            gols.append(quant)
    atleta['gols'] = gols.copy()
    gols.clear()
    atleta['total de gols'] = total
    total = 0
    jogadores.append(atleta.copy())
    e = input('deseja continuar? ')[0]
    if e in 'Nn':
        break

print('_'*40)
print(f'cod', end=' ')
for i in atleta.keys():
    print(f'{i:<12}', end='')
print()
print('_' * 40)
for i, d in enumerate(jogadores):
    print(f'{i:>3}', end=' ')
    for v in d.values():
        print(f'{str(v):<12}', end=' ')
    print()
print('_' * 40)

while True:
    e = int(input('exibir os dados do jogador (999 para parar): '))
    if e == 999:
        break
    elif e >= len(jogadores):
        print('digite um número válido')
    else:
        print(f'levantamento do jogador {jogadores[e]["nome"]}:')
        for i, g in enumerate(jogadores[e]['gols']):
            print(f'    no {i+1}º jogo o jogador fez {g} gols')
