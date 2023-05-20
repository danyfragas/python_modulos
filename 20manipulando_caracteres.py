# exercício 20: Crie um programa que leia o nome completo de uma pessoa e mostre:
# 01. O nome com todas as letras maiúsculas e minúsculas.
# 02. Quantas letras ao todo (sem considerar espaços).
# 03. Quantas letras tem o primeiro nome.

nome = str(input('Insira o seu nome completo: ')).strip()

# 02
# nome1 = nome.split()
# nnome = ''.join(nome1)
# nnnome = len(nnome)

# 03
nome2 = nome.split()

print('Nome completo maiúsculo: {}\n'
      'Nome completo minúsculo: {}\n'
      'Quantidade de letras ao todo: {}\n'
      'Quantidade de letras no primeiro nome: {}'.format(nome.upper(), nome.lower(),
                                                         len(nome) - nome.count(' '), len(nome2[0])))
