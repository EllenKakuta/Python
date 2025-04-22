print('Descubra se o ano é bissexto!')
ano = int(input('Digite o ano: '))
if ano %4==0 and ano%100 !=0 or ano %400==0:
    print('BISSEXTO')
else:
    print ('Não é bissexto')