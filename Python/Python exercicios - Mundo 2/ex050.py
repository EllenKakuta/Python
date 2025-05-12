#DESENVOLVA UM PROGRAMA QUE LEIA 6 NÚMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FORME PARES. SE O VALOR DIGITADO FOR ÍMPAR, DESCONSIDERE-O
s=0
print('Somador de número pares')
for c in range(0,6):
    num= int(input('Digite um número: '))
    if num%2==0:
        s+=num
if num%2!=0:
    print('Não foi digitado nenhum número par')
print('A soma de todos os número pares é igual a: {}'.format(s))
    