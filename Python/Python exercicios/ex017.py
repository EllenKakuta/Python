import math

oposto = float(input('Qual o valor do cateto oposto? '))
adjacente = float(input('Qual o valor do cateto adjacente? '))

hip = oposto**2+adjacente**2
hipTotal = math.sqrt(hip)

print ('O valor da hipotenusa é {:.2f}'.format(hipTotal))