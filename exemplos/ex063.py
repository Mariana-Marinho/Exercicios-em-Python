"""
n primeiros termos da sequencia fibonacci
"""
print('SEQUÊNCIA FIBONACCI\n')
quantidade = int(input('digite quantos termos você deseja: '))
a = 0
b = 1
print(f'{a}, {b}', end=", ")
contador = 2
while quantidade > contador:
    fibonacci = a + b
    a = b
    b = fibonacci
    print(fibonacci, end=', ')
    contador += 1
print(f'são os {quantidade} primeiros termos da sequência fibonacci')
