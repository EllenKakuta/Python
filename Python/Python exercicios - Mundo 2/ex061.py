#REFAÇA O DESAFIO 051, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE

print('10 PRIMEIROS TERMOS DE UMA PA')
a1= int(input('Digite o primeiro termo da PA: '))
r= int(input('Digite a razão da PA: '))
contador=1
while contador <=10:
    pa= a1+(contador-1)*r
    contador+=1
    print (pa,end=' ')