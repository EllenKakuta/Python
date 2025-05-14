#FAÇA UM PROGRAMA QUE LEIA O PESO DE 5 PESSOAS. NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR PESO LIDOS
pesos=[]
for c in range(1,6):
    peso=float(input('Peso da {}ª pessoa:  '.format(c)))
    pesos.append(peso)#inclui dentro da lista de pesos para que possa ser encontrado o maior
print('O maior peso inserido foi: {:.1f}Kg'.format(max(pesos)))
print('O menor peso inserido foi: {:.1f}Kg'.format(min(pesos)))