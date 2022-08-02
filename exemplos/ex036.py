"""
Programa para aprovar empréstimo bancário
recebe o valor da casa, o salário e quantos anos de pagamento
a prestação mensal não pode exceder 0,3 do valor do salário
"""
print('CALCULANDO SEU EMPRÉSTIMO BANCÁRIO')
casa = float(input('digite o preço da casa: '))
salario = float(input('digite o valor de seu salário: '))
anos = int(input('digite em quantos anos você vai pagar: '))
prestacao = casa / (anos*12)
print(f'para pagar uma casa de R${casa:.2f}, seriam necessárias {anos*12} parcelas de {prestacao:.2f} reais')
if prestacao <= 0.3*salario:
    print(f'seu empréstimo foi aprovado')
else:
    print('infelizmente, seu empréstimo foi negado...')
