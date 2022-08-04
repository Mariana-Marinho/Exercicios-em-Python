"""
Lê inteiros e só para quando lê 999, mostre quantos foram digitados e qual a soma
"""
soma = num = quant = 0
print('LENDO INTEIROS, digite 999 para sair\n')
while num != 999:
    num = int(input('digite um número inteiro: '))
    quant += 1
    soma += num
print(f'\na soma dos {quant} números digitados foi igual a {soma}')
