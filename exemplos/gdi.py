oficial = list()
oficialusuario = list()
contdeqnumeros = list()
extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco'


def tracos():
    print('---' * 30)


def usuario():
    listausuario = list()
    listausuario.clear()
    qnumeros = str(input('▪ Quantos números deseja cadastrar? '))
    while not qnumeros.isnumeric():
        qnumeros = str(
            input('Apenas números são aceitos\n▪ Quantos números deseja cadastrar? '))
    qnumeros = int(qnumeros)
    while qnumeros < 0:
        qnumeros = int(
            input('▪ Digite apenas valores positivos.\nQuantos números deseja cadastrar? '))
    if qnumeros == 0:
        print('Nenhum valor cadastrado.')
        contdeqnumeros.append(qnumeros)
    if qnumeros > 0:
        for cadastro in range(0, qnumeros):
            numero = str(input(f'Digite o {cadastro + 1}ª valor: '))
            while not numero.isnumeric():
                numero = str(
                    input(f'Apenas números são aceitos.\nDigite o {cadastro + 1}ª valor: '))
            numero = int(numero)
            if numero not in listausuario:
                listausuario.append(numero)
            else:
                while numero in listausuario:
                    numero = str(
                        input('Esse valor já foi adicionado. Digite outro valor: '))
                    while not numero.isnumeric():
                        numero = str(
                            input('Apenas números são aceitos.\nDigite outro valor: '))
                    numero = int(numero)
                else:
                    listausuario.append(numero)
        oficialusuario.append(listausuario[:])
        print(f'▪ Os valores da sua lista são:', end=' ')
        for dissecar in listausuario:
            print(f'{dissecar}', end=' ')
        print()


def sorteando():
    from random import randint
    from time import sleep
    temp = list()
    temp2 = list()
    resultados = str(input('▪ Deseja quantos resultados ? '))
    while not resultados.isnumeric():
        resultados = str(
            input('Apenas números são aceitos.\n▪ Deseja quantos resultados? '))
    resultados = int(resultados)
    tracos()
    for sorteio in range(0, resultados):
        temp.clear()
        for x in range(0, randint(1, 6)):
            var = randint(0, 10)
            if var not in temp:
                temp.append(var)
        print(f'▪ "Sorteando" {extenso[len(temp)]}', ('valores da' if len(temp) > 1 else "valor da"),
              f'{sorteio + 1}ªlista: ', end='')

        for lista in temp:
            print(f'{lista}', end=' ')
        print()
        temp2.append(temp[:])
    oficial.append(temp2[:])
    if resultados > 0:
        print('▪ ANALISANDO A SOMA DOS VALORES PARES DE CADA LISTA ▪')
        sleep(1)
        for time in range(5, 0, -1):
            print(f'{time:>2}', '...' if time > 1 else '.', end=' ')
            sleep(1)
        print()
    else:
        print(f'Não é possível retornar {resultados} resultados.')


def somapares(lista):
    cont = 0
    for par in lista:
        pares = 0
        cont += 1
        for numero in par:
            if numero % 2 == 0:
                pares += numero
        print(
            f'▪ Somando os valores pares da {cont}ª lista: {tuple(par)} resultado: ', end='')
        print(pares)


def somaimpar(lista):
    cont = 0
    for impar in lista:
        impares = 0
        cont += 1
        for numero in impar:
            if numero % 2 != 0:
                impares += numero
        print(
            f'▪ Somando os valores ímpares da {cont}ª lista: {tuple(impar)} resultado: ', end='')
        print(impares)


# Essa indentação é muito importante pro funcionamento do scrpit.


while True:
    print(f"\n{'FUNÇÕES PARA SORTEAR E SOMAR'.rjust(55)}")
    tracos()
    sortear = str(input(
        f'▸[1] Sortear números aleatoriamente.\n▸[2] Acrescentar meus números.\n▪ Digite: '))
    while not sortear.isnumeric():
        sortear = str(input(
            f'Apenas números são aceitos.\n▸[1] Sortear números aleatoriamente.\n▸[2] Acrescentar meus números.\n▪ '
            f'Digite: '))
    sortear = int(sortear)
    while sortear <= 0 or sortear > 2:
        sortear = str(input('▪ Escolhe apenas as opções diposníveis: '))
        while not sortear.isnumeric():
            sortear = str(
                input('Apenas números são aceitos.\n▪ Escolha apenas as opções diposníveis: '))
        sortear = int(sortear)
    if sortear == 1:
        sorteando()
        for menosuma in oficial:
            oficial = menosuma
        if oficial:
            somapares(oficial)
            tracos()
            somaimpar(oficial)
        else:
            print(f"Não há valores a serem somados.")
    if sortear == 2:
        usuario()
        menosusuario = []
        for menosum in oficialusuario:
            menosusuario = menosum
        if menosusuario != [] and contdeqnumeros != [0]:
            somapares(oficialusuario)
            tracos()
            somaimpar(oficialusuario)
        else:
            if contdeqnumeros == [0] or menosusuario == []:
                print(f"Não há valores a serem somados.")
        contdeqnumeros.clear()
    quer = str(input('● Deseja continuar? [S/N]: '))[0].upper()
    while quer not in 'SN':
        quer = str(input('▪ Digite apenas [S/N]: '))[0].upper()
    if quer == 'N':
        break
tracos()
print("▪ PROGRAMA ENCERRADO ▪")
