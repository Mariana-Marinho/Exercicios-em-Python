# calcular o IMC
peso = float(input('digite seu peso em kg: '))
altura = float(input('digite sua altura em metros: '))
imc = peso/(altura**2)
"""match imc:
    case imc < 18.5:
        print('você está abaixo do peso ideal')
    case 18.5 <= imc < 25:
        print('você está no peso ideal')
    case 25 <= imc < 30:
        print('você está acima do peso ideal')
    case 30 <= imc < 40:
        print('você está obeso')
    case imc >= 40:
        print('SE CUIDE!!! VOCÊ ESTÁ OBESO MÓRBIDO!!!')
"""
if imc < 18.5:
    print(f'você está abaixo do peso ideal, imc={imc:.1f}')
elif imc < 25:
    print(f'você está no peso ideal, imc={imc:.1f}')
elif imc < 30:
    print(f'você está acima do peso ideal, imc={imc:.1f}')
elif imc < 40:
    print(f'você está obeso, imc={imc:.1f}')
elif imc >= 40:
    print(f'SE CUIDE!!! VOCÊ ESTÁ OBESO MÓRBIDO!!! imc={imc:.1f}')
