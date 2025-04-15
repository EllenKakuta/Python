km= float(input('Digite a quantidade de Km percorridos: '))
dias=int(input('Digite a quantidade de dias alugados: '))

valorDiario = dias*60
valorKm= km*0.15
valorTotal = valorDiario+valorKm

print('O valor a ser pago será de R${:.2f}'.format(valorTotal))