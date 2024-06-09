from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
novo = atual - ano
print('O atleta tem {} anos.'.format(novo))
if novo <= 9:
    print('Classificação: MIRIM')
elif novo > 9 and novo <= 14:
    print('Classificação: INFANTIL')
elif novo > 14 and novo <= 19:
    print('Classificação: JUNIOR')
elif novo > 19 and novo <= 25:
    print('Classificação: SÊNIOR')
elif novo > 25:
    print('Classificação: MASTER')