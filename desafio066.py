soma = 0
quant = 0
while True:
    n = int(input('Digite um valor (999 para parar) : '))
    if n == 999:
        break
    soma = soma + n
    quant = quant + 1
print(f'As soma dos {quant} foi {soma}')