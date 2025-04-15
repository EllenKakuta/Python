n1= input('Digite um valor: ')
print(type(n1))

n1= int(input('Digite um valor: '))
print(type(n1))

n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
s = n1+n2
# print('A soma entre',n1, 'e', n2, 'é igual a:', s) FORMATO ANTIGO 
print('A soma entre {} e {} vale {}'.format(n1,n2,s))