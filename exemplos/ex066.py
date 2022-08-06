"""
Programa que lê int, só para quando o usuário digita 999, final mostrar quantos números digitados e a soma
"""
numeros = soma = 0
print('SOMANDO NÚMEROS, digite 999 para parar')
while True:
    digitado = int(input('digite um número inteiro: '))
    if digitado == 999:
        break
    soma += digitado
    numeros += 1
print(f'foram digitados {numeros} números, somando {soma}')
