"""
testar se o site está acessível na máquina usada
"""
import urllib.request

try:
    urllib.request.urlopen('http://pudim.com.br/')
    print('consegui acessar')
except Exception as erro:
    print(f'deu erro: {erro}')
