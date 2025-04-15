import math

angulo = float(input('Informe o ângulo: '))
sen = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)

print('O angulo de {:.2f}° possui o seno: {:.2f}°, cosseno: {:.2f}° e tangente: {:.2f}°'.format(angulo, sen, cos, tan))