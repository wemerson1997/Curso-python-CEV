preco = float(input('Qual o valor do produto: '))
novo = preco+(preco*30/100)
print('O produto que custava R${} na promoção de 5% de desconto, agora está custando R${:.2f}'.format(preco, novo))