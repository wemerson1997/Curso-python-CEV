from time import sleep
print('-=-'*20)
print('MÉDIA DO ALNO')
print('-=-'*20)
sleep(1)

n1 = float(input('Primeira nota: '))
n2 = float(input('segunda nota: '))
media = (n1 + n2) /2
if media < 5:
    print('Seu aluno está reprovado')
    print('Media é de {}'.format(media))
elif media >= 5.0 and media <7:
    print('Seu aluno está de recuperação')
    print('media é de {}'.format(media))
elif media >= 7.0:
    print('Parabéns, seu aluno está aprovado')
    print('Sua média é de {}'.format(media))