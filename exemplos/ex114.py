"""
testar se o site está acessível na máquina usada
"""
import urllib.request
import urllib

try:
    urllib.request.urlopen('http://pudim.com.br/')
except:
    print(f'no momento site não está acessível')
else:
    print('consegui acessar')
