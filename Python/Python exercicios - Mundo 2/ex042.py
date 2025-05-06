#REFAZER EXERCICIO 035 DOS TRIÂNGULOS - ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO
#EQUILÁTERO - TODOS OS LADOS IGUAIS
#ISÓSCELES - DOIS LADOS IGUAIS
#ESCALENO - TODOS OS LADOS DIFERENTES

print('É POSSÍVEL FORMAR UM TRIÂNGULO? QUAL TRIÂNGULO SERÁ FORMADO? ')
r1 = float(input('Informe o valor da primeira reta: '))
r2 = float(input('Informe o valor da segunda reta: '))
r3 = float(input('Informe o valor da terceira reta: '))
if (r1+r2 >r3) and (r2+r3>r1) and (r3+r1>r2):
    if (r1==r2) and (r1 == r3) and (r2==r3):
        print('Você formou um triângulo equilátero!')
    elif (r1==r2) or (r1==r3) or (r2==r3):
        print('Você formou um triângulo isósceles!')
    else:
        print('Você formou um triângulo escaleno!')
else:
    print('Não foi possível formar um triângulo com os valores fornecidos')