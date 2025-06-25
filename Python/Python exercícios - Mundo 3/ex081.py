#CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA. DEPOIS DISSO, MOSTRE:
#A)QUANTOS NÚMEROS FORAM DIGITADOS
#B)A LISTA DE VALORES ORDENADAS DE FORMA DECRESCENTE
#C)SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA

valores=[]
valores.append(int(input('Informe um valor: ')))
continua=''
while True:
    continua=str(input('Gostaria de continuar? [S/N] ')).upper()
    if continua=='S':
        valores.append(int(input(f'Informe um novo valor: ')))
    elif continua!='S'and continua !='N':
        print(f'Opção inválida! Tente novamente..')
    else:
        break
print(f'Foram digitados {len(valores)} números')
valores.sort(reverse=True)
print(f'Números digitados em ordem descrescente : {valores}')
if 5 in valores:
    print('O número 5 faz parte da lista')
else:
    print('O número 5 não faz parte da lista')