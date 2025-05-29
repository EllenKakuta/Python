#CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
#[1] SOMAR
#[2] MULTIPLICAR
#[3] MAIOR
#[4] NOVOS NÚMEROS
#[5] SAIR DO PROGRAMA
#SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO
import time
valor1=0
valor2=0
menu=0
valor1=int(input('INSIRA O 1º VALOR: '))
valor2=int(input('INSIRA O 2º VALOR: '))
while menu !=5:
    menu=int(input('QUAL A AÇÃO DESEJADA? \n' \
    '[1] SOMAR\n' \
    '[2] MULTIPLICAR \n' \
    '[3] MAIOR \n' \
    '[4] NOVOS NÚMEROS \n' \
    '[5] SAIR DO PROGRAMA \n' \
    '-> '))
    time.sleep(1)
    if menu==1:
        print('A soma entre {} e {} é: {}'.format(valor1, valor2,valor1+valor2))
        time.sleep(2)
    elif menu==2:
        print('A multiplicação entre {} e {} é: {}'.format(valor1,valor2,valor1*valor2))
        time.sleep(2)
    elif menu==3:
        if valor1>valor2:
           print('O número {} é maior que {}'.formtat(valor1,valor2))
        elif valor2>valor1:
           print('O número {} é maior que {}'.format(valor2,valor1))
        else: 
            print('Os valores são iguais')
        time.sleep(2)
    elif menu==4:
        valor1=int(input('INSIRA O 1º VALOR: '))
        valor2=int(input('INSIRA O 2º VALOR: '))
        time.sleep(2)
    else:
        print('Opção inválida, escolha novamente')
        time.sleep(2)
print('ENCERRANDO...')