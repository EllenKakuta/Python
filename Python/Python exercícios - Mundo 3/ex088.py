#FAÇA UM PROGRAMA QUE AJUDE UM JOGADOR DA MEGA SENA A CRIAR PALPITES. O PROGRAMA VAI PERGUNTAR QUANTOS JOGOS SERÃO GERADOS E VAI SORTEAR 6 NÚMEROS ENTRE 1 E 60 PARA CADA JOGO, CADASTRANDO TUDO EM UMA LISTA COMPOSTA.

import random
import time
jogos=list()
quantidade=int(input(f'Quantidade de jogos desejados: '))
for j in range(0,quantidade):
    jogo=list()
    while len(jogo)<6:        
        sorteio=random.randint(1,60)
        if sorteio not in jogo:
            jogo.sort()
            jogo.append(sorteio)
    jogos.append(jogo[:])
    # print(jogo)
print(f'Listagem de jogos: {jogos}')


#CORREÇÃO VIA AULA
# lista=list()
# jogos2=list()
# print('-'*30)
# print(' JOGA NA MEGA SENA')
# print('-'*30)
# quant=int(input(f'Quantos jogos você quer que eu sorteie? '))
# tot=1
# while tot<=quant:
#     cont=0
#     while True:
#         num=random.randint(1,60)
#         if num not in lista:
#             lista.append(num)
#             cont+=1
#         if cont >=6:
#             break
#     lista.sort()
#     jogos2.append(lista[:])
#     lista.clear()
#     tot+=1
# print('-'*3, f'SORTEANDO {quant} JOGOS', '-'*3)
# for i, l in enumerate(jogos2):
#     print(f'Jogo {i+1}: {l}')
#     time.sleep(1)

    
