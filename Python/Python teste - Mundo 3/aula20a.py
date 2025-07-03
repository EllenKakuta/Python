'''
FUNÇÕES - PARTE 1

Rotina - algo que acontece constantemente no programa
print()
input()
len()
int()
float()
São todas funções para o python, ou seja, já existente

função mostralinha()
-------------------------------------------------------------

def - definição de função

Algo trabalhoso e repetitivo = Rotina
OTIMIZAR

def mostralinha():
    print('--------------------------------------')

mostralinha()
print('       SISTEMA DE ALUNOS         ')
mostralinha()
print('       CADASTRO DE FUNCIONÁRIOS     ')
mostralinha()
print('      ERRO DO SISTEMA            ')
mostralinha()



print('-'*30)
print('CURSO EM VÍDEO')
print('-'*30)
print('-'*30)
print('APRENDA PYTHON')

def lin():
    print('-'*30)


#Programa principal - 2 linhas para executar
lin()
print('CURSO EM VÍDEO')
lin()
lin()
print('APRENDA PYTHON')

------------------------------------------------------------------------------------------------------------------------------

print('--------------------------')
print(         )
print('--------------------------')

def mensagem(msg):
    print('--------------------------')
    print(msg)
    print('--------------------------')
mensagem('SISTEMA DE ALUNOS')

------------------------------------------------------------------------------------------------------------------------------------

def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

#Programa principal - 2 linhas para executar
titulo('CURSO EM VÍDEO')
titulo('APRENDA PYTHON')

-------------------------------------------------------------------------------------------------------------------------------------

EMPACOTAMENTO
def contador(*num): o asterisco vai usar quantos parâmetros forem escritos
    print(num)#cria uma tupla com todos os valores

contador(5,7,3,1,4)
contador(8,4,7)

'''

#PARTE PRÁTICA
a=4
b=5
s=a+b
print(s)

a=8
b=9
s=a+b
print(s)

a=2
b=1
s=a+b
print(s)
#-------------------------------------------------------------
def soma(a,b):
    s=a+b
    print(s)
#PROGRAMA PRINCIPAL
soma(4,5)#PARÂMETROS
soma(8,9)
soma(2,1)
#soma(4) - VAI DAR ERRO POIS TEM SOMENTE 1 PARAMETRO E A FUNÇÃO TEM 2
#------------------------------------------------------------------------
def soma(a,b):
    print(f'A = {a} e B = {b}')
    s=a+b
    print(f'A soma A + B = {s}')

soma(4,5)
soma(b=4,a=5) #dá para inverter os valores
soma(7,2)

#EMPACOTAR PARÂMETROS
def contador(*num):
    for valor in num:
        print(f'{valor}', end=' ')
    print('FIM!')

def contador(*num):
    tam=len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2,1,7)#tuplas
contador(8,0)
contador(4,4,7,6,2)

#-----------------------------------
#ISSO NÃO É UM DESEMPACOTAMENTO
def dobra(lista):
    posicao=0
    while posicao <len(lista):
        lista[posicao]*=2
        posicao+=1

valores=[6,3,9,1,0,2]#listas
print(valores)
dobra(valores)
print(valores)

#ISSO É DESEMPACOTAMENTO
def soma(*valores):
    s=0
    for num in valores:
        s+=num
    print(f'Somando os valores {valores} temos {s}')

soma(5,2)
soma(2,9,4)