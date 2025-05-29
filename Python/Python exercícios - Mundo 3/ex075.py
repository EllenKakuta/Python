#DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TECLADO E GUARDE-OS EM UMA TUPLA. NO FINAL, MOSTRE:
#A) QUANTAS VEZES APARECEU O VALOR 9
#B) EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3
#C) QUAIS FORAM OS NÚMEROS PARES

# n1=int(input('Informe o primeiro número: '))
# n2=int(input('Informe o segundo número: '))
# n3=int(input('Informe o terceiro número: '))
# n4=int(input('Informe o quarto número: '))
# numeros =(n1,n2,n3,n4)
numeros=(int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')),int(input('Digite o terceiro número: ')),int(input('Digite o quarto número: ')))
tem_par=False
print(f'Você digitou os valores {numeros}')
if 9 in numeros:
    print(f'O número 9 apareceu: {numeros.count(9)} vezes')
else:
    print('O número 9 não foi digitado nenhuma vez')
if 3 in numeros:
    print(f'O número 3 foi digitado primeiramente na {numeros.index(3)+1}° posição')
else: 
    print('O número 3 não foi digitado nenhuma vez')
print(f'Números pares: ',end='')
for numero in numeros:
    if numero %2==0:
        print(f'{numero} ')
        tem_par=True
if not tem_par:
    print('Não há nenhum número par')