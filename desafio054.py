from datetime import date
atual = date.today().year
totmenor = 0
totmaior = 0
for pess in range(1, 8):
    nascimento = int(input('em que ano a {}ª pessoa nasceu?'.format(pess)))
    idade = atual - nascimento
    if idade >= 21:
        totmenor += 1
    else:
        totmaior += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))