from time import sleep


def contador(inicio, fim, passo):
    print(f'contagem de {inicio} a {fim}, pulando de {passo} em {passo}')
    passo = abs(passo)
    if passo == 0:
        passo = 1
    if inicio < fim:
        c = i
        while c <= fim:
            print(c, end=' ')
            sleep(0.5)
            c += passo
    else:
        c = i
        while c >= fim:
            print(c, end=' ')
            sleep(0.5)
            c -= passo


i = int(input('início: '))
f = int(input('fim: '))
p = int(input('pular: '))
contador(i, f, p)
