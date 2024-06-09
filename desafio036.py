valor_casa = float(input("Informe o valor da casa: R$ "))
salario = float(input("Informe o salário: R$ "))
anos = int(input("Informe em quantos anos será pago: "))

prestacao_mensal = valor_casa / (anos * 12)

if prestacao_mensal > (salario * 30) / 100:
    print("Empréstimo negado. A prestação mensal não pode exceder 30% do salário.")
    print('A prestação do seu financiamento será de R${:.2f}'.format(prestacao_mensal))
else:
    print("Empréstimo aprovado. A prestação mensal será de R$ {:.2f} por mês.".format(prestacao_mensal))
