'''
FUNÇÕES - PARTE2

-Interactive Help
-Docstrings
-Argumentos Opcionais
-Escopo de variáveis
-Retorno de resultados


-> INTERACTIVE HELP - AJUDA INTERATIVA
help() - se não funcionar no terminal, digitar python dar enter e help() de novo
help(print) colocar pra rodar, vai trazer as informações tbm
print(input.__doc__)
help(input)

------------------------------------------------------------------------------------------------------

-> DOCSTRINGS - STRING DE DOCUMENTAÇÃO

def contador(i,f,p):
docstring(aspas duplas 3x depois do comando def) - não precisa escrever docstring, só colocar as aspas
    """
    -> Faz uma contagem e monstra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c=i
    while c <=f:
        print(f'{c}',end=' ')
        c+=p
    print('FIM!')

contador(2,10,2)
help(contador) -> Vai trazer as informações por causa da docstring criada / Manual

-------------------------------------------------------------------------------------------------------------------------

-> PARÂMETROS OPCIONAIS
def somar(a,b,c=0): Quando não for informado valor de c, c vai valer 0, podendo tbm fazer def somar(a=0,b=0,c=0):
    s=a+b+c
    print(f'A soma vale {s}')
somar (3,2,5)
somar(8,4) -> valor de c vai faltar
somar(3)
somar()
somar(b=4,c=2)
somar(c=3,a=2)

------------------------------------------------------------------------------------------------------------------------

-> ESCOPO DE VARIÁVEIS - Local onde uma variável vai existir e o local onde a variável não vai mais existir
def teste():
x=8 (VARIÁVEL LOCAL)
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#Programa Principal
n=2(VARIÁVEL GLOBAL)
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}) -> NÃO FUNCIONA POIS X FOI DEFINIDO SOMENTE DENTRO DA FUNÇÃO, NÃO SENDO RECONHECIDO FORA DELA

def teste(b):
    global a - o 'a' de baixo(global) vai passar a valer 8
    a=8 -> Variável local 
    b+=4 
    c=2  
    print(f'A dentro vale {a}') -> 8
    print(f'B dentro vale {b}') -> 9
    print(f'C dentro vale {c}') -> 2
    
a=5 -> ESCOPO GLOBAL
teste(a)
print(f'A dentro vale {a}') -> FUNCIONA NORMAL -> 5 - Passa a valer 8 se usado global dentro da local
print(f'B dentro vale {b}') -> NÃO FUNCIONA - FORA DO ESCOPO
print(f'C dentro vale {c}') -> NÃO FUNCIONA - FORA DO ESCOPO


def funcao():
    n1=4 - LOCAL
    print(f'N1 dentro vale {n1}') -> 4

n1=2 - GLOBAL
funcao()
print(f'N1 fora vale {n1}') -> 2

-------------------------------------------------------------------------------------------------------------------------------

RETORNO DE VALORES
return

def somar(a=0,b=0,c=0):
    s=a+b+c
    # print(f'A soma vale {s}')
    return s

resp=somar(3,2,5)
print(somar(3,2,5))
somar(2,2)
somar(6)

r1=somar(3,2,5)
r2=somar(1,7)
r3=somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')

Bom para personalização dos resultados

'''


#PARTE PRÁTICA
#fatorial de um número

def fatorial(numero=1):
    f=1
    for c in range(numero,0,-1):
        f*=c
    return f

n=int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1=fatorial(5)
f2=fatorial(4)
f3=fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')



def par(n=0):
    if n%2==0:
        return True
    else:
        return False
    
num=int(input('Digite um número: '))
print(par(num))

if par(num):
    print(f'É par!')
else:
    print(f'Não é par!')