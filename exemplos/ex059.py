"""
Programa que lê dois valores e mostre o menu:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
"""
escolha = 0
while operacao != 5:
    numero1 = float(input('\ndigite o primeiro número: '))
    numero2 = float(input('digite o segundo número: '))
    operacao = int(input('''\n
    MENU:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    
sua escolha: '''))
    if operacao == 1:
        print(f'{numero1} + {numero2} = {numero2+numero1}')
    elif operacao == 2:
        print(f'{numero1} x {numero2} = {numero2*numero1}')
    elif operacao == 3:
        if numero1 > numero2:
            print(f'{numero1} é maior que {numero2}')
        elif numero2 > numero1:
            print(f'{numero2} é maior que {numero1}')
        else:
            print('os números são iguais')
    elif operacao == 5:
        print('\nprograma finalizado')
        break
