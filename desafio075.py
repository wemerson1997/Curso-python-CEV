num = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
      int(input('Digite mais um número: ')), int(input('Digite o último número: ')))

print(f'Os valores digitados foram: {num}')
print(f'O valor 9 apareceu {num.count(9)}')
print(f'O valor 3 apareceu na {num.index(3)}ª posição')
print(f'Os valores pares digitados forma', end=' ')
for n in num:
    if n % 2 == 0:
        print(n)