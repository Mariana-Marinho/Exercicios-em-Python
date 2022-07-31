# fatiamento de uma string
frase = 'mariana marinho da silva andrade'

print(f'o nome é "', frase, f'" e o caractere 10 é o {frase[9]} e a primeira linha é {frase[0:7]}, '
    f' pulando de 2 em 2 é {frase[0:7:2]}, do meio pro final é {frase[6:]}')

print(f'o nome tem {len(frase)} caracteres')

print(f'a frase tem', frase.count('a'), 'vezes a letra a ao todo e',
      frase.count('a', 0, 15), 'vezes do começo para o meio')

print('existe a palavra mari nesse nome: ', 'mari' in frase)

# não tem como mudar sem usar o replace; a mudança só vai ser salva se você usar frase = frase.replace('algo', 'alguma')
print(f'substitua andrade por orleans bragança: ', frase.replace('andrade', 'orleans bragança'))

print(f'agora todo em maiúsculo:', frase.upper())

print(f'tudo em minúsculo: ', frase.lower())

print(f'capitalizado:', frase.capitalize(), 'em título:', frase.title())

# print('sem espaços: ', frase.strip())

# print('lista com os nomes separados: ', frase.split())

dividido = frase.split()

print('agora a 3a letra do 2o nome: ', dividido[1][2])
