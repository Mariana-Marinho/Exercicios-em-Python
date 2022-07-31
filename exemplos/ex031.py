distancia = float(input('digite a distância da sua viagem: '))
if distancia <= 200:
    custo = distancia*0.5
    print(f'você pagará {custo:.2f} reais')
else:
    custo = distancia*0.45
    print(f'você pagará {custo:.2f} reais')
