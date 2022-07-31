salario = float(input('digite o seu salário: '))
if salario >= 1250:
    print(f'seu novo salário será {salario*110/100:.2f} reais')
else:
    print(f'seu novo salário será {salario*115/100:.2f} reais')
