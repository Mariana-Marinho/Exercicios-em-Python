"""
Caixa eletrônico:
1- ler o valor a ser sacado
2- informar quantas cédulas (50, 20, 10 e 5) serão dadas
"""
valor = int(input('digite o valor a ser sacado: '))
cinquenta = vinte = dez = cinco = 0
if valor != 0:
    cinquenta = valor // 50
    valor -= cinquenta*50
    vinte = valor // 20
    valor -= vinte*20
    dez = valor // 10
    valor -= dez*10
    cinco = valor // 5
    valor -= cinco*5
print(f'''
{cinquenta} notas de 50
{vinte} notas de 20
{dez} notas de 10
{cinco} notas de 5''')
