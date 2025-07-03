#CRIE UM PROGRMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL. O PROGRAMA VAI LER O NOME DO JOGADOR E QUANTAS PARTIDAS ELE JOGOU. DEPOIS VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA. NO FINAL, TUDO SERÁ GUARDADO EM UM DICIONÁRIO, INCLUINDO O TOTAL DE GOLS FEITOS DURANTE O CAMPEONATO
#APRIMORE O DESAFIO 93 PARA QUE ELE FUNCIONE COM VÁRIOS JOGADORES, INCLUINDO UM SISTEMA DE VISUALIZAÇÃO DE DETALHES DO APROVEITAMENTO DE CADA JOGADOR.

import time
jogadores=[]
while True:
    jogador={}
    gols=[]
    total_gols=0
    jogador['nome']= str(input('Nome do jogador: ')).title()
    partidas=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(0,partidas):
        gol=int(input(f'Quantos gols na partida {p}? '))
        gols.append(gol)
        total_gols+=gol
    jogador['gols']=gols
    jogador['total']=total_gols
    jogadores.append(jogador.copy())
    while True:
        inclui=str(input('Gostaria de acrescentar outro jogador? [S/N] ')).upper()
        if inclui in 'SN':
            break
        else:
            print('ERRO! Escolha S ou N')
    if inclui == 'N':
        break
print(jogadores)
print('-'*60)
print(f'{"CÓD":>5} {"JOGADOR":<7} {"GOLS":<25} {"TOTAL":>5}')
for i, jogador in enumerate(jogadores):
    gol_str=str(jogador['gols'])
    print(f'{i:>5} {jogador["nome"]:<7} {gol_str:<25} {jogador["total"]:>5}')
while True:
    continua=(int(input(f'\nMostrar dados de qual jogador? (999 encerra) ')))   
    if continua == 999:
        break
    if 0<=continua <len(jogadores):
        c=jogadores[continua]
        print(f'LEVANTAMENTO DO JOGADOR {c["nome"]}')
        for i,g in enumerate(c['gols']):
            print(f' - No jogo {i} fez {g} gols')
    else:
        print(f'ERRO! Não existe jogador com código {continua}! Tente novamente')
        time.sleep(1)
print('ENCERRRANDO..')


#CORREÇÃO VIA AULA
# print('-'*30)
# print('cod ', end='')
# for i in jogador.keys():
#     print(f'{i:<15}', end='')
# print()
# for k, v in enumerate(jogadores):
#     print(f'{k:>3} ', end='')
#     for d in v.values():
#         print(f'{str(d):<15}', end='')
#     print()
# print('-'*40)
# while True:
#     busca=int(input(f'Buscar dados de qual jogador? (999 para parar) '))
#     if busca ==999:
#         break
#     if busca >=len(jogadores):
#         print(f'Erro! Não existe jogador com o código {busca}')
#     else:
#         print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}: ')
#         for i, g in enumerate(jogadores[busca]["gols"]):
#             print(f' - No jogo {i} fez {g} gols.')
#         print('-'*40)
# print(f'VOLTE SEMPRE')






