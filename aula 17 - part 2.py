'''pessoas = [['pedro', 25], ['Joao', 32], ['Maria', 19]]

print(pessoas[1][1])
print(pessoas)

for nome in pessoas:
    print(f'{nome[0]} tem {nome[1]} anos de idade')'''

#Esse bloco são as listas compostas
galera = []
dado = []

#Esse bloco ler os dados e joga dentro da lista gelera
for c in range(0, 3):
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input("Digite sua idade: ")))
    galera.append(dado[:])
    dado.clear()

#Esse bloco organiza os dados em nome e idade
for nome in galera:
    print(f'{nome[0]} tem {nome[1]} anos de idade')