salarioAtual = float(input('Digite seu salário atual: '))
aumento10 = salarioAtual *(10/100)
aumento15 = salarioAtual*(15/100)
if salarioAtual > 1250.00:
    print('Seu aumento foi de R${:.2f}, totalizando R${:.2f}.'.format(aumento10, salarioAtual+aumento10))
else:
    print ('Seu aumento foi de R${:.2f}, totalizando R${:.2f}.'.format(aumento15, salarioAtual+aumento15))