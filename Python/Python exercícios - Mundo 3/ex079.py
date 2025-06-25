#CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA.CASO O NÚMERO JÁ EXISTA LÁ DENTRO, ELE NÃO SERÁ ADICIONADO.
#NO FINAL, SERÃO EXIBIDOS TODOS OS VALORES ÚNICOS DIGITADOS, EM ORDEM CRESCENTE

valores=[]
valores.append(int(input(f'Informe um valor: ')))
print(f'Valor adicionado!')
continua=''
while True:
    continua=str(input('Gostaria de continuar? [S/N] ')).upper()
    if continua =='S':
        valor=int(input('Informe o próximo valor: '))
        if valor in valores:
            print(f'Valor existente. Não adicionado!')
        else:
            valores.append(valor)
            print(f'Valor adicionado!')
    elif continua != 'S' and continua !='N':
        print(f'Opção inválida! Tente novamente..')
    else:
        break
valores.sort()
print(f'Valores digitados {valores}')