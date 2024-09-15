'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

lista = []
pares = []
impares = []
while True:
    lista.append(int(input("Digite um valor: ")))
    resp = str(input("Quer continuar? "))
    if resp in 'Nn':
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print('-=' * 30)
print(f'A lista completa que vcê digitou foi:  {lista}')
print(f'A lista de pares completa que vcê digitou foi:  {pares}')
print(f'A lista completa de impares que vcê digitou foi:  {impares}')