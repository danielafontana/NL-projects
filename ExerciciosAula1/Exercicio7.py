# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

import math

lado = float(input("Digite o lado do quadrado:"))

area = lado * 4

area_dobro = math.pow(area, 2)

print("A área do quadrado é: {:.2f}".format(area))
print("O dobro da área do quadrado é {:.2f}".format(area_dobro))
