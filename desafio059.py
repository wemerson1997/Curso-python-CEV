n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} mais {} é igua a {}'.format(n1, n2, soma))
    elif opcao == 2:
        resultado = n1 * n2
        print('O valor da multiplicação é de {}'.format(resultado))

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
    elif opcao == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opcao ==5:
        print('Finalizando programa...')
print('Fim do programa! Volte sempre!')
