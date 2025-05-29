'''
VARIÁVEIS COMPOSTAS - TUPLAS

-> AS TUPLAS SÃO IMUTÁVEIS (NÃO DA PRA TIRAR DA TUPLA)

'''

lanche=('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')#as tuplas tbm podem ser usadas sem parênteses a partir do python3
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])#Python sempre ignora o último elemento
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
# Tuplas são imutáveis
# lanche[1]='Refrigerante'
# print(lanche[1]) - Não é executado, aparece erro
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

for cont in range(0,len(lanche)): #quando precisar usar a posição
    print(f'Vou comer {lanche[cont]}')

for posicao, comida in enumerate(lanche):#quando precisar usar a posição
    print(f'Vou comer {comida} na posição {posicao}')

print(sorted(lanche)) #coloca em ordem


a=(2,5,4)
b=(5,8,1,2)
c=a+b
d=b+a
print(a)
print(b)
print(c)
print(d)
print(len(c))
print(c.count(5)) #quantas vezes está aparecendo o número 5 dentro de c
print(c.index(8)) #em qual posição está o número 8
print(c.index(5,1))

pessoa=('Ellen', 40, 'F', 94.65)
# del(pessoa) - é imutável, menos para apagar ela toda
print(pessoa)