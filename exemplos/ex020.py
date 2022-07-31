from random import shuffle
nome1 = input('digite o nome do aluno: ')
nome2 = input('digite o nome do aluno: ')
nome3 = input('digite o nome do aluno: ')
nome4 = input('digite o nome do aluno: ')
lista = [nome4, nome3, nome2, nome1]
# misturando a ordem
print(f'{shuffle(lista)}', lista)
