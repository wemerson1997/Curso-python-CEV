numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

maior = numero1
menor = numero1

if numero2 > maior:
  maior = numero2

if numero3 > maior:
  maior = numero3

if numero2 < menor:
  menor = numero2

if numero3 < menor:
  menor = numero3

print("\033[4;30;43O maior número é\033[m", maior)
print("O menor número é", menor)
