# 1. Escribe un programa Python que acepte el radio de un círculo del usuario y calcule el área. 

from math import pi

r = float(input('Escriba el radio del círculo: '))

area = pi * r ** 2 ** 2

print('El area del círculo es {0}'.format(area))