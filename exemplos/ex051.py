"""
Programa que lê o primeiro termo e a razão de uma progressão aritmética an = a1 + (n-1) * r
"""
a1 = float(input('digite o primeiro termo da progressão: '))
r = float(input('digite a razão da progressão: '))
progressao = []
for n in range(1, 11):
    termo = a1 + (n - 1) * r
    print(f'o {n:2}º termo é {termo:2}')
    progressao.insert(n, termo)
print(f'os 10 primeiros termos da progressão: {progressao}')
