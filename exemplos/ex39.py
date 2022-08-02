# ler o ano de nascimento de alguém e informar a situação de alistamento no exército
from datetime import date

ano_nasc = int(input('digite o ano de nascimento do jovem: '))
idade = date.today().year-ano_nasc
if idade == 18:
    print('você deve se alistar no exército!')
elif idade > 18:
    ano = date.today().year - idade - 18
    print(f'você deveria se alistar há {idade-18} anos, em {ano}')
else:
    ano = date.today().year + 18 - idade
    print(f'voce deve aguardar {18-idade} anos para se alistar, no ano {ano}')
