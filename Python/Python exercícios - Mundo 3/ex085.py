#CRIE UM PROGRAMA ONDE O USÁRIO POSSA DIGITAR 7 VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA ÚNICA QUE MANTENHA SEPARADOS OS VALORES PARES E ÍMPARES. NO FINAL, MOSTRE OS VALORES PARES E ÍMPARES EM ORDEM CRESCENTE - TUDO NUMA LISTA SÓ, NÃO EM 3  LISTAS SEPARADAS COMO NO OUTRO EXERCÍCIO - 1 LISTA COMPOSTA POR 2 LISTAS INTERNAS

# valores=list()
# pares=list()
# impares=list()
# for v in range(0,7):
#     valor=int(input(f'Digite o {v+1}° valor: '))
#     valores.append(valor)
#     if valor %2==0:
#         pares.append(valor)
        
#     else:
#         impares.append(valor)
# print(f'Números digitados: {valores}')
# valores.clear()
# valores.append(pares)
# valores.append(impares)
# pares.sort()
# impares.sort()
# print(f'Valores pares: {pares}\nValores ímpares {impares}')
# print(f'Números digitados separados por ordem crescente em grupos de pares e ímpares: {valores}')

#CORREÇÃO VIA AULA:

numero= [[],[]]
valor=0
for c in range(1,8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor %2==0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
numero[0].sort()       
numero[1].sort()
print(f'Os valores pares digitador foram: {numero[0]}')
print(f'Os valores ímpares digitados foram: {numero[1]}')