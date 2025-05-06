import random
computador =(random.randint(0,5))
# print (computador)
print('DESCUBRA O NÚMERO')
numero = int(input('Digite um número entre 0 e 5: '))
if numero == computador:
    print('Parabéns, você acertou!!')
else:
    print('Não foi dessa vez, o número correto é {} ...'.format(computador))