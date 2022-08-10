"""
Programa que conta a quantidade de vogais na palavra
"""
palavras = 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'FUTURA', 'PROGRAMADORA'
vogais = 'A', 'E', 'I', 'O', 'U'
for c in range(0, 6):
    print(f'\nna palavra {palavras[c]} tem as vogais:', end=' ')
    for i in range(0, 5):
        if vogais[i] in palavras[c]:
            print(vogais[i], end=' ')
