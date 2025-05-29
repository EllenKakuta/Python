#CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNICO. NO INÍCIO, PERGUNTE AO USUÁRIO QUAL SERÁ O VALOR A SER SACADO(NÚMERO INTEIRO) E O PROGRAMA VAI INFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES
#OBS: CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE R$50, R$20, R$10 E R$1


print('----- BANCO -----')
# valor=int(input('Informe o valor do saque: R$'))

# while True:
#     cinquenta = valor//50
#     sobra=valor-cinquenta*50
#     vinte=sobra//20
#     sobra=sobra-vinte*20
#     dez=sobra//10
#     sobra=sobra-dez*10
#     um=sobra//1
#     sobra=sobra-um*1
#     if sobra==0:
#         break
# print(f'{cinquenta} notas de R$50.')
# print(f'{vinte} notas de R$20.')
# print(f'{dez} notas de R$10.')
# print(f'{um} notas de R$1.')


#----------------------------------------------------------------
#RESOLUÇÃO VIA AULA
valor = int(input('Informe o valor do saque: R$'))
total=valor
cedula=50
total_cedula=0
while True:
    if total >=cedula:
        total-=cedula
        total_cedula+=1
    else:
        if total_cedula>0:
            print(f'Total de {total_cedula} cédulas de {cedula}')
        if cedula==50:
            cedula=20
        elif cedula==20:
            cedula=10
        elif cedula==10:
            cedula=1
        total_cedula=0
        if total==0:
            break