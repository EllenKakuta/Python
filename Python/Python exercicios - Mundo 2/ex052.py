#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO

print('IDENTIFICADOR DE NÚMERO PRIMO')
num = int(input('Digite um número inteiro: '))
contador = 0
if num >1:
    for c in range(1,num+1):
        if  num%c==0:      
            contador+=1             
if contador >2:
    print('{} não é um número primo'.format(num))
else:
    print('{} é um número primo'.format(num))
