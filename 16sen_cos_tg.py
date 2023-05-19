# exercício 16: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math
# from math import radians, sin, cos, tan

a = int(input('Ângulo: '))
x = math.radians(a)
s = math.sin(x)
c = math.cos(x)
t = math.tan(x)
print('Seno: {:.2f}'. format(s))
print('Cosseno: {:.2f}'. format(c))
print('Tangente: {:.2f}'. format(t))
