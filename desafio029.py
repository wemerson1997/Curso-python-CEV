v1 = float(input('Qual a sua velociade atual? '))
if v1 > 80:
    print('MULTADO! Você excedeu o limite permitido que de 80km/h')
    multa = (v1-80)*7
    print('Você devepagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança')