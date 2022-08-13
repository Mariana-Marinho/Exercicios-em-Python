"""
Aprimorar o desafio 093, com vários jogadores e visualizar o aproveitamento de cada um
"""
jogador = {}
jogadores = []
gols = []
total = 0
c = 1

while True:
    jogador['nome'] = str(input('digite o nome do jogador: '))
    partidas = int(input(f'digite o número de partidas que {jogador["nome"]} jogou: '))
    if partidas > 0:
        for c in range(0, partidas):
            quant = int(input(f'gols feitos na {c+1}ª partida: '))
            gols.append(quant)
            total += quant
    jogador['gols'] = gols
    jogador['total de gols'] = total
    jogadores.append(jogador.copy())
    e = input('deseja continuar? ')[0]
    if e in 'Nn':
        break

print('_'*40)
print('_' * 40)
print(f'{"cod":<5} {"nome":<15} {"gols":<13} {"total":<7}')

for j in jogadores:
    print(f'{c:<5} {j["nome"]:<15} {j.["gols"]:<13} {j.["total de gols"]:<7}')
    c += 1
c = 1

print('_'*40)

e = int(input('mostrar dados do jogador: '))
print(f'Levantamento do jogador {jogadores[e]["nome"]}:')



