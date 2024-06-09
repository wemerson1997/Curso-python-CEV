from math import sin, cos, tan,radians
valor = float(input('Digite o ângulo que você desja: '))
conv = radians(valor)
seno = sin(conv)
coseno = cos(conv)
tangente = tan(conv)
print('O ângulo de {} tem o SENO de {:.2f}'.format(valor, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(valor, coseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(valor, tangente))
