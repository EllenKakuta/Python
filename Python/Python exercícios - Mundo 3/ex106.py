#FAÇA UM MINI-SISTEMA QUE UTILIZE O INTERACTIVE HELP DO PYTHON. O USUÁRIO VAI DIGITAR O COMANDO E O MANUAL VAI APARECER. QUANDO O USUÁRIO DIGITAR A PALAVRA 'FIM', O PROGRAMA SE ENCERRARÁ.
# OBS: USE CORES.

import time
limpa = '\033[m'
vermelho = '\033[31m'
verde = '\033[32m'
fundoCinza='\033[47m'
amarelo='\033[33m'
magenta='\033[35m'
inverso = '\033[7m'

def titulo(texto):
    t=len(texto)-4
    print(f'{fundoCinza}~{limpa}'*t)
    print(f'  {texto}')
    print(f'{fundoCinza}~{limpa}'*t)


def sistema():
    while True:
        titulo(f'{verde}SISTEMA DE AJUDA PyHELP{limpa}')
        time.sleep(1)
        comando=str(input(f'{magenta}Função ou Biblioteca>{limpa} ')).lower().strip()
        if comando == 'fim':
            titulo(f'{vermelho}>> ATÉ LOGO! <<{limpa}')
            break
        else:
            time.sleep(1)
            titulo(f'{verde}>> Acessando o manual do comando "{comando}"{limpa}')
            time.sleep(2)
            print(inverso)
            help(eval(comando))
            print(limpa)
            time.sleep(3)

sistema()


#CÓDIGO FEITO VIA CORREÇÃO DO EXERCÍCIO
# from time import sleep
# c=('\033[m', #0 sem cor
#    '\033[0;30;41m',#1 vermelho
#    '\033[0;30;42m',#2 verde
#    '\033[0;30;43m',#3 amarelo
#    '\033[0;30;44m',#4 azul
#    '\033[0;30;45m',#5 roxo
#    '\033[7;30m'    #6 branco
#    );

# def ajuda(com):
#     titulo(f'Acessando o manual do comando \'{com}\'',4)
#     print(c[6], end='')
#     help(com)
#     print(c[0], end='')
#     sleep(2)

# def titulo(msg, cor=0):
#     tamanho=len(msg)+4
#     print(c[cor], end='')
#     print('~'*tamanho)
#     print(f'  {msg}')
#     print('~'*tamanho)
#     print(c[0], end='')
#     sleep(1)

# comando=''
# while True:
#     titulo('SISTEMA DE AJUDA PyHELP', 2)
#     comando=str(input('Função ou Biblioteca> '))
#     if comando.upper()=='FIM':
#         break
#     else:
#         ajuda(comando)
# titulo('ATÉ LOGO!',1)