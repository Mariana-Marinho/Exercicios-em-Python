"""
Programa que mostra 10 primeiros termos de uma pa, e pergunta quantos mais mostrar
"""
primeiro = float(input('digite o primeiro termo de uma p.a.: '))
razao = float(input('digite sua razão: '))
c = int(input('quantos termos você deseja? '))
continuar = 'S'
x = 0
while x <= c and continuar == 'S':
    progressao = primeiro + x*razao
    print(progressao, end=" -> ")
    x += 1
    if x == c:
        continuar = input('você deseja saber mais termos? digite S/N: ').upper()[0]
        if continuar == 'S':
            amais = int(input('quantos termos a mais você quer? '))
            c = x + amais
        else:
            break
print('obrigada')
