import math


# numero = input('Digite um número de 0 a 9999: ')
# # separador = numero.split()
# # print(separador)
# unidade = numero[3]
# dezena = numero[2]
# centena = numero[1]
# milhar = numero[0]

# print("""unidade: {}
# dezena: {}
# centena: {}
# milhar: {}""".format(unidade,dezena,centena,milhar))


# num = int(input('Digite um número de 0 a 999: '))
# un = math.

#---------------ESTUDAR MAAAAAAAAAAIS------------------------------------------------------------------------#
#----------- RESOLUÇÃO VIA AULA -----------------------------------------#

numero = int(input('Informe um número de 0 a 999: '))
# num = str(numero) #CONVERSÃO DE NÚMERO PARA STRING  
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Analisndo o número {}'.format(numero))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
