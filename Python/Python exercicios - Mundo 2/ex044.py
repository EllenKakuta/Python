#PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO
#À VISTA - DINHEIRO/CHEQUE - 10% DE DESCONTO
#À VISTA - CARTÃO - 5% DE DESCONTO
#EM ATÉ 2X NO CARTÃO - PREÇO NORMAL
#3 OU MAIS VEZES NO CARTÃO - 20% JUROS

precoNormal = float(input('Digite o valor do produto: R$ '))
condicaoPagamento = int(input('Digite 1 para pagamento à vista e 2 para pagamento à prazo: '))
if condicaoPagamento == 1:
    int(input('1- Dinheiro \n' 
    '2- Cheque \n' \
    '3- Cartão \n' \
    '-> '))
    dinheiro = precoNormal-(precoNormal*10/100)
    cheque = precoNormal-(precoNormal*10/100)
    cartao = precoNormal-(precoNormal*5*100)
    if condicaoPagamento ==1:
        print('Valor total a ser pago: R${:.2f}'.format(dinheiro))
    elif condicaoPagamento ==2:
        print('Valor total a ser pago: R${:.2f}'.format(cheque))
    elif condicaoPagamento ==3:
        print('Valor total a ser pago: R${:.2f}'.format(cartao))
    else:
        print('Opção inválida. Digite uma das 3 opções solicitadas')
        