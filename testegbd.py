
while True:
    nome = str(input('Digite um nome: '))
    if nome == 'wemerson':
        print('Você digitou {}'.format(nome))
        print('-=-' * 20)
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()
        print('-=-' * 20)
        if continuar == 'N':
            break
    else:
        print('Tente novamente')

