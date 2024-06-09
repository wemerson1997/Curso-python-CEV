from time import sleep
r1 = float(input('Digite um valor: '))
r2 = float(input('Digite outro valor: '))
r3 = float(input('Digite outro valor: '))
print('Calculando...')
sleep(2)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos podem formar um triângulo')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM triângulo')
