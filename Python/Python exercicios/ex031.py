distancia = float(input('Qual a distância da viagem? '))
if distancia <= 200:
    valor1 = distancia*0.5
    print('O valor da passagem é R${:.2f}'.format(valor1))
else:
    valor2 = distancia*0.45
    print('O valor da passagem é R${:.2f}'.format(valor2))
    