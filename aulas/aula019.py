"""
Dicionários
    pode nomear as keys
    em vez de índices, tem elementos/chaves (keys)
    as chaves recebem valores
    itens são as chaves e valores

       dicionário = {
                     'key_1': 'value_1',
                     'key_2': 'value_2',
                     'key_3': 'value_3'
       }

    pode criar uma lista de dicionários
        tupla = ()
        lista = []
        dicionario = {}
"""
# criando duas chavez (nome, idade)
dados = {'nome': 'Pedro', 'idade': 25}
print(dados)
# criando outra chave sexo
dados['sexo'] = 'M'
print(dados)
# deletando um elemento
del dados['idade']
print(dados)

filme = {
    'titulo': 'Star wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme.items())
print(filme.values())
print(filme.keys())
for keys, values in filme.items():
    print(f'o {keys} é {values}')

# criando dicionário dentro de uma lista
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)

estado = dict()
brasil_estados = list()
for c in range(0, 3):
    estado['uf'] = str(input('uf: '))
    estado['sigla'] = str(input('sigla: '))
    brasil_estados.append(estado.copy())
for e in brasil_estados:
    for k, v in e.items():
        print(f'a chave {k} tem valor {v}')

# preenchendo dict com for
dado = {}
for i in range(1, 5):
    dado[f'jogador {i}'] = randint(1, 6)
