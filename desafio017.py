from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento docateto adjacente: '))
hi = hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))
