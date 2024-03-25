comprimento = float(input('Coloqque o comprimento do aposento: '))
largura = float(input('Coloque a largura do aposento: '))
area = ((largura * 2.8) * 2) + ((comprimento * 2.8) * 2) - (0.8 * 2.1)
litros = area / 3
latas18 = int(litros // 18)
galoes = int((litros % 18) // 3.7)
latas1 = (litros % 18) % 3.7

if (latas1 > 0 and latas1 < 0.5) or (latas1 > 1 and latas1 < 1.5) or (latas1 > 2 and latas1 < 2.5):
    latas1 = round(latas1 + 1)
else:
    latas1 = round(latas1)

print('A quantidade de Baldes de tinta necessário é:', latas18, 'latas de 18 Litros,', galoes, 'latas de 3,7 Litros e', latas1, 'latas de um litro.')
