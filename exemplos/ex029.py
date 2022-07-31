velocidade = float(input('digite a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade-80)*7
    print(f'você ultrapassou o limite de velocidade, deverá pagar {multa:.2f} reais')
else:
    print('você dirigem bem')
