# exercício 21: Crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados (Unidade, Dezena, Centena e Milhar)

num = int(input('Informa o número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O número {}, possui: '
      '\n Unidade: {} '
      '\n Dezena: {} '
      '\n Centena: {} '
      '\n Milhar: {}'. format(num, u, d, c, m))
