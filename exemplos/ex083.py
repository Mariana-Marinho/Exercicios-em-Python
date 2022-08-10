"""
Expressão matemática com () e analisar se está na ordem correta
"""
expressao = str(input('digite uma expressão numérica: '))
if expressao.count('(') == expressao.count(')'):
    print('expressão válida')
else:
    print('expressão não válida')
