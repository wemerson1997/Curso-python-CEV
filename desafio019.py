from random import choice
n1 = str(input('Digite um nome: '))
n2 = str(input('Digite um nome: '))
n3 = str(input('Digite um nome: '))
lista = [n1, n2, n3]
escolhido = choice(lista)
print('O nome soretado foi {}'.format(escolhido))