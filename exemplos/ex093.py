"""
Ler o nome de um jogador e quantas partidas jogou, quantidade de gols em cada partida, mostrar total de gols
"""
jogador = {}
gols = []
total = 0

jogador['nome'] = str(input('digite o nome do jogador: '))
partidas = int(input(f'digite o número de partidas que {jogador["nome"]} jogou: '))
if partidas > 0:
    for c in range(0, partidas):
        gols.append(int(input(f'gols feitos na {c+1}ª partida: ')))
    jogador['gols'] = gols[:]
    jogador['total de gols'] = sum(gols)

print('_'*40)
print(jogador)
print('_'*40)
for k, v in jogador.items():
    print(f'{k} tem valor:           {v}')
print('_'*40)

if len(gols) > 0:
    print(f'{jogador["nome"]} jogou {len(gols)} partidas: ')
    for i, v in enumerate(gols):
        print(f'     na {i+1}ª partida, {jogador["nome"]} fez {v} gols')

