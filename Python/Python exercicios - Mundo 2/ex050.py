#DESENVOLVA UM PROGRAMA QUE LEIA 6 NÚMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES. SE O VALOR DIGITADO FOR ÍMPAR, DESCONSIDERE-O
soma=0
cont=0
print('Somador de número pares')
for c in range(0,6):
    num= int(input('Digite um número: '))
    if num%2==0:
        soma+=num
        cont+=1
print('Você informou {} números pares e a soma deles é igual a: {}'.format(cont,soma))
    