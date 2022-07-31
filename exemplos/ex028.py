from random import randint
from time import sleep
num = randint(1, 5)
cores = {
    'roxo': '\033[34m',
    'limpa': '\033[m'
}
print(cores['roxo'], '*'*12, cores['limpa'])
palpite = int(input(' tente adivinhar o número que eu escolhi: '))
print(cores['roxo'], '*'*3, 'PERAÍ', '*'*3, cores['limpa'])
sleep(1)

if palpite == num:
    print('meus parabéns!!! você acertou')
else:
    print('vishhh errou')
