n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m >= 7:
    print('Parabésns você foi aprovado, sua nota foi {}'.format(m))
else:
    print('Desculpa, você não conseguiu nota suficiente para passar, sua note foi {}'.format(m))