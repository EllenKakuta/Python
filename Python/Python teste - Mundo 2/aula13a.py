#LAÇOS DE REPETIÇÃO(PARTE1) A estrutura FOR precisa de um limite 
#LAÇO COM VARIÁVEL DE CONTROLE - Ex:
# laço c no intervalo(1,10)
#     passo
# pega

# for c in range(1,10):
#     passo
# pega

for c in range(0,6):
    print('Oi')
print('FIM')

for c in range(1,7):#conta de 1 a 6, sempre preciso colocar um a mais
    print(c)
print('FIM')

for c in range(6,0,-1):#para fazer de trás pra frente
    print(c)
print('FIM')

for c in range(0,7,2):#para pular de 2 em 2
    print(c)
print('FIM')

n=int(input('Digite um número: '))
for c in range(0,n+1):
    print(c)
print('FIM')

i=int(input('Início: '))
f=int(input('Fim: '))
p=int(input('Passo: '))
for c in range(i,f+1,p):
    print(c)
print('FIM')

s=0
for c in range(0,3):
    n=int(input('Digite um número: '))
    s+=n
print('A soma de todos os números digitados é: {}'.format(s))