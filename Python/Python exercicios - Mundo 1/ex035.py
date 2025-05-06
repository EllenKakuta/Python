print('É possível formar um triangulo?''\n''Digite o comprimento de 3 retas e terá a resposta')
r1= float(input('Primeira reta: '))
r2= float(input('Segunda reta: '))
r3= float(input('Terceira reta: '))
if (r1+r2 >r3) and (r2+r3>r1) and (r3+r1>r2):
    print('Você formou um triângulo!')
else:
    print('Não foi possível formar um triângulo com os valores fornecidos..')