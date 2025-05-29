#FAÇA UM PROGRAMA QUE JOGUE PAR OU ÍMPAR COM O COMPUTADOR. O JOGO SÓ SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER, MOSTRANDO O TOTAL DE VITÓRIAS CONSECUTIVAS QUE ELE CONQUISTOU NO FINAL DO JOGO.
#EX: diga um valor: 8
#Par ou ímpar? [P/I] P
# Você jogou 8 e o computador 2. Total deu 10 - Deu par
#Você venceu! Vamos jogar novamente

import random
print('JOGUE PAR OU ÍMPAR COM O COMPUTADOR')
resposta=''
numeral=''
vitoria=0
contador=1
while True:
    valor=int(input('Diga um valor: '))
    computador = random.randint(0,10)
    # print(computador)
    soma=valor+computador
    resposta=str(input('PAR ou ÍMPAR? [P/I]: ')).upper().strip()[0]
    if soma %2==0:
        numeral = 'PAR'
    else:
        numeral='IMPAR'
    print(f'Você jogou {valor} e o computador jogou {computador}. O Total deu {soma} - Deu {numeral}')
    if resposta =='P'and numeral =='PAR':
        print('Você venceu! Vamos jogar novamente!')
        contador+=1
        vitoria+=1
    elif resposta =='I' and numeral=='IMPAR':
        print('Você venceu! Vamos jogar novamente!')
        contador+=1
        vitoria+=1
    else:
        print('Você perdeu!')
        break
print(f'No total, você jogou {contador} vezes e teve {vitoria} vitórias')