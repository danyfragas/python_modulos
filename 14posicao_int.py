# exercício 14: Crie um programa que leia um nº real qualquer pelo teclado e mostre na tela a sua posição inteira

from math import trunc

n = float(input('Número: '))
print('A posição inteira de {} é {}'. format(n, trunc(n)))
#print('A posição inteira de {} é {}'. format(n, int(n)))
