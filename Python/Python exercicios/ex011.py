largura = float(input('Digite a largura da parede: '))
altura= float (input('Digite a altura da parede: '))
area = largura*altura
tinta = area/2
print ('A quantidade de tinta necessária será de {:.2f} litros para uma área de {:.2f}m²'.format(tinta, area))
