"""
Ler nome e média, e calcular a situação de um aluno, mostrar na tela
"""
boletim = dict()

boletim['nome'] = str(input('nome: '))
boletim['media'] = int(input('media: '))

if boletim['media'] >= 7:
    print('você está aprovado')
else:
    print('você está reprovado')
