dias = int(input('digite por quantos dias você alugou o carro: '))
km = float(input('digite quantos km você percorreu: '))

preco = dias*60 + km*0.15

print(f'você deve pagar R${preco:.2f}')
