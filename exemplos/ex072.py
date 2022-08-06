"""
Programa que tenha uma tupla preenchida de 0 a 20, deve mostrar o número escolhido pelo usuário
"""
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    if escolha in range(0, len(numeros)):
        print(f'o número {escolha} por extenso é {numeros[escolha]}')
        break
    else:
        print('!!!digite um número válido!!!')
