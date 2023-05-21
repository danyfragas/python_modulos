# exercício 25: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Insira o nome completo: ')).strip()
nome = n.split()
print('Primeiro nome: {}\n'
      'Último nome: {}'. format(nome[0], nome[len(nome)-1]))
