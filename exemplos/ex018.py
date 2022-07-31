from math import (
    cos,
    tan,
    sin,
    radians
)
ang = float(input('digite um ângulo em rad: '))
ang = radians(ang)
print(f'o valor do seno de {ang:.2f} é {sin(ang):.2f}, seu cosseno é {cos(ang):.2f} e sua tangente é {tan(ang):.2f}')
