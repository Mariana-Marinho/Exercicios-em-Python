# programa que calcula a média
nota1 = float(input('digite sua primeira nota: '))
nota2 = float(input('digite sua outra nota: '))
media = (nota1+nota2)/2
if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    if media < 5:
        print(f'infelizmente sua nota foi muito baixa, tirou {media:.1f}... você foi reprovado.')
    elif 5 <= media < 7:
        print(f'sua média foi {media:.1f}, você ficou de recuperação, estude mais!')
    else:
        print(f'MEUS PARABÉNS! Você passou por média, tirou {media:.1f}')
else:
    print('digite notas válidas')
