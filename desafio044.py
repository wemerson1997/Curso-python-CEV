from time import sleep
print('=========LOJAS SILVA=======')
preco = float(input('Preço das compraras: R$ '))
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
forma = int(input('Qual a sua opção? '))
if forma == 1:
    valor = (10*preco) / 100
    npreco = preco - valor
    print('Sua compra de {:.2f} vai custar R${:.2f} no final'.format(preco, npreco))
elif forma == 2:
    valor = (5*preco) / 100
    npreco = preco - valor
    print('Sua compra de {:.2f} vai custar R${:.2f} no final'.format(preco, npreco))
elif forma ==3:
    parcela = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(parcela))
elif forma == 4:
    quan = int(input('Quantas Parcelas? '))
    juros = (20 * preco) / 100
    valorfinal = preco + juros
    parcelas = valorfinal / quan
    print('Sua compra será parcelada em {}x de R${:.2f} com JUROS'.format(quan, parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, valorfinal))
else:
    preco = 8
    print('Opção inválida! Tente novamente')


