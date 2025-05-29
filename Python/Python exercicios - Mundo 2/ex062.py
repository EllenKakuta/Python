#MELHORE O DESAFIO 061, PERGUNTANDO PARA O USUÁRIO SE ELE QUER MOSTRAR MAIS TERMOS. O PROGRAMA ENCESSA QUANDO ELE DISSER QUE QUER MOSTRAR 0 TERMOS.

# print('DESCUBRA OS 10 PRIMEIROS TERMOS DE UMA PROGRESSÃO ARITIMÉTICA')
# a1= int(input('Digite o primeiro termo da PA: '))
# r= int(input('Digite a razão da PA: '))
# contador=1
# resposta='S'
# while resposta!='N':
#     resposta=str(input('Gostaria de incluir mais termos? [S/N]: ')).upper()
#     if resposta =='S':
#         acrescimo=int(input('Quantos termos gostaria de acrescentar?: '))
#         atualizado = 10+acrescimo
#     if resposta =='N':
#         atualizado=10+acrescimo
#         # print(atualizado) - coloquei para teste 
#         # print(contador)- coloquei para teste           
#     if resposta!='S' and resposta!='N': 
#         print('Resposta inválida')
# while contador <=atualizado:
#     pa=a1+(contador-1)*r
#     contador+=1
#     print(pa,end=' ')


#CORREÇÃO
print('Gerador de PA')
a1= int(input('Digite o primeiro termo da PA: '))
r= int(input('Digite a razão da PA: '))
contador=1
total=0
mais=10
while mais!=0:
    total+=mais
    while contador<=total:
        pa= a1+(contador-1)*r
        contador+=1
        print (pa,end=' ')
    print('-> Pausa ')
    mais=int(input('Gostaria de adicionar quantos termos? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))