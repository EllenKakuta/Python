#CRIE UM PROGRAMA QUE TENHA UMA TUPLA ÚNICA COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PREÇOS, NA SEQUÊNCIA
#NO FINAL, MOSTRE UMA LISTAGEM DE PREÇOS, ORGANIZANDO OS DADOS EM FORMA TABULAR

produtos=('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)
for p in range(0,len(produtos),2):
    nome = produtos[p]
    valor= produtos[p+1]
    print(f'{nome:.<30} R${valor:>7.2f}')

#CORREÇÃO VIA AULA
# for pos in range(0, len(produtos)):
#     if pos%2==0:
#         print(f'{produtos[pos]:.<30}', end='')
#     else:
#         print(f' R${produtos[pos]:>7.2f}')