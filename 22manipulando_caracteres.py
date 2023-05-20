# exercício 22: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

n = str(input('Insira o nome da cidade: ')).strip()
nn = n.split()
nnn = 'Santo' in nn[0]
print('Santo é a primeira palavra da frase?\n {}'. format(nnn))
