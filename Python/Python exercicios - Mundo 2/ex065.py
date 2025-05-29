#CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. NO FINAL DA EXECUÇÃO, MOSTRE A MÉDIA ENTRE TODOS OS VALORES E QUAL FOI O MAIOR E O MENOR VALORES LIDOS. O PROGRAMA DEVE PERGUNTAR AO USUÁRIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES.

print('LEITOR DE NÚMEROS')
valores=[]
contador=1
soma=0
adiciona='S'
valor=int(input('Informe um número: '))
valores.append(valor)
soma+=valor
while adiciona=='S':
    adiciona=str(input('Gostaria de acrescentar outro número? [S/N] ')).upper()
    if adiciona=='S':
        valor=int(input('Informe o número: '))
        valores.append(valor)
        soma+=valor
        contador+=1      
        # print(contador)
if adiciona !='S'and adiciona !='N':
    print('Opção inválida!')
print('A média entre os valores inseridos é: {}'.format(soma/contador))
print('O maior valor digitado foi: {}'.format(max(valores)))
print('O menor valor digitado foi: {}'.format(min(valores)))