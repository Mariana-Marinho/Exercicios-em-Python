# programa que lê dois valores e mostre se são iguais ou qual o maior
num1 = float(input('digite um número qualquer: '))
num2 = float(input('digite outro número: '))
if num1 == num2:
    print('os números são iguais')
elif num1 > num2:
    print(f'o primeiro número {num1} é maior que o segundo {num2}')
else:
    print(f'o segundo número {num2} é maior que o primeiro {num1}')
