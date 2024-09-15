galera = []
dado = []

while True:
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input("Digite seu peso: ")))
    galera.append(dado[:])
    dado.clear()
    resp = str(input("Quer continuar? "))
    if resp in 'Nn':
        break
print(f'Ao todo, você cadastrou {len(galera)} pessoas')
print(f'O mario peso foi de {max(galera)}')