#FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR(), QUE RECEBA VÁRIOS PARÂMETROS COM VALORES INTEIROS.
#SEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES E DIZER QUAL DELES É O MAIOR. - NÃO FOI USADO IMPUT, VALORES COLOCADOS NO PRÓPRIO CÓDIGO

import time
def maior(*numero):
    print(f'Entre os números:', end=' ')
    for num in numero:
        time.sleep(1)
        print(f'{num}',end=' ', flush=True)
    time.sleep(2)
    print(f', o maior é: {max(numero)}')

maior(5,4,9,0,50,1)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)