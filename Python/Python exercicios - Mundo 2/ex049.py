#REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHERM SÓ QUE AGORA UTILIZANDO O LAÇO FOR

num = int(input('Qual a tabuada solicitada? '))
for c in range (1, 11):
    calculo = num*c
    print('{} x {} = {}'.format(num,c,calculo))