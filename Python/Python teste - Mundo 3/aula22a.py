'''
MÓDULOS E PACOTES

MODULARIZAÇÃO - Construir módulos
Foco> dividir um programa grande
    >  aumentar a legibilidade
    > facilitar a manutenção

def fatorial(n):
    f=1
    for c in range(1,n+1):
        f*=c
    return f

def dobro(n):
    return n*2

def triplo(n):
    return n*3

num=int(input('Digite uma valor'))
fat=fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
print(f'O triplo de {num} é {triplo(num)}')

CÓDIGO FICANDO GRANDE, É POSSÍVEL SEPARAR DO CÓDIGO PRINCIPAL

VANTAGENS:
    >Organização do código
    >Facilita na manutenção 
    >Ocultação do código detalhado
    >Reutiliação em outros projetos

    
---------------------------------------------------------------------------------------------------------------------------

PACOTES(BIBLIOTECA)
Quando dentro da pasta 'Modulos/uteis' ficar sobrecarregado com muitas funções, vai dificultar a legibidade e manutenção
Junção de módulos separados por ASSUNTOS = PACOTES
EX: só pra tratamento de números, strings, datas, cores etc

import uteis
from uteis import datas
from uteis import numeros


SINTAXE

__init__.py que fica dentro das pastas

Resumindo: Tenho a pasta principal onde ficará o programa principal, dentro dela crio outra pasta(que será o pacote), crio um arquivo __init__.py e coloco as funções, crio pastas dentro desse pacote para tratar assuntos diferentes
Ex: -Modulos
     -Uteis
      -numeros
       -__init__.py
     -__init__.py
     -programa_principal.py

Obs: tbm é possível criar o pacote(pasta) com arquivo init e outros arquivos como numeros, datas etc, sem ser necessário a criação de subpastas

'''

