"""
Programa que mostre a contagem regressiva de 10 a 0 com pausa de 1 segundo
"""
from time import sleep
import emoji
print(emoji.emojize(':fireworks::fireworks::fireworks:CONTAGEM DE ANO NOVO!:fireworks::fireworks::fireworks:'))
sleep(1)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize(":fireworks::fireworks::fireworks:FELIZ ANO NOVOOO:fireworks::fireworks::fireworks:"))
