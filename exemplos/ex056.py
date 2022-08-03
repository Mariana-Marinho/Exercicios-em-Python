"""
Ler nome, idade e sexo de 4 pessoas
1- imprimir o nome do homem mais velho
2- quantas mulheres tem menos de 20 anos
3- média de idade
"""
media = 0
soma = 0
c = 0
homem = ''
mulheres = 0
for i in range(1, 5):
    print(f' ----- {c}ª PESSOA -----')
    nome = input('\ndigite o nome da pessoa: ')
    sexo = input('digite F para feminino ou M para masculino: ')
    idade = int(input('digite também sua idade: '))
    soma += idade
    if sexo.upper().find("M") != -1 and idade > c:
        c = idade
        homem = nome
    elif sexo.upper().find("F") != -1 and idade < 20:
        mulheres += 1
media = soma/4
print(f'a média de idade do grupo é {media:.1f}')
if homem == "":
    print('não foram informados homens')
else:
    print(f'o homem mais velho é o {homem}')
if mulheres == 0:
    print('não foram informadas mulheres mais novas que 20 anos')
else:
    print(f'tem {mulheres} mulher(es) com menos de 20 anos')
