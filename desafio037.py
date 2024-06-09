numero = int(input("Digite um número inteiro: "))

opcao = int(input("Escolha a base de conversão: \n1 - Binário\n2 - Octal\n3 - Hexadecimal\n"))

if opcao == 1:
    print("O número {} em binário é: {}".format(numero, bin(numero)[2:]))
elif opcao == 2:
    print("O número {} em octal é: {}".format(numero, oct(numero)[2:]))
elif opcao == 3:
    print("O número {} em hexadecimal é: {}".format(numero, hex(numero)[2:]))
else:
    print("Opção inválida.")
