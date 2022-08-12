"""
Expressão matemática com () e analisar se está na ordem correta
"""
expressao = str(input('digite uma expressão numérica: '))
if expressao.find('(') > expressao.find(')'):
    print('expressão não válida, ")" antes de "(" ')
elif expressao.count('(') == expressao.count(')'):
    print('expressão válida')
else:
    print('expressão não válida, não fechou os parênteses')
