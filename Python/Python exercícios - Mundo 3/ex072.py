#CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA COM UMA CONTAGEM POR EXTENSO, DE ZERO ATÉ VINTE.
#SEU PROGRAMA DEVERÁ LER UM NÚMERO PELO TECLADO(ENTRE 0 E 20) E MOSTRÁ-LO POR EXTENSO.

extenso=('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

numero=-1
while numero <0 or numero >20:
    numero=int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {extenso[numero]}.')


#while True:
    #numero=int(input('Digite um número entre 0 e 20:))
    #if 0<=numero<20:
        #break
    #print('Tente novamente.',end='')