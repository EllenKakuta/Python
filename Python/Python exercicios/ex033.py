#DIZER QUAL É O NÚMERO MAIOR E QUAL É O MENOR

n1= int(input('Digite o primeiro número: '))
n2= int(input('Digite o segundo número: '))
n3= int(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print('{:.0f} é o maior número'.format(n1))
elif n2 > n1 and n2 > n3:
    print('{:.0f} é o maior número'.format(n2))
elif n3 > n1 and n3 > n2:
    print('{:.0f} é o maior número'.format(n3))
elif n1 < n2 and n1<n3:
    print('{:.0f} é o menor número'.format(n1))
elif n2 <n1 and n2<n3:
    print('{:.0f} é o menor número'.format(n2))
else:
    print('{:.0f} é o menor número'.format(n3))


