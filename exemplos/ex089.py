"""
Ler nomes e notas, mostrar boletim com a média de cada aluno e notas individuais
"""
boletim = list()

while True:
    nome = str(input('nome: '))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1+nota2)/2
    boletim.append([nome, [nota1, nota2], media])
    e = input('deseja continuar? ').upper()[0]
    if e == 'N':
        break

print('_'*30)
print(f'{"Nº":^4}{"NOME":<10}{"MÉDIA":>8}')
print('_'*30)

for num, aluno in enumerate(boletim):
    print(f'{num:^4}{aluno[0]:<10}{aluno[2]:>8}')
e = int(input('quer ver a nota de qual aluno? digite o número: '))
if e in range(0, len(boletim)):
    print(f'as notas de {boletim[e][0]} são {boletim[e][1]}')
