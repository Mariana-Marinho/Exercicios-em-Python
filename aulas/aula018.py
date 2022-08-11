"""
Estruturas compostas:
    listas dentro de listas
"""
identidade = ['Pedro', 25, 'Maria', 19, 'João', 32]
pessoas = list()
# pessoas tem como índice uma parte da outra lista identidade
pessoas.append(identidade[0:2])
pessoas.append(identidade[2:4])
pessoas.append(identidade[4:6])
print(pessoas)
# o primeiro [] indica o índice de pessoas, e o outro [] de identidade
print(pessoas[0][0], '\n')
# posso também fazer assim:
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for informacao in galera:
    print(f'{informacao[0]} tem {informacao[1]} anos de idade')
# preenchendo essa mesma lista
gente = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    gente.append(dado[:])
    dado.clear()
for p in gente:
    if p[1] >= 50:
        print(f'{p[0]} tem mais de 50')
print(f'\n a lista ficou {gente}')
