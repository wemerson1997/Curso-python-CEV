print('-'*40)
print('Lojão do wemerson')
print('-'*40)
total = totmil = menor = cont = 0

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Valor do produto: '))
    total = total + preco
    cont = cont + 1
    if preco > 1000:
        totmil = totmil + 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        break

print('-'*40)
print('{:-^40}'.format('Fim do prgrama'))
print(' O total de compras foi R${:.2f}'.format(total))
print('Temos {} produtos custando mais de R$1000.00'.format(totmil))
print(f'O produto mais barato custa R${menor:.2f}')
