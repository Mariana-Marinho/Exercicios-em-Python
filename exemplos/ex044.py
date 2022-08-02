"""
Programa que calcula o valor a ser pago considerando a condição de pagamento
"""
preco = float(input('Digite o preço original do produto: '))
forma = int(input('Digite 1 para pagamento a vista e 2 para pagamento parcelado: '))
if forma == 1:
    avista = int(input('digite 1 para a cartão ou 2 para dinheiro/cheque: '))
    if avista == 1:
        preco = preco*0.95
        print(f'você pagará {preco:.2f}')
    elif avista == 2:
        preco = preco*0.9
        print(f'você pagará {preco:.2f}')
    else:
        print('digite um número válido')
elif forma == 2:
    parcela = int(input('em quantas parcelas você pretende pagar? '))
    if parcela < 3:
        parcela = preco/parcela
        print(f'você pagará {parcela:.2f} por parcela')
    elif parcela >= 3:
        preco = preco*1.2
        parcela = parcela/preco
        print(f'você pagará {parcela:.2f} por parcela')
    else:
        print('digite um número válido')
else:
    print('digite um número válido')
