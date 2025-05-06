#CONDIÇÕES

nome = str(input('Qual é seu nome? '))
if nome == 'Ellen':
    print ('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print ('Bom dia, {}!'.format(nome))

#-----------------------------------------------------------------------------------------
n1=float(input('Digite a primeira nota: '))
n2= float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média é: {:.1f}'.format(m))
if m >=6.0:
    print('Parabéns!')
else:
    print('Estude mais!!!')