# exercício 24: Crie um programa que leia uma frase pelo teclado e mostre:
# 01. quantas vezes aparece a letra "A"
# 02. em que posição ela aparece a primeira vez
# 03. em que posição ela aparece a última vez

n = str(input('Frase: ')).strip().upper()
print('A frase "{}", possui as seguintes informações: \n'
      'A quantidade de vezes que a letra "A" aparece é: {}\n'
      'A posição que a letra "A" aparece pela primeira vez foi: {}\n'
      'A posição que a letra "A" aparece pela última vez foi: {}'. format(n, n.count('A'), n.find('A')+1, n.rfind('A')+1))
