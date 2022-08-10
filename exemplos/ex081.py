"""
Programa que lê números e coloca em lista, mostrar:
A) quantos números foram digitados
B) ordem decrescente
C) se 5 foi digitado
"""
lista = []
while True:
    lista.append(input('digite um valor: '))
    escolha = input('deseja continuar? [S/N]: ').upper()[0]
    if escolha == 'N':
        break
    elif escolha != 'S':
        print('preste atenção no que você digita')
print(f'A) lista em ordem decrescente: {sorted(lista)[::-1]}')
print(f'B) você digitou {len(lista)} números')
if 5 in lista:
    print(f'C) o número 5 foi digitado')
else:
    print(f'C) 5 não foi digitado')
