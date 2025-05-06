velocidade = float(input('Qual a velocidade do carro? '))
if velocidade >80:
    print('Você ultrapassou a velocidade permitida, que é de 80km/h')
    multa = (velocidade-80)*7
    print('O valor da multa a ser paga é R${:.2f}'.format(multa))
else:
    print('Boa viagem!!')
