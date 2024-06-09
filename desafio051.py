from time import sleep
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('digite a razão: '))
decimo = primeiro + (10 - 1) * razao
print('Calculando a razão...')
sleep(2)
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')