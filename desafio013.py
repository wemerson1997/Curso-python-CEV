salario = float(input('Qual o valor do produto: '))
novo = salario+(salario*15/100)
print('O seu salário era de R${} com o aumento de 15%, agora é R${:.2f}'.format(salario, novo))