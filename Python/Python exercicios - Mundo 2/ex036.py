# PROGRAMA PARA APROVAR EMPRÉSTIMO BANCÁRIO PARA COMPRA DE UMA CASA. 
# VAI PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR
# CALCULAR O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO

print('** SIMULE O EMPRÉSTIMO PARA COMPRA DE SUA CASA **')
valorDaCasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salário: R$ '))
anos = int(input('Em quantos anos será realizado o pagamento? '))
parcelas = anos*12
# print(parcelas) - coloquei apenas para conferência do cálculo
valorMensal = valorDaCasa/parcelas
# print(valormensal)- coloquei apenas para conferência do cálculo
trintaPorCento = salario*30/100

if valorMensal > (trintaPorCento):
    print ('O valor da parcela ultrapassa o limite permitido. Empréstimo negado')
    print('Valor de cada parcela: R${:.2f}, esse valor excede 30% do seu salário que é R${:.2f}'.format(valorMensal, trintaPorCento))
elif valorMensal <= (trintaPorCento):
    print('Empréstimo aprovado, você pagará {} parcelas no valor de R${:.2f} cada'.format(parcelas,valorMensal))