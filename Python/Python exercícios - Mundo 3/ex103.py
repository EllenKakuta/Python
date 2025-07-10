#FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FICHA() QUE RECEBA 2 PARÂMETROS OPCIONAIS: O NOME DE UM JOGADOR E QUANTOS GOLS ELE MARCOU.
#O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DO JOGADOR, MESMO QUE ALGUM DADO NÃO TENHA SIDO INFORMADO CORRETAMENTE

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador: {nome} marcou {gols} gol(s)')    


nome=input('Nome do jogador: ')
gols=input('Gols marcados: ')
if gols.isnumeric():
    gols=int(gols)
else:
    gols=0

if nome.strip()=='':
    ficha(gols=gols)
else:
    ficha(nome, gols)


