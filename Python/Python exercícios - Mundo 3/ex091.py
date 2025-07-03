#CRIE UM PROGRAMA ONDE 4 JOGADORES JOGUEM UM DADO E TENHAM RESULTADOS ALEATÓRIOS. GUARDE ESSES RESULTADOS EM UM DICIONÁRIO. NO FINAL, COLOQUE ESSE DICIONÁRIO EM ORDEM, SABENDO QUE O VENCEDOR TIROU O MAIOR NÚMERO NO DADO - COM DICIONÁRIO
#Valores sorteados: (tempo para cada sorteio acontecer)
#O jogador 1 tirou 6
#O jogador 2 tirou 1
#O jogador 3 tirou 6
#O jogador 4 tirou 5
#Ranking dos jogadores:
#1º lugar: jogador 1 com 6
#2º lugar: jogador 3 com 6
#3º lugar: jogador 4 com 5
#4º lugar: jogador 2 com 1

import time
import random
from operator import itemgetter #[0] EM PARTE DE CHAVE [1] EM PARTE DE VALOR
jogadores={}
listajogadores=list()
for c in range (1,5):
    jogadores[f'jogador {c}']=random.randint(1,6)
for k, v in jogadores.items():
    time.sleep(2)
    print(f'O {k} tirou {v} no dado.')
# print(jogadores.items()) - teste
lista=[]
for k,v in jogadores.items():
    lista.append([v,k])
lista.sort(reverse=True)
time.sleep(2)
print(f'-'*10 ,'Ranking dos jogadores', '-'*10)
for posicao, item in enumerate(lista):
    time.sleep(2)
    print(f'{posicao+1}º lugar: {item[1]} com {item[0]}')

#---------------------------------------------
#FEITO EM AULA
print(f'CÓDIGO FEITO EM AULA')
ranking=[]
print(f'Valores sorteados: ')
for k,v in jogadores.items():
    print(f'{k} tirou {v}')
    time.sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i,v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    time.sleep(1)


  
  
