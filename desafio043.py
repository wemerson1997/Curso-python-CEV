from time import sleep
peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m)'))
imc = peso / (altura ** 2 )
print('Seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Obesiidade')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
