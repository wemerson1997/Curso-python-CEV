palavras = ("cachorro", "livro", "montanha", "lapis",
            "teclado", "carro", "sol", "festa", "jardim", "relógio")

for p in palavras:
    print(f'\n Na palavra {p. upper()} temos - ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
