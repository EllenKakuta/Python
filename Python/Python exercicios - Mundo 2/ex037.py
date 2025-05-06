# PROGRAMA QUE LEIA UM NÚMERO INTEIRO E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO
#1- PARA BINÁRIO
#2- PARA OCTAL
#3- PARA HEXADECIMAL

print('** CONVERSOR DE NÚMEROS **')
numero = int(input('Digite um número inteiro: '))
escolha = int(input('Escolha uma das opções abaixo para realizar a conversão \n' \
'1- para Binário \n' \
'2- para Octal \n' \
'3- para Hexadecimal \n' \
'-> '))
binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)
if escolha == 1:
    print('O número {} convertido para binário é: {}'.format(numero,binario))
elif escolha ==2:
    print('O número {} convertido para octal é: {}'.format(numero, octal))
elif escolha ==3:
    print('O número {} convertido para hexadecimal é: {}'.format(numero, hexadecimal))
else:
    print('Opção não encontrada, escolha 1 dentre as 3 opções!')