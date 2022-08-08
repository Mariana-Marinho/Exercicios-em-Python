from random import sample
aleatorios = tuple(sample(range(10), 5))
print(f'foram sorteados os números: {aleatorios}')
print(f'o maior valor foi {max(aleatorios)}, e o menor foi {min(aleatorios)}')
