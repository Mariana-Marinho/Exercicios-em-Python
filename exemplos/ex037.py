"""
Programa que converte um inteiro a um binário/octal/hexadecimal
"""
print('\n\nCONVERTENDO INTEIROS PARA BIN/OCT/HEX\n\n')
numero = int(input('digite um número inteiro para fazer a conversão: '))
base = int(input("""escolha a base escolhida de acordo com: 
( 1 ) para binário
( 2 ) para octal
( 3 ) para hexadecimal
escolha: """))
if base == 1:
    numero = bin(numero)
    # tirando o 0b do início
    print(f'o número informado convertido em binário fica: {numero[2:]}')
elif base == 2:
    numero = oct(numero)
    # tirando o 0o do início
    print(f'o numero informado convertido em octal fica: {numero[2:]}')
elif base == 3:
    numero = hex(numero)
    # tirando o 0h do início
    print(f'o número informado convertido em hexadecimal fica: {numero[2:]}')
else:
    print('digite um número válido')
