#CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA.
#DEPOIS DISSO, CRIE DUAS LISTAS EXTRAS QUE VÃO CONTER APENAS OS VALORES PARES E OS VALORES ÍMPARES DIGITADOS, RESPECTIVAMENTE.
#AO FINAL, MOSTRE O CONTEÚDO DAS 3 LISTAS GERADAS.
valores=[]
valores.append((int(input(f'Informe um valor: '))))
continua=''
while True:
    continua=str(input('Gostaria de continuar? [S/N]')).upper()
    if continua=='S':
        valores.append(int(input('Informe o novo valor: ')))
    elif continua !='S'and continua !='N':
        print(f'Opção inválida! Tente novamente..')
    else:
        break
par=[]
impar=[]
for valor in valores:
    if valor %2==0:
        par.append(valor)
    else:
        impar.append(valor)
print(f'Valores informados:{valores}')
print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')
