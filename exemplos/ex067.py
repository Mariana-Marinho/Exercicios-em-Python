"""
mostrar a tabuada de vários números, interromper quando ler um negativo
"""
num = c = 1
while num >= 1:
    num = int(input(f'tabuada do número: '))
    print('_' * 20)
    while num >= 1 and c <= 10:
        tabuada = num*c
        print(f'{num:3} x {c:2} = {tabuada:3}')
        c += 1
    print('_'*20)
    c = 1
print('tabuada finalizada.')
