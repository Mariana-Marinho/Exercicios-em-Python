"""
ler valores diferentes e mostrá-los em ordem crescente
"""
numeros = []
while True:
    num = int(input('\ndigite um número: '))
    if num in numeros:
        print('digite um valor diferente')
    else:
        numeros.append(num)
    escolha = input('deseja continuar? [S/N]: ').upper()[0]
    if escolha == 'N':
        break
    elif escolha != 'S':
        print('preste atenção no que você digita')
numeros.sort()
print(f'\n\nvocê digitou os números {numeros}')
