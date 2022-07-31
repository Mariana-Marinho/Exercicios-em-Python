num = input('digite um número entr 0 e 9999\n')
i = len(num)
print(f'temos {i} classes ao total\n')

print('unidade: ', num[i-1])

if i >= 2:
    print('dezena: ', num[i-2])

if i >= 3:
    print('centena: ', num[i-3])

if i >= 4:
    print('milhar: ', num[i-4])
