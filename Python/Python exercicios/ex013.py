salarioInicial = float(input('Digite o salário inicial: '))
aumento = salarioInicial*15/100
salarioFinal = salarioInicial+aumento
print('O novo salário é R${:.2f}, houve um aumento de R${:.2f}.'.format(salarioFinal, aumento))