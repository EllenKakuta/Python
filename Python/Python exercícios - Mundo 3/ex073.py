#CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL, NA ORDEM DE COLOCAÇÃO. DEPOIS MOSTRE:
#A) APENAS OS 5 PRIMEIROS COLOCADOS
#B) OS ÚLTIMOS 4 COLOCADOS DA TABELA
#C) UMA LISTA COM OS TIMES EM ORDEM ALFABÉTICA
#D) EM QUE POSIÇÃO ESTÁ O TIME DA CHAPECOENSE

times=('Palmeiras', 'Flamengo', 'Cruzeiro', 'Bragantino', 'Fluminense', 'Ceará', 'Bahia', 'Corinthians', 'Mirassol', 'Atlético-MG', 'Botafogo', 'Grêmio', 'São Paulo', 'Internacional', 'Vasco da Gama', 'Fortaleza', 'Vitória', 'Santos', 'Juventude', 'Sport Recife' )
print(f'-'*20,'TABELA DE CLASSIFICAÇÃO','-'*20)
for posicao, time in enumerate(times):
    print(f'{posicao+1}° - {time}')
print(f'-'*80)
print(f'OS 5 PRIMEIROS COLOCADOS SÃO: ',times[:5])
print(f'-'*80)
print(f'OS 4 ÚLTIMOS COLOCADOS SÃO: ',times[-4:])
print(f'-'*80)
print(f'TIMES EM ORDEM ALFABÉTICA: ',sorted(times))
print(f'-'*80)
# if 'São Paulo' in times:
print(f'São Paulo está na {times.index("São Paulo")+1}° posição')
print(f'-'*80)