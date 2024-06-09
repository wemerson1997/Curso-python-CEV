from random import randint
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = computador + jogador
    tipo = ' '
    v = 0
    while tipo not in 'PI':
        tipo = str(input('Você quer Par ou ímpar [P/I]? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e computador jogou {computador}. Total de {total}')
    print('Deu par' if total % 2 == 0 else 'Deu ímpar ', end='')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU')
            v = v + 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('você VENCEU')
            v = v + 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente? ')
print(f'GAME OVER! Você venceu {v} vezes')