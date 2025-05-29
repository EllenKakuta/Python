#CRIE UM PROGRMA QUE VAI GERAR CINCO NÚMEROS ALEATÓRIOS E COLOCAR EM UMA TUPLA.
#DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMEROS GERADOS E TAMBÉM INDIQUE O MENOR E O MAIOR VALOR QUE ESTÃO NA TUPLA.
import random

g1=random.randint(0,10)
g2=random.randint(0,10)
g3=random.randint(0,10)
g4=random.randint(0,10)
g5=random.randint(0,10)
gerador=(g1,g2,g3,g4,g5)
print(f'Numeros gerados:{gerador}')
print(f'O menor número é: {min(gerador)}')
print(f'O maior número é: {max(gerador)}')

#-----------------------------------------------------------------------------------------------------------------
#CORREÇÃO VIA AULA
numeros=(random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10))
print('Os valores sorteados foram:', end=' ')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior número é: {max(numeros)}')
print(f'O menor número é: {min(numeros)}')