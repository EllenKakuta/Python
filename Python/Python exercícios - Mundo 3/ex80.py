#CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR 5 VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA, JÁ NA POSIÇÃO CORRETA DE INSERÇÃO(SEM USAR O SORT()).
#NO FINAL, MOSTRE A LISTA ORDENADA NA TELA
valores=[]
for v in range(0,5):
    num=int(input(f'Informe um número: '))    
    if not valores:
        valores.append(num) 
        print(f'Valor adicionado')  
    elif num > valores[-1]:
        valores.append(num)
        print(f'Valor adicionado ao final da lista')      
    else:         
        for p,v in enumerate(valores):
            if num <=v:
                valores.insert(p,num)
                if p==0:
                    print(f'Valor adicionado ao início da lista')
                else:
                    print(f'Valor adicionado a posição {p+1} da lista')
                break         
print(f'Os valores adicionados são: {valores}')


#CORREÇÃO DO EXERCÍCIO

# lista=[]
# for c in range(0,5):
#     n=int(input('Digite um valor: '))
#     if c==0 or c>lista[-1]:
#         lista.append(n)
#     else:
#         posicao=0
#         while posicao < len(lista):
#             if n <=lista[posicao]:
#                 lista.insert(posicao,n)
#                 break
#             posicao+=1
# print(f'Os valores digitaods em ordem foram: {lista}')