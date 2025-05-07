#PROGRAMA QUE CALCULE O IMC E MOSTRE O STATUS DE ACORDO COM A TABELA:
#ABAIXO DE 18.5 - ABAIXO
#ENTRE 18.5 E 25 - PESO IDEAL
#25 ATÉ 30 - SOBREPESO
#30 ATÉ 40 - OBESIDADE
#ACIMA DE 40 - OBESIDADE MÓRBIDA

print('***** CALCULE SEU IMC *****')
peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso/(altura*altura)
if imc < 18.5:
    print('Seu IMC é: {:.1f} - ABAIXO DO PESO'.format(imc))
elif imc >=18.5 and imc <25:
    print('Seu IMC é: {:.1f} - PESO IDEAL'.format(imc))
elif imc >=25 and imc <30:
    print('Seu IMC é: {:.1f} - SOBREPESO'.format(imc))
elif imc >=30 and imc <40:
    print('Seu IMC é: {:.1f} - OBESIDADE'.format(imc))
else:
    print('Seu IMC é: {:.1f} - OBESIDADE MÓRBIDA'.format(imc))