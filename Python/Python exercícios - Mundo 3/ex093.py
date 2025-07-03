#CRIE UM PROGRMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL. O PROGRAMA VAI LER O NOME DO JOGADOR E QUANTAS PARTIDAS ELE JOGOU. DEPOIS VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA. NO FINAL, TUDO SERÁ GUARDADO EM UM DICIONÁRIO, INCLUINDO O TOTAL DE GOLS FEITOS DURANTE O CAMPEONATO

total_partidas=total_gols=0
jogador={}
jogador['nome']=str(input('Nome do jogador: ')).title()
partidas=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols=list()
for p in range(1,partidas+1):
    gol=int(input(f'Quantos gols na partida {p}? '))
    gols.append(gol)
    total_gols+=gol
    total_partidas+=1
jogador['gols']=gols[:]
jogador['total'] = total_gols
# jogador['total'] = sum(partidas) - AULA DE CORREÇÃO
print('-'*60)
print(jogador)
print('-'*60)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor: {v}')
print('-'*60)
print(f'O jogador {jogador["nome"]} jogou {total_partidas} partidas.')
# print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.') - AULA DE CORREÇÃO
for g in enumerate(gols):
# for g in enumerate(jogador['gols']): - AULA DE CORREÇÃO
    print(f' => Na partida {g[0]+1}, fez {g[1]} gols.')
print(f'Foi um total de {total_gols} gols.')
print()