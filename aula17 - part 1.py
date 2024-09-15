'''num = [2, 5, 9, 1]
if 5 in num:
    num.remove(5)
else:
    print('O valor 5 não está')
print(f'Essa lista tem {len(num)} elementos {num}')'''

'''valores = list()
valores.append(5)
valores.append(6)
valores.append(9)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print(f'Cheguei ao final da lista')'''

'''valores = []

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print(f'Cheguei ao final da lista')'''

a = [2, 3, 4, 7]
b = a[:]
b[2]=8
print(f' A lista A: {a}')
print(f'A lista B: {b}')