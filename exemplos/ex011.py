altura = float(input('digite a altura da sua parede: '))
largura = float(input('digite a largura da sua parede: '))
tinta = float(input('quantos m^2 sua tinta consegue pintar? '))
latas = altura*largura//tinta
# se precisar de parte de uma lata de tinta
if altura*largura % tinta != 0:
    latas += 1

print(f'a área da sua parede é {altura*largura}, assim, você precisará de {latas} latas de tinta')
