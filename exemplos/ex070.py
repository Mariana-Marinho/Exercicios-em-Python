"""
Programa que lê preços, mostrar total, gasto quantos mais caros que 1000 e o mais barato
"""
print('&'*20)
print('LENDO PREÇOS DE PRODUTOS')
print('&'*20)
continuar = 'S'
mais_barato = []
caros = comparar = total = 0
while continuar == 'S':
    produto = input('\nnome do produto: ').strip().capitalize()
    valor = float(input('valor: '))
    total += valor
    if comparar == 0:
        comparar = valor
    if valor <= comparar:
        comparar = valor
        mais_barato = produto
    if valor >= 1000:
        caros += 1
    continuar = input('deseja continuar? [S/N]: ').strip().upper()[0]
print(f'''
total gasto: R&{total:.2f}
produtos que custam mais de R$ 1000,00: {caros}
mais barato: {mais_barato}''')
