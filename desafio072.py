cont = ('zero', 'um', 'dois', 'três',
        'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze',
        'quatorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
        num = int(input('Digite um número: '))
        if 0 <= num <= 20:
                print('Você digitou o número {}'.format(num))
                print('-=-'*20)
                continuar = str(input('Quer continuar? [S/N]')).strip().upper()
                print('-=-' * 20)
                if continuar == 'N':
                        break
        else:
                print('tente novamente')
print('O programa acabou! Obrigado!')
