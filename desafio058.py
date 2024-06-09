from random import randint

numero = randint(1, 10)
guess = 0
palpite = 0
print('-=-' * 20)
print('Vamos brincar um pouco. Tente acertar um número')
print('-=-' * 20)

while guess != numero:
    guess = int(input('tente advinhar um número:'))
    palpite = palpite + 1
    if guess < numero:
        print('tente um número maior.')
    elif guess > numero:
        print('tente um número menor.')
print('parabéns você acertou! você tentou {} vez até acertar'.format(palpite))