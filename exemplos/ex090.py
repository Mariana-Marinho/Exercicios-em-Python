"""
Ler nome e média, e calcular a situação de um aluno, mostrar na tela
"""
boletim = dict()

boletim['nome'] = str(input('nome: '))
boletim['media'] = int(input('media: '))

if boletim['media'] >= 7:
    boletim['situacao'] = 'aprovado'
elif boletim['media'] in range(5, 7):
    boletim['situacao'] = 'recuperação'
else:
    boletim['situacao'] = 'reprovado'
print()

for k, v in boletim.items():
    print(f'{k}: {v}')
