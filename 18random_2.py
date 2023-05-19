# exercício 18: O mesmo professor do exercício 17 quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

# import random
from random import shuffle

a = str(input('Nome do aluno 1 : '))
b = str(input('Nome do aluno 2 : '))
c = str(input('Nome do aluno 3 : '))
d = str(input('Nome do aluno 4 : '))
alunos = [a, b, c, d]
shuffle(alunos)
print('Ordem de apresentação: ', alunos)
