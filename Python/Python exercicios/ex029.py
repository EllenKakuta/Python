velocidade = int(input('Qual a velocidade do carro? '))
if velocidade >80:
    print('Você ultrapassou a velocidade permitida')
    multa = (velocidade-80)*7
    print('O valor da multa é R${:.2f}'.format(multa))
else:
    print('Boa viagem!!')
