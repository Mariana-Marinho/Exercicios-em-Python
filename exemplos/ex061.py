"""
1o termo e razão de uma p.a. e mostrar os 10 primeiros termos
"""
primeiro = float(input('digite o primeiro termo de uma p.a.: '))
razao = float(input('digite sua razão: '))
x = 1
while x <= 10:
    progressao = primeiro + (x-1)*razao
    print(progressao, end=", ")
    x += 1
print('são os primeiros termos da p.a. informada')
