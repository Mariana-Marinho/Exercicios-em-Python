from random import randint, choice
nome1 = input('digite o nome de seus quatro alunos: ')
nome2 = input('')
nome3 = input('')
nome4 = input('')
lista = [nome1, nome2, nome3, nome4]
# escolhendo um número e usando-o como index
x = randint(0, 3)
print(f'o aluno escolhido foi {lista[x]}')
# escolhendo um item da lista
print(f'o outro aluno escolhido foi {choice(lista)}')
