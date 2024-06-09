dias = int(input('Quantos dias você alugou?'))
km = float(input('Quantos KM você rodou?'))
pago = ((dias * 60)+ km * 0.15)
print('o total a pagar é de R${:.2f}'.format(pago))