lados = input('digite os lados do triângulo: ')
lados = lados.split()
if len(lados) == 3:
    i = 0
    a = 0
    maior = 0
    while i < 3:
        if lados[a] >= lados[i]:
            maior = lados[a]
            m = a
            i += 1
        else:
            maior = lados[i]
            a = i
            m = 1
            i += 1
    i = lados.index(maior)
    c = len(lados)
    x = 0
    soma = 0
    while c > 0:
        if x != i:
            soma = soma+int(lados[x])
            x += 1

    if soma > int(maior):
        print(f'pode-se fazer um triângulo com lados menores valendo {soma} e o lado maior valendo {maior}')
    else:
        print(f'não se pode fazer um triângulo, pois {soma} não é maior que {maior}')
else:
    print('digite 3 lados')
