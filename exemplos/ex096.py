"""
Função área que receba as dimensões de um terreno e mostre a área
"""


def getarea(lar, comp):
    area = lar*comp
    print(f'a área de um terreno {lar}mX{comp}m vale {area}m²')


largura = int(input('largura do seu terreno em m: '))
comprimento = int(input('comprimento em m: '))
print('_'*30)
getarea(largura, comprimento)
