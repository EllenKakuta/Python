#FAÇA UM PROGRAMA QUE LEIA NOME E PESO DE VÁRIAS PESSOAS, GUARDANDO TUDO EM UMA LISTA. NO FINAL, MOSTRE:
#A) QUANTAS PESSOAS FORAM CADASTRADAS
#B) UMA LISTAGEM COM AS PESSOAS MAIS PESADAS - colocar o maior peso e os nomes
#C) UMA LISTAGEM COM AS PESSOAS MAIS LEVES - colocar o menor peso e os nomes
#considerando pesado acima de 100 e leve <=70

# dados=list()
# pessoas=list()
# contador_maior=contador_menor=contador=0
# while True:
#     dados.append(str(input('Informe seu nome: ')))
#     dados.append(float(input('Informe o peso: ')))
#     pessoas.append(dados[:])
#     contador+=1
#     dados.clear()
#     resposta=(str(input('Gostaria de continuar? [S/N] '))).upper()
    
#     if resposta=='N':
#         break
    
# for pessoa in pessoas:
#     if pessoa[1] >99:
#         maximo=max(pessoa[1])
      
         
#     elif pessoa[1]<71:
#         contador_menor+=1
            
# print(pessoas)
# print(pessoa)
# print(f'Foram cadastradas {contador} pessoas. ')
# print(f'O maior peso foi de  Kg. Peso de: ')
# print(f'O menor peso foi de  Kg. Peso de: ')

#RESOLUÇÃO VIA AULA
temporario=[]
principal=[]
maior = menor =0
while True:
    temporario.append(str(input('Nome: ')).title())
    temporario.append(float(input('Peso: ')))
    if len(principal)==0:
        maior=menor=temporario[1]
    else:
        if temporario[1]>maior:
            maior=temporario[1]
        if temporario[1]<menor:
            menor=temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    resposta=str(input('Quer continuar? [S/N]: ')).upper()
    if resposta =='N':
        break
print('-'*30)
# print(f'Dados: {principal}')
print(f'Foram cadastradas {len(principal)} pessoas. ')
print(f'O maior peso foi de {maior}Kg. Peso de: ', end='')
for p in principal:
    if p[1]==maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de: ', end='')
for p in principal:
    if p[1]==menor:
        print(f'[{p[0]}] ', end='')