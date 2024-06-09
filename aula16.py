lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#tuplas são imutáveis

#Não precisa de posição
for comida in lanche:
    print(f'Eu vou comer {comida}')


#precisa da posição
for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#precisa da posição e do numero
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')