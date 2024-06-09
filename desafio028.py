from random import randint
from time import sleep
notebook = randint(0,10) # faz o computador pensar
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10,tente acertar!')
print('-=-'*20)
jogador = int(input('em que número pensei?')) #Jogador tenta adivinhar
print('Processadno...')
sleep(3)
if jogador == notebook:
    print('Parabéns! você acertou')
else:
    print('Ganhei! eu pensei no númro {} e não no {}'.format(notebook, jogador))
print('Pensei em {}'.format(notebook))