salario = float(input('Qual o valor do seu salário? R$ '))
if salario >= 1250:
    aumento = (10 * salario) / 100 + salario
    print('Seu aumento foi de 10% e seu novo salário é de R${:.2f}'.format(aumento))
else:
    aumento = (15 * salario / 100) + salario
    print('\033[0;32;40mSeu aumento foi de de 15% e seu novo salário é de R${:.2f}\033[m'.format(aumento))


