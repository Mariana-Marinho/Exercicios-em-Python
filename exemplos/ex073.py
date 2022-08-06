"""
Tupla com 20 primeiros colocados no brasileirão, mostrar:
1: os 5 primeiros colocados
2: últimos 4
3: ordem alfabética
4: onde está o santos
"""
classificados = ('Palmeiras', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Flamengo', 'Internacional', 'Atlético-MG',
                 'Bragantino', 'Santos', 'São Paulo', 'Goiás', 'Botafogo', 'América-MG', 'Ceará', 'Coritiba', 'Avaí',
                 'Cuiabá', 'Fortaleza', 'Atlético-GO', 'Juventude')
print('_'*50)
print('TABELA BRASILEIRÃO'.center(50))
print('_'*50)
print(f'''
[1] os primeiros colocados foram {classificados[:5]}
[2] os 4 últimos foram {classificados[-4:]}
[3] em ordem alfabética: {sorted(classificados)}
[4] o Santos está na {classificados.index('Santos') + 1}ª posição''', end=' ')
