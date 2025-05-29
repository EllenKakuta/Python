#CRIE UM PROGRAMA QUE LEIA O NOME E PREÇO DE VÁRIOS PRODUTOS. O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR. NO FINAL, MOSTRE:
#A) QUAL É O TOTAL GASTO NA COMPRA
#B) QUANTOS PRODUTOS CUSTAM MAIS DE R$1000
#C) QUAL É O NOME E O PREÇO DO PRODUTO MAIS BARATO

produto=total=menor=contador=0
nome=''
print('-'*40)
print('- SUPERMERCADO - ')

while True:
    print('-'*40)
    nome_produto=str(input('Nome do produto: '))
    valor_produto=float(input('Valor do produto: R$'))
    contador+=1
    if valor_produto > 1000:
        produto+=1
    total+=valor_produto
    if contador==1 or valor_produto<menor:
        menor=valor_produto
        nome=nome_produto
    print('-'*40)   
    continua=' '
    while continua not in 'SN':
        continua=str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continua =='N':
        break
print('-'*40)
print(f'Total da compra: R${total:.2f}.')
print(f'{produto} produtos custam mais de R$1000.00.')
print(f'{nome.title()} é o produto mais barato e custa R${menor:.2f}.')
print('-'*40)


