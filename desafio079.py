numeros = list()
while True:
    n = int(input("digite um número: "))
    if n not in numeros:
        numeros.append(n)
        print("Valor adcionaado com sucesso...")
    else:
        print("valor duplicado! Não vou adicionar...")
    r = str(input("Quer continuar? [S/N]"))
    if r in 'Nn':
        break
print('-='*30)
numeros.sort()
print(f'Você acionou os seguintes valores {numeros}')


'''lista = int(input('Digite um número: '))

num = 0
while lista != 0:
    num = 1
    lista = int(input('Digite outro número: '))


print(f'Os números digitados forma {lista}')'''