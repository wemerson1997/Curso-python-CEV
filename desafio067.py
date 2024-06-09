'''while True:
    num = int(input('Digite um valor: '))
    if num < 0:
        break
    cont = 0
    print('-=-'*20)
    while cont <= 10:
        tabuada = num * cont
        print(f' {num} x {cont} = {tabuada}')
        cont = cont + 1
    print('-=-'*20)
print('Tabuada encerrada')'''

while True:
    num = int(input('Digite um valor: '))
    print('-=-'*20)
    if num <0:
        break
    for c in range(1, 11):
        valor = num * c
        print(f'{num} x {c} = {valor}')
    print('-=-'*20)
print('TABUADA ENCERRADA')