# exercício 17: Um professor quer sortear um dos seus quatro alunos p/ apagar o quadro. Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido

# import random
from random import choice

a = str(input('Nome do aluno 1 : '))
b = str(input('Nome do aluno 2 : '))
c = str(input('Nome do aluno 3 : '))
d = str(input('Nome do aluno 4 : '))
alunos = [a, b, c, d]
# sorteio = random.choice(alunos)
sorteio = choice(alunos)
print('O aluno sorteado foi: {}'. format(sorteio))
