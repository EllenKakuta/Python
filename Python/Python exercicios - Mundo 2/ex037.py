# PROGRAMA QUE LEIA UM NÚMERO INTEIRO E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO
#1- PARA BINÁRIO
#2- PARA OCTAL
#3- PARA HEXADECIMAL

print('** CONVERSOR DE NÚMEROS **')
numero = int(input('Digite um número inteiro: '))
escolha = int(input('Escolha uma das opções abaixo para realizar a conversão \n' \
'1- Binário \n' \
'2- Octal \n' \
'3- Hexadecimal \n' \
'-> '))
binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)
if escolha == 1:
    print('O número {} convertido para binário é: {}'.format(numero,binario[2:]))#pular as 2 primeiras casas
elif escolha ==2:
    print('O número {} convertido para octal é: {}'.format(numero,octal[2:]))
elif escolha ==3:
    print('O número {} convertido para hexadecimal é: {}'.format(numero,hexadecimal[2:]))
else:
    print('Opção não encontrada, escolha uma opção válida!')