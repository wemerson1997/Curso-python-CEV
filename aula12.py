nome = str(input("Qual é o seu nome: "))
if nome == 'Gustavo':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'paulo':
    print('Seu nome é bem popular no brasil')
elif nome == 'Wemerson':
    print('Seu nome é lindo')
else:
    print('Você é um otário')
print('tenha um bom dia, {}'.format(nome))