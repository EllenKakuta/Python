'''
LAÇOS DE REPETIÇÃO(PARTE3)
INTERROMPENDO REPETIÇÕES WHILE

enquanto verdadeiro:
    se chão
        passo
    se buraco
        pula
    se moeda
        pega
    se troféu
        pula
        interrompa
pega

------------------------------------------

while true:
    if chão
        passo
    if buraco
        pula
    if moeda
        pega
    if troféu
        pula
        break (sai do looping - joga pra fora da estrutura de repetição)
pega

'''

contador=1
while contador<=10:
    print(contador, '-> ', end='')
    contador+=1
print('Acabou')

n=0
s=0
while n!=999:
    n=int(input('Digite um número: '))


while True:
    n=int(input('Digite um número: '))
    if n ==999:
        break
    s+=n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}') #PYTHON 3.6+
    

nome='José'
idade=33
salario=987.3
print(f'O {nome:^20} tem {idade} anos e ganha R${salario:.2f}')