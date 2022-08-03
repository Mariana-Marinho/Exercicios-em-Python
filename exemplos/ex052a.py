"""
Outro programa que checa se o número é primo
"""
num = int(input('digite um número: '))
c = 0
for i in range(1, num+1):
    if num % i == 0:
        print(f'\033[32m{i}\033[m', end=" ")
        c += 1
    else:
        print(f'\033[31m{i}\033[m', end=" ")
if c == 2:
    print(f'\no número {num} é primo')
else:
    print(f'\no número {num} não é primo, foi divisível {c} vezes')