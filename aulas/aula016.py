"""
Variáveis compostas
    tupla:
        recebe mais de um elemento, por índice
        identificado com (), mas nem precisa usar
        SÃO IMUTÁVEIS
            tupla = ()
            tupla[int, str, float] = (1, 'mariana', 4.5)
            print(tupla[0:2])= 1, 'mariana'
            print(tupla[2:])= 'mariana', 4.5
            print(tupla[-1])= 4.5, 'mariana', 1
            for c in tupla:
                print(c)= 1, 'mariana', 4.5
            tupla_nova= ('mariana', 'marinho')
"""
nome = ('mariana', 'marinho', 'da', 'silva', 'andrade')
for n in nome:
    print(n.capitalize())

for posicao, n in enumerate(nome):
    print(f'{n}, na posicao {posicao}')

for i in range(0, len(nome)):
    print(nome[i], f'na posição {i}')

print('\n')
print(nome[::-1], end=' ')
print('\n')
print(nome[0:2], end=' ')
# agora vai dar erro:
# nome[-1] = 'orleans bragança'
nome1 = ('mariana', 'marinho')
nome2 = ('da', 'silva', 'andrade')
nomes = nome1 + nome2
print(nomes.count('mariana'), 'vezes que aparece (mariana)')
print(nomes.index('marinho'), 'posição que está o nome marinho')
