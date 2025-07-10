#FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR(), QUE RECEBA VÁRIOS PARÂMETROS COM VALORES INTEIROS.
#SEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES E DIZER QUAL DELES É O MAIOR. - NÃO FOI USADO IMPUT, VALORES COLOCADOS NO PRÓPRIO CÓDIGO

import time
def maior(*numero):
    print('-'*30)
    if not numero:
        print('Nenhum número foi informado')
    else:
        cont=0
        time.sleep(0.3)
        print('-'*30)
        print(f'Analisando os números')
        for num in numero:
            time.sleep(1)
            print(f'{num}',end=' ', flush=True)
            cont+=1
        time.sleep(2)
        print(f'\nForam informados {cont} números ao todo.')
        print(f'O maior é: {max(numero)}')
        

maior(5,4,9,0,50,1)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
maior()