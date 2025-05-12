#FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS ÍMPARES QUE SÃO MÚLTIPLOS DE 3 EM QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500

s = 0
for c in range(1,501):
    if c%3==0:
        s+=c
        # print(c)
print('A soma de todos os números ímpares múltiplos de 3 é igual a: {}'.format(s))