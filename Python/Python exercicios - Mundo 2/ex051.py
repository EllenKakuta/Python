# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PROGRESSÃO ARITMÉTICA. NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO
print('10 PRIMEIROS TERMOS DE UMA PA')
a1= int(input('Digite o primeiro termo da PA: '))
r= int(input('Digite a razão da PA: '))
for c in range(1,11):
    pa= a1+(c-1)*r
    print (pa,end=' ')


