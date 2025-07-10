#CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO FATORIAL() QUE RECEBA DOIS PARÂMETROS: O PRIMEIRO QUE INDIQUE O NÚMERO A CALCULAR E O OUTRO CHAMADO SHOW, QUE SERÁ UM VALOR LÓGICO(OPCIONAL) INDICANDO SE SERÁ MOSTRADO OU NÃO NA TELA O PROCESSO DE CÁLCULO DO FATORIAL.

def fatorial(n,show=False):
    """
    Calcula o fatorial de um número.
    :param n: número a ser calculado
    :param show: opcional para mostrar ou não a conta.
    :return: o valor fatorial de um número n
    """
    print('-'*40)
    f=1
    for c in range(n,0,-1):          
        if show==True:
            print(c, end='')
            if c >1:
                print(f' x ', end='')  
            else:
                print(f' = ', end='')
        f*=c               
    return f

n=int(input('Qual o fatorial desejado? '))
print(fatorial(n,True))
help(fatorial)
