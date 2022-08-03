"""
Programa que mostra 10 primeiros termos de uma pa, e pergunta quantos mais mostrar
"""
primeiro = float(input('digite o primeiro termo de uma p.a.: '))
razao = float(input('digite sua razão: '))
x = 1
while x <= 10:
    progressao = primeiro + (x-1)*razao
    print(progressao, end=", ")
    x += 1
print('são os primeiros termos da p.a. informada')
continuar = input('você deseja saber mais termos? digite S/N: ').upper()
if continuar == 's':
    c = 1
    escolha = int(input('quantos termos a mais você quer? '))
    while c <= escolha:
        progressao = primeiro + ((c+10) - 1) * razao
        print(progressao, end=", ")
        c += 1
    print(f'são os {escolha} termos após o 10º')
elif continuar == 'n':
    print('obrigada!')
