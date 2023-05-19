# exercício 15: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa

import math
# from math import hypot

x = float(input('Comprimento do cateto oposto: '))
y = float(input('Comprimento do cateto adjacente: '))
h = math.hypot(x, y)
# h = (x ** 2 + y ** 2) ** (1/2)
print('O comprimento é: {:.2f}'. format(h))
