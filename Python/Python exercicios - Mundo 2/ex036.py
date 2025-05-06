# PROGRAMA PARA APROVAR EMPRÉSTIMO BANCÁRIO PARA COMPRA DE UMA CASA. 
# VAI PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR
# CALCULAR O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO

print('** SIMULE O EMPRÉSTIMO PARA COMPRA DE SUA CASA **')
valorDaCasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salário: R$ '))
anos = int(input('Em quantos anos será realizado o pagamento? '))
parcelas = anos*12
# print(parcelas)
valormensal = valorDaCasa/parcelas
# print(valormensal)

if valormensal > (salario*30/100):
    print ('O valor da parcela ultrapassa o limite permitido. Empréstimo negado')
elif valormensal <= (salario*30/100):
    print('Empréstimo aprovado, você pagará {} parcelas no valor de R${:.2f} cada'.format(parcelas,valormensal))