import math

oposto = float(input('Qual o valor do cateto oposto? '))
adjacente = float(input('Qual o valor do cateto adjacente? '))

hip = oposto**2+adjacente**2
hipTotal = math.sqrt(hip)

print ('O valor da hipotenusa é {:.2f}'.format(hipTotal))
#-------------------------------------------------------------------------------------------#

oposto = float(input('Qual o valor do cateto oposto? '))
adjacente = float(input('Qual o valor do cateto adjacente? '))

hip = math.hypot(oposto, adjacente) #-->> HÁ UM MÓDULO PARA HIPOTENUSA SEM SER NECESSÁRIO FAZER CONTAS SEPARADAS

print ('O valor da hipotenusa é {:.2f}'.format(hip))


#-------------------------------------------------------------------------------------------#
oposto = float(input('Qual o valor do cateto oposto? '))
adjacente = float(input('Qual o valor do cateto adjacente? '))

hip = (oposto**2+adjacente**2) **(1/2) #SEM UTILIZAÇÃO DO MATH

print ('O valor da hipotenusa é {:.2f}'.format(hip))

#-------------------------------------------------------------------------------------------#