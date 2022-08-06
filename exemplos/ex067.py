"""
mostrar a tabuada de vários números, interromper quando ler um negativo
"""
while True:
    num = int(input(f'tabuada do número: '))
    print('_' * 20)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num:3} x {c:2} = {(num*c):3}')
    print('_'*20)
print('tabuada finalizada.')
