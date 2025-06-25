#CRIE UM PROGRAMA QUE CRIE UMA MATRIZ DE DIMENSÃO 3X3 E PREENCHA COM VALORES LIDOS PELO TECLADO.
#NO FINAL, MOSTRE A MATRIZ NA TELA, COM A FORMATAÇÃO CORRETA
#MATRIZ COM 3 LINHAS E 3 COLUNAS 
#EX: [ 1 ] [ 2 ] [ 3 ]
#    [ 4 ] [ 5 ] [ 6 ]
#    [ 7 ] [ 8 ] [ 9 ]

matriz=[[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0,3):
    for coluna in range (0,3):
        matriz[linha][coluna]=int(input(f'Digite um valor para [{linha}, {coluna}] '))
# print(matriz)
print('-'*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha] [coluna]:^5}]', end='')
    print()