import tensorflow as tf
soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('\nVocê informou {} números Pares e a soma foi {}'.format(cont,  soma))