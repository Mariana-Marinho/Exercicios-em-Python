"""
Ler nome, idade e sexo de 4 pessoas
1- imprimir o nome do homem mais velho
2- quantas mulheres tem menos de 20 anos
3- média de idade
"""
media = 0
idades = 0
c = 0
homem = []
mulheres = 0
for i in range(0, 4):
    nome = input('\ndigite o nome da pessoa: ')
    sexo = input('digite FEM para feminino ou MASC para masculino: ')
    idade = int(input('digite também sua idade: '))
    if idade >= 0:
        idades += idade
        if sexo.upper().find("MASC") != -1:
            if idade > c:
                c = idade
                homem = nome
        elif sexo.upper().find("FEM") != -1:
            if idade < 20:
                mulheres += 1
        else:
            print('digite ou MASC ou FEM')
    else:
        print('digite idades válidas')
media = idades/4
print(f'a média de idade do grupo é {media:.1f}')
if homem == "":
    print('não foram informados homens')
else:
    print(f'o homem mais velho é o {homem}')
if mulheres == 0:
    print('não foram informadas mulheres mais novas que 20 anos')
else:
    print(f'tem {mulheres} mulher(es) com menos de 20 anos')

