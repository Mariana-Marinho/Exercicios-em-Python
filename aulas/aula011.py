# cores no terminal
'''
padrão ANSI:
padrão de normalização internacional
-> começa com contrabarra e um código
sempre que quiser começar uma cor você põe:
    \033[style:text:backm
entre o [ e o m você põe o código, com o valor do estilo (0 none, 1 bold, 4 underline, 7 negative),
do texto (de 30 a 37) e do fundo (40 a 47)
text        back
30 white     40
31 red       41
32 green     42
33 yellow    43
34 blue      44
35 purple    45
36 turquoise 46
37 grey      47
'''
print('\033[0:30:41mMariana')
print('\033[mMariana')
print('\033[7:30mMariana')
print('\033[1:34:45mMariana\033[m')
print('\033[36mMariana \033[33mMarinho \033[35mda \033[32mSilva \033[34mAndrade')
nome = 'Mariana Marinho'
print(f'\033[4:36m{nome}\033[m')
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print(cores['pretoebranco'], f'{nome}', cores['limpa'])
