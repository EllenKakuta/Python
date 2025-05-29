#ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO N INTEIRO QUALQUER E MOSTRE NA TELS OS N PRIMEIROS ELEMENTOS DE UMA SEQUENCIA DE FIBONACCI
#EX: 1->1->2->3->5->8

print('SEQUÊNCIA DE FIBONACCI')
n=int(input('Quantos elementos terá a sequência? '))
contador=3
elemento1=0
elemento2=1
print('{} {} '.format(elemento1,elemento2),end='')
while contador <=n:
    elemento3=elemento1+elemento2
    elemento1=elemento2
    elemento2=elemento3
    contador+=1
    print(elemento3, end=' ')