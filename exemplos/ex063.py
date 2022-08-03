"""
n primeiros termos da sequencia fibonacci
"""
print('SEQUÊNCIA FIBONACCI\n')
n = int(input('digite quantos termos vocÊ deseja: '))
fibonacci = 0
c = 0
a = 0
b = 1
print('1', end=", ")
n -= 1
while n > c:
    fibonacci = a + b
    a = b
    b = fibonacci
    print(fibonacci, end=', ')
    c += 1
print(f'são os {n+1} primeiros termos da sequência fibonacci')
