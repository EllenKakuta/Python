valorInicial= float(input('Digite o valor do produto: '))
desconto = valorInicial*5/100
valorFinal = valorInicial-desconto
print('O valor final do produto com desconto é R${}. Houve um desconto de R${:.2f}'.format(valorFinal, desconto))