#FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR(), QUE RECEBA 3 PARâMETROS:INÍCIO, FIM E PASSO E REALIZE A CONTAGEM
#SEU PROGRAMA TEM QUE REALIZAR 3 CONTAGENS ATRAVÉS DA FUNÇÃO CRIADA:
#A) DE 1 ATÉ 10, DE 1 EM 1
#B) DE 10 ATÉ 0, DE 2 EM 2
#C) UMA CONTAGEM PERSONALIZADA - USUÁRIO VAI DIGITAR O INICIO, O FIM E O PASSO - TANTO CRESCENTE QUANTO DECRESCENTE, E TBM COM NÚMERO NEGATIVO (vAI VOLTAR). SE NÃO COLOCAR O PASSO (0) VAI TRANSFORMAR EM 1
import time
# def contador(inicio,fim,passos):
#     print(f'Contagem personalizada de {inicio} até {fim} de {passos} em {passos}: ')
#     if fim < inicio :
#         if passos ==0:
#             passos=1
#         for c in range(inicio,fim-1,-passos):
#             time.sleep(1)
#             print(f'{c}', end=' ', flush=True)
#     elif passos < 0:
#         for c in range(fim,inicio-1,passos):
#             time.sleep(1)
#             print(f'{c}', end=' ', flush=True)
#     elif passos ==0:
#         for c in range(inicio,fim+1,1):
#             time.sleep(1)
#             print(f'{c}', end=' ', flush=True)
#     elif fim > inicio:
#         for c in range(inicio,fim+1,passos):
#             time.sleep(1)
#             print(f'{c}', end=' ', flush=True)
 

# print(f'Contagem de 1 até 10, de 1 em 1: ')
# for c in range(1,11,1):
#     time.sleep(1)
#     print(f'{c}', end=' ', flush=True)       
# time.sleep(2)

# print(f'\nContagem regressiva de 10 até 0, de 2 em 2: ')
# for c in range(10,-1,-2):
#     time.sleep(1)
#     print(f'{c}', end=' ', flush=True)
# time.sleep(2) 

# print(f'Contagem personalisada')
# inicio=int(input(f'\nNúmero inicial: '))
# fim=int(input('Número final: '))
# passos=int(input(f'Passos: '))

# contador(inicio,fim,passos)


#CORREÇÃO AULA
def contador(i,f,p):
    if p < 0:
        p*=-1

    if p ==0:
        p=1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    # time.sleep(2)
    cont = i
    if i < f:
        
        while cont <= f:
            # time.sleep(1)
            print(f'{cont}', end=' ', flush=True)
            cont+=p
    else:
        while cont >= f:
            # time.sleep(1)
            print(f'{cont}', end=' ', flush=True)
            cont-=p
    print('FIM')

contador(1,10,1)
contador(10,0,2)
print(f'Agora é a sua vez de personalizar a contagem!')
inicio=int(input(f'Início: '))
fim=int(input('Fim: '))
passo=int(input(f'Passo: '))
contador(inicio,fim,passo)

#FORMA MUITO MAIS RÁPIDA DE SER FEITA, MAS O MEU TAMBÉM FUNCIONOU KK