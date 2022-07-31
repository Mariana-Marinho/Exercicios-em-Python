from datetime import date
ano = int(input('digita o ano aí para saber se ele é bissexto: '))
if ano % 100 == 0 and ano // 100 % 4 == 0 or ano % 400 == 0:
    print(f'o ano {ano} é bissexto !!')
else:
    print(f'esse ano {ano} não é bissexto não, vi')
print(f'aliás, hoje é o dia {date.today().day} do mês {date.today().month} de {date.today().year}')
