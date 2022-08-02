# receber 3 lados e informar se pode se formar triângulos, se sim, qual o tip
lado1 = float(input('digite um lado do triângulo: '))
lado2 = float(input('digite outro lado do triângulo: '))
lado3 = float(input('digite o terceiro lado: '))
lados = [lado1, lado2, lado3]
# pôr a lista em ordem crescente para facilitar
lados = sorted(lados)
print(f'{lados[2]} é o maior lado')
if lados[2] < lados[0]+lados[1]:
    print('pode formar triângulo!')
    if lados[0] == lados[1] == lados[2]:
        print('formará um triângulo equilátero')
    elif lados[0] == lados[1] or lados[1] == lados[2]:
        print('formará um triângulo isósceles')
    else:
        print('formará um triângulo escaleno')
else:
    print('não poderá formar triângulo')
