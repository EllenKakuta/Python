import datetime
print('Descubra se o ano é bissexto!')
ano = int(input('Digite o ano ou digite 0 para o ano atual: '))
if ano ==0:
    ano = datetime.date.today().year
if ano %4==0 and ano%100 !=0 or ano %400==0:
    print('O ano de {} É BISSEXTO'.format(ano))
else:
    print ('O ano de {} NÃO É BISSEXTO'.format(ano))