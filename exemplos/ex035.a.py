print('*'*20)
print('analisador de triângulos')
print('*'*20)
lado1 = float(input('digite o 1o lado: '))
lado2 = float(input('digite o 2o lado: '))
lado3 = float(input('digite o 3o lado: '))
if lado1 < lado3+lado2 and lado2 < lado3+lado1 and lado3 < lado1+lado2:
    print('poderá formar triângulo')
else:
    print('não poderá formar triângulo')