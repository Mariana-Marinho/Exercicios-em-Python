"""
Estruturas compostas:
    listas:
        recebe mais de um valor, pode mudar
"""

lista = ['mariana', 'marinho', 'da', 'silva', 'andrade']
print('meu nome é', lista)
# adicionar elemento no final da lista
lista.append('orleans bragança')
print('adicionando elemento no final:', lista)
# encaixar um elemento no meio da lista
lista.insert(2, 'oliveira')
print('encaixando no meio do nome:', lista)
# deletando índices de duas formas:
del lista[6]
# se o pop não receber parâmetro, deleta o último
lista.pop(2)
print('voltando ao normal:', lista)
# removendo pelo valor
lista.remove('da')
print('tirando o da:', lista)
print('em ordem alfabética:', sorted(lista))

lista_num = [9, 3, 5, 1, 7, 2]
print(f'lista de números: {lista_num}')
print(f'em ordem crescente: ', sorted(lista_num))
print(f'em ordem decrescente: {sorted(lista_num)[::-1]}')

lista_input = []
for c in range(0, 3):
    # preenchendo listas
    lista_input.append(int(input('digite um número:')))
print(lista_input)
# se igualar duas listas, a mudança em uma tb vai ser feita na outra
lista_input2 = lista_input
lista_input2[0] = 99999
print(lista_input, lista_input2)
# assim que se copia os valores:
lista_input2 = lista_input[:]
lista_input[0] = 0
print(lista_input, lista_input2)
