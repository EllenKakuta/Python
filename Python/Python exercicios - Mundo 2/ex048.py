#FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS ÍMPARES QUE SÃO MÚLTIPLOS DE 3 EM QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500

soma = 0
cont=0
for c in range(1,501,2):#o contagem de 2 em dois a partir do 1 para que sejam número ímpares
    if c%3==0:
        soma+=c
        cont+=1
        # print(c)
print('A soma de todos os {} números ímpares múltiplos de 3 é igual a: {}'.format(cont,soma))
